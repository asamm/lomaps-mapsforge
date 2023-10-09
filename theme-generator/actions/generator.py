import copy

import bs4.element
from bs4 import BeautifulSoup
from bs4.formatter import XMLFormatter
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers import XmlSerializer

from mapsforge.render_theme import Rule, Cap, Line
from options import Options
from osmc_symbols.osmc_gen import OsmcSymbolGenerator, OsmcLineGenerator
from xml_templates.config import TemplateVariables


class GeneratorActions:

    def __init__(self, options: Options):

        self.options = options
        self.soup = self._init_soup(options.output_template)

        self.actions = [
            TemplateVariables.gen_action_copy_section,
            TemplateVariables.gen_action_create_highway_tunnels,
            TemplateVariables.gen_action_create_railway_bridge,
            TemplateVariables.gen_action_osmc_sac_order,
            TemplateVariables.gen_action_osmc_to_iwn_rwn,

            TemplateVariables.gen_action_cycle_icn,
            TemplateVariables.gen_action_cycle_basic_to_mtb_scale_0,

            # these two actions has to be last ones and in this order because the OSMC section as source section is
            # modified during these actions

            TemplateVariables.gen_action_osmc_colors,
            TemplateVariables.gen_action_osmc_symbols_and_order,
        ]

        self.non_supported_attributes = ['poidb', 'gen_section']

    def process_actions(self) -> BeautifulSoup:

        # find places where are required some actions and where results will be placed
        input_sections = []
        for action_name in self.actions:
            input_sections.extend(self.soup.find_all(action='{}'.format(action_name)))

        for input_section in input_sections:

            # find all section that should be used as source for generator action defined in input section
            source_sections = self.soup.find_all(gen_section='{}'.format(input_section['source_section']))

            if len(source_sections) == 0:
                print("WARNING - Can not find source section for '{}'. "
                      "Please check that gen_section=\"{}\" is defined in template".
                      format(input_section['source_section'], input_section['source_section']))
                continue

            config = ParserConfig(
                fail_on_unknown_properties=True,
                fail_on_unknown_attributes=False,
            )
            parser = XmlParser(config=config)
            serializer = XmlSerializer()

            for section_soup in source_sections:

                # deserialize XML to mapsforge objects (basically into rule and it's content)
                source_rule = parser.from_string(section_soup.prettify(), Rule)

                # get name of action from attribute
                action_name = input_section['action']

                # Proccess different action based on it name
                if action_name == TemplateVariables.gen_action_create_highway_tunnels:
                    self.convert_to_highway_tunnel(source_rule)

                elif action_name == TemplateVariables.gen_action_create_railway_bridge:
                    self.convert_to_railway_bridge(source_rule)

                elif action_name == TemplateVariables.gen_action_osmc_sac_order:
                    source_rule = self.add_osmc_sac_scale(source_rule, input_section)

                elif action_name == TemplateVariables.gen_action_osmc_colors:
                    osmc_line_gen = OsmcLineGenerator(self.options)
                    source_rule = osmc_line_gen.add_osmc_colors(source_rule)

                elif action_name == TemplateVariables.gen_action_osmc_to_iwn_rwn:
                    source_rule = self.gen_action_osmc_to_iwn_rwn(source_rule)

                elif action_name == TemplateVariables.gen_action_osmc_symbols_and_order:

                    osmc_symbol_gen = OsmcSymbolGenerator(self.options)
                    source_rule = osmc_symbol_gen.generate(source_rule)

                elif action_name == TemplateVariables.gen_action_cycle_icn:
                    source_rule = self.create_cycle_sections(source_rule, TemplateVariables.color_cycle_icn_ncn)

                elif action_name == TemplateVariables.gen_action_cycle_basic_to_mtb_scale_0:
                    source_rule = self.create_cycle_sections(source_rule, TemplateVariables.color_cycle_mtb)

                elif action_name == TemplateVariables.gen_action_copy_section:
                    source_rule = self.copy_section(source_rule)
                else:
                    print("Warning unsupported action {}".format(action_name))

                # convert back xsdata object into soup
                tunnel_soup = BeautifulSoup(serializer.render(source_rule), 'xml')

                # if action_name == TemplateVariables.gen_action_osmc_colors :
                if action_name == TemplateVariables.gen_action_osmc_colors or action_name == TemplateVariables.gen_action_osmc_symbols_and_order:
                    # replace all children in specific section by new child from created rules
                    child = tunnel_soup.findChild()
                    section_soup.replaceWith(child)
                elif action_name == TemplateVariables.gen_action_osmc_sac_order:
                    input_section.parent.replaceWith(tunnel_soup.findChild())
                else:
                    # append the created tunnel section into defined place in the tree
                    input_section.parent.extend(tunnel_soup.children)

        for input_section in input_sections:
            # remove the input section from the base xml tree
            input_section.extract()

        # remove other non-supported tags or attributes
        self.remove_nonsupported_attributes(self.soup)

        # write results to final XML file
        self.write_to_file(self.options.result_xml, self.soup)

        print("Generator actions performed for base map theme")

        return self.soup

    def write_to_file(self, output_f, soup):
        """
        Save result into XML file
        :param output_f: path to result XML file
        :param soup: :BeautifulSoup object of prepare theme
        """
        formatter = SortAttributes(indent="\t")
        f = open(output_f, "w")
        f.write(soup.prettify(formatter=formatter))
        f.close()

    def _init_soup(self, output_template):
        """
        Initialize BeautifulSoup from output of Cheetah XML
        :param output_template: path to the xml created by cheetah
        :return: soup instance
        """
        file = open(output_template, "r")
        return BeautifulSoup(file.read(), 'xml')

    def convert_to_highway_tunnel(self, rule: Rule, parent_rules=[], zoom_min=0):
        """
        Find lines in the rules and make them dashed
        :param rule:
        :param parent_rules:
        :param zoom_min:
        """
        # rember parent rules for
        parent_rules.append(rule)

        if rule.zoom_min and rule.zoom_min > zoom_min:
            zoom_min = rule.zoom_min

        # iterate child rules
        for child_rule in rule.rule:
            # inherit zoom and parent rules
            self.convert_to_highway_tunnel(child_rule, parent_rules, zoom_min)

        for line in rule.line:
            # customize the line
            line.stroke_dasharray = TemplateVariables.highway_tunnel_dash_array
            line.stroke_linecap = Cap.BUTT
            if len(line.stroke) == 7:
                line.stroke = line.stroke.replace("#", "#90")

    def convert_to_railway_bridge(self, rule: Rule, parent_rules=[], zoom_min=0):
        """
        Find lines in the rules and make them dashed
        :param rule:
        :param parent_rules:
        :param zoom_min:
        """
        # rember parent rules for
        parent_rules.append(rule)

        if rule.zoom_min and rule.zoom_min > zoom_min:
            zoom_min = rule.zoom_min

        # iterate child rules
        for child_rule in rule.rule:
            # inherit zoom and parent rules
            self.convert_to_railway_bridge(child_rule, parent_rules, zoom_min)

        if len(rule.line) > 0:
            # railway style can consist from multiple line > find the max width to know the width for bridge
            max_width = max(line.stroke_width for line in rule.line)
            bridge_case = Line(stroke_width=max_width + 0.5, stroke="#000000", stroke_linecap=Cap.BUTT)
            bridge_core = Line(stroke_width=max_width + 0.25, stroke="#F7F7F7", stroke_linecap=Cap.BUTT)
            rule.line.clear()
            rule.line.extend([bridge_case, bridge_core])

    def copy_section(self, rule: Rule):
        # nothing to do with source rule
        return rule



    def create_cycle_sections(self, source_rule: Rule, cycle_line_color):
        """
        Find lines in the rules and set color for ICN
        :param source_rule: definition for cycle lines to replace color of lines
        :param cycle_line_color: new color to replace the original colors
                """
        # iterate child rules
        for child_rule in source_rule.rule:
            self.create_cycle_sections(child_rule, cycle_line_color)

        for line in source_rule.line:
            # customize the line
            line.stroke = cycle_line_color

        return source_rule

    ## OSMC SYMBOLS section ------------------------
    def add_osmc_symbols_order(self, source_rule):
        """
        Generate almost identical rules for OSMC lines only offset is increased to create multiple lines along paths
        :param source_rule: definition for the first line with basic offset
        :return:
        """
        symbol_orders_rules = []

        for order in range(0, 3):
            # definition of line width,etc. that will be recreated for every osmc color
            symbol_rule = copy.deepcopy(source_rule.rule[0])

            symbol_orders_rules.append(self.create_osmc_symbol_order(symbol_rule, order))

        source_rule.rule = symbol_orders_rules

        return source_rule

    def create_osmc_symbol_order(self, source_rule, order: int):
        """
        Change offset of lines based on the order value
        :param source_rule
        :param order
        """
        if source_rule.k == 'osmc_order':
            if order == 0:
                source_rule.v = "~"  # for first order do not print counter
            else:
                source_rule.v = str(order)

        for child_rule in source_rule.rule:
            # inherit zoom and parent rules
            self.create_osmc_symbol_order(child_rule, order)

        for lineSymb in source_rule.line_symbol:
            lineSymb.repeat_start = lineSymb.repeat_start + 1.1 * order * lineSymb.symbol_width

        return source_rule

    def gen_action_sac_scale2lwn(self, source_rule: Rule) -> Rule:

        # filter rules for sac_scale different to "sac_scale=hiking" (only style for hiking sac is used as style for LWN pr IWN)

        if source_rule.k == "osmc_order":
            filtered_rules = [child_rule for child_rule in source_rule.rule if self._is_sac_scale_hiking(child_rule)]
            source_rule.rule = filtered_rules

        for child_rule in source_rule.rule:
            # inherit zoom and parent rules
            self.gen_action_sac_scale2lwn(child_rule)
        return source_rule

    def _is_sac_scale_hiking(self, rule: Rule):
        if rule.k == "sac_scale":
            return rule.v == "~" or rule.v == "hiking"

        return False

    def gen_action_osmc_to_iwn_rwn(self, source_rule: Rule) -> Rule:
        """
        Use definition of standard hiking routes and convert it for routes in network IWN,NWN,RWN,LWN
        :param source_rule: definition for offset of hiking routes with OSMC symbol
        :return: #Rule
        """
        if source_rule.k == "*" and source_rule.v == "*":
            children = source_rule.rule
            if len(children) != 1:
                print('WARNING incorrect definition for "osmc_hiking" section at "osmc_color" section. (Parent can '
                      'contain only one child of "osmc_color")')
                return source_rule

            # skip rule for osmc_color
            sub_children_rules = children[0].rule
            source_rule.rule = sub_children_rules

        for child_rule in source_rule.rule:
            # find lines in the children rules and set IWN/RWN color
            child_rule = self.set_iwn_rwn_line_style(child_rule)
        return source_rule

    def set_iwn_rwn_line_style(self, source_rule: Rule):
        """
        Recursively find all lines in rules and change color to defined color for IWN/RWN...
        :param source_rule:
        :return: #Rule
        """
        for child_rule in source_rule.rule:
            self.set_iwn_rwn_line_style(child_rule)

        for line in source_rule.line:
            line.stroke = TemplateVariables.color_hiking_iwn_nwn

        return source_rule

    def add_osmc_sac_scale(self, source_rule: Rule, input_section: bs4.element.Tag) -> Rule:
        """
        Ass source rules are used the SAC defintion for order=0. Obtain current zoom level and order to offset the line
        :param input_section: Rule as soup object where result will be placed
        :param source_rule:
        :return:
        """
        parent_tag = input_section.parent.parent
        order = int(parent_tag['v'])
        zoom_min = int(self.find_first_parent_with_attribute(input_section, 'zoom-min'))

        # if zoom_min is in range 16 - 17
        if zoom_min in range(12, 15):
            self.increase_osmc_sac_dy(source_rule, TemplateVariables.osmc_hiking_width_z13 * 1.1 * order)
        elif zoom_min in range(16, 17):
            self.increase_osmc_sac_dy(source_rule, TemplateVariables.osmc_hiking_width_z16 * 1.1 * order)
        elif zoom_min >= 18:
            self.increase_osmc_sac_dy(source_rule, TemplateVariables.osmc_hiking_width_z18 * 1.1 * order)
        return source_rule;

    def increase_osmc_sac_dy(self, rule: Rule, line_offset, pathtext_offset = 0):
        for child_rule in rule.rule:
            self.increase_osmc_sac_dy(child_rule, line_offset, pathtext_offset)

        for line in rule.line:
            if line.dy >= 0:
                line.dy = line.dy + line_offset
            else:
                line.dy = line.dy - line_offset

        for path_text in rule.path_text:
            if path_text.dy >= 0:
                path_text.dy = path_text.dy + pathtext_offset
            else:
                path_text.dy = path_text.dy - pathtext_offset

    def remove_nonsupported_attributes(self, soup):
        """
        Remove attributes that aren't supported by renderer
        :param soup:
        """
        for attribute_name in self.non_supported_attributes:
            tags = soup.select('[{}]'.format(attribute_name))
            for tag in tags:
                del tag[attribute_name]

    def find_first_parent_with_attribute(self, tag: bs4.element.Tag, key):
        """
        Iterate parents of soup tag object and search for any parent with defined attribute key.
        It can be used to find parent with defined zoom that's ingerited for children
        :param key: attribute key to find
        """

        if tag.has_attr(key):
            return tag[key];
        return self.find_first_parent_with_attribute(tag.parent, key)


class Osmc2SacScale():

    def add_sac_scale(self, source_rule, parent_rule=None, zoom_min=0):

        if source_rule.zoom_min and source_rule.zoom_min > zoom_min:
            zoom_min = source_rule.zoom_min

        # iterate child rules
        for child_rule in source_rule.rule:

            if self._is_osmc_order_rule(child_rule):
                # this rule will be converted into SAC SCALE
                rule = copy.deepcopy(child_rule)

                self._order_rule_2_sac(rule)

                sac_rules = self._order2sac(child_rule)

            # inherit zoom and parent rules
            self.convert_to_highway_tunnel(child_rule, parent_rule, zoom_min)

    def _is_osmc_order_rule(self, rule: Rule):
        return rule.k == "osmc_order" and (rule.v == "~" or rule.v == "1")

    def _order_rule_2_sac(self, rule):
        pass


class SortAttributes(XMLFormatter):
    def attributes(self, tag):
        """Reorder a tag's attributes based on this order."""
        attrib_order = ['cat', 'e', 'k', 'v', 'zoom-min', 'zoom-max']
        new_order = []
        for element in attrib_order:
            if element in tag.attrs:
                new_order.append((element, tag[element]))
        for pair in tag.attrs.items():
            if pair not in new_order:
                new_order.append(pair)
        return new_order
