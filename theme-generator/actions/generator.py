import copy

from bs4 import BeautifulSoup
from bs4.formatter import XMLFormatter
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers import XmlSerializer

from mapsforge.render_theme import Rule, Cap, Line
from options import Options
from osmc_symbols.osmc_gen import OsmcSymbolGenerator
from xml_templates.config import TemplateVariables


class GeneratorActions:

    def __init__(self, options: Options):

        self.options = options
        self.soup = self._init_soup(options.output_template)

        self.actions = [
            TemplateVariables.gen_action_copy_section,
            TemplateVariables.gen_action_create_highway_tunnels,
            TemplateVariables.gen_action_create_railway_bridge,
            TemplateVariables.gen_action_osmc_colors,
            TemplateVariables.gen_action_sac_scale2lwn,

            TemplateVariables.gen_action_cycle_icn,
            TemplateVariables.gen_action_cycle_basic_to_mtb_scale_0,
            TemplateVariables.gen_action_osmc_symbols_and_order,
        ]

        self.non_supported_attributes = ['poidb', 'gen_section']

    def process_actions(self) -> BeautifulSoup:

        # find places where are required some actions and where results will be placed
        input_sections = []
        for action_name in self.actions:
            input_sections.extend(self.soup.find_all(action='{}'.format(action_name)))

        for input_section in input_sections:

            # find all section that should be used as source for converting to tunnel, bridge etc
            source_sections = self.soup.find_all(gen_section=input_section['source_section'])

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

                # Process different action based on it name
                if action_name == TemplateVariables.gen_action_create_highway_tunnels:
                    self.convert_to_highway_tunnel(source_rule)

                elif action_name == TemplateVariables.gen_action_create_railway_bridge:
                    self.convert_to_railway_bridge(source_rule)

                elif action_name == TemplateVariables.gen_action_osmc_colors:
                    source_rule = self.add_osmc_colors(source_rule)

                elif action_name == TemplateVariables.gen_action_sac_scale2lwn:
                    source_rule = self.gen_action_sac_scale2lwn(source_rule)

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

                #if action_name == TemplateVariables.gen_action_osmc_colors :
                if action_name == TemplateVariables.gen_action_osmc_colors or action_name == TemplateVariables.gen_action_osmc_symbols_and_order:
                    # replace all children in specific section by new child from created rules
                    child = tunnel_soup.findChild()
                    section_soup.replaceWith(child)
                else:
                    # append the created tunnel section into defined place in the tree
                    input_section.parent.extend(tunnel_soup.children)

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

    def add_osmc_colors(self, source_rule):
        """
        For every defined color use original definition (for red color) and duplicate it for every OSMC color
        :param source_rule: definition of marked trails for single color (red)
        :return: rules for all OSMC colors
        """
        color_rules = []

        for key in TemplateVariables.osmc_colors:
            # definition of line width,etc that will be recreated for every osmc color
            color_rule = copy.deepcopy(source_rule.rule[0])

            color_rules.append(self.create_osmc_color_definition(color_rule, key))

        source_rule.rule = color_rules

        return source_rule

    def create_osmc_color_definition(self, source_rule, color_key):
        """
        Replace the color line from original definition
        :param source_rule: xml template section
        :param color_key: color to set
        :return:
        """
        if source_rule.k == 'osmc_color':
            source_rule.v = color_key

        for child_rule in source_rule.rule:
            # inherit zoom and parent rules
            self.create_osmc_color_definition(child_rule, color_key)

        for pathText in source_rule.path_text:
            pathText.fill = TemplateVariables.osmc_colors[color_key]

        for line in source_rule.line:

            line.stroke = TemplateVariables.osmc_colors[color_key]
            line.stroke_linecap = Cap.BUTT

            if color_key == 'green':
                # remove the line from original rule
                source_rule.line.remove(line)

                # part for standard green
                rule = Rule()
                rule.e = 'way'
                rule.k = 'osmc_foreground'
                rule.v = '~|green_arch|green_bar|green_bowl|green_circle|green_corner|green_cross|green_diamond|green_diamond_line|green_dot|green_drop_line|green_fork|green_hiker|green_L|green_rectangle|green_rectangle_line|green_right|green_round|green_slash|green_stripe|green_triangle|green_triangle_line|green_triangle_turned|green_turned_T|green_x|white_arch|white_backslash|white_bar|white_circle|white_corner|white_cross|white_diamond|white_diamond_line|white_dot|white_fork|white_hiker|white_lower|white_pointer|white_rectangle|white_rectangle_line|white_red_diamond|white_right|white_round|white_slash|white_stripe|white_triangle|white_triangle_line|white_turned_T|white_wheelchair|white_x'

                # part for educational green lines
                rule_edu = copy.deepcopy(rule)
                rule_edu.v = 'green_backslash'
                line_edu = copy.deepcopy(line)
                line_edu.stroke_linecap = Cap.ROUND
                line_edu.stroke_dasharray = '1,8,8,8'
                line_edu.stroke_width = line_edu.stroke_width * 0.75

                # add line into the new rule
                rule.line.append(line)
                rule_edu.line.append(line_edu)

                # append the new rules into parent rule
                source_rule.rule.append(rule)
                source_rule.rule.append(rule_edu)

        return source_rule

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

    def remove_nonsupported_attributes(self, soup):
        """
        Remove attributes that aren't supported by renderer
        :param soup:
        """
        for attribute_name in self.non_supported_attributes:
            tags = soup.select('[{}]'.format(attribute_name))
            for tag in tags:
                del tag[attribute_name]


class Osmc2SacScaleGenerator():

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
