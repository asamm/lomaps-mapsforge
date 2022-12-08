# Generator of Mapsforge LoMaps V4 theme using templates and other variables
import copy
import os
from dataclasses import dataclass

from bs4.formatter import XMLFormatter
from xsdata.formats.dataclass.parsers.config import ParserConfig

from bs4 import BeautifulSoup

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer

from config import TemplateVariables

from mapsforge import Rule, Cap, Line, Linejoin, LineSymbol


@dataclass
class Options:
    input_template: str
    output_template: str
    result_xml: str

class SortAttributes(XMLFormatter):
    def attributes(self, tag):
        """Reorder a tag's attributes however you want."""
        attrib_order = ['cat','e', 'k', 'v', 'zoom-min', 'zoom-max']
        new_order = []
        for element in attrib_order:
            if element in tag.attrs:
                new_order.append((element, tag[element]))
        for pair in tag.attrs.items():
            if pair not in new_order:
                new_order.append(pair)
        return new_order

class GeneratorActions:

    def __init__(self, options: Options):

        self.options = options
        self.soup = self._init_soup(options.output_template)

        self.actions = [
            TemplateVariables.gen_action_create_highway_tunnels,
            TemplateVariables.gen_action_create_railway_bridge,
            TemplateVariables.gen_action_osmc_colors,
            TemplateVariables.gen_action_cycle_icn,
            TemplateVariables.gen_action_cycle_basic_to_mtb_scale_0,
            TemplateVariables.gen_action_osmc_symbols_order,

        ]

    def process_actions(self):

        # find places where are required some actions and where results will be placed
        input_sections = []
        for action_name in self.actions:
            input_sections.extend(self.soup.find_all(f='{}'.format(action_name)))

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

                # convert lines to tunnel style
                action_name = input_section['f']
                if action_name == TemplateVariables.gen_action_create_highway_tunnels:
                    self.convert_to_highway_tunnel(source_rule)

                elif action_name == TemplateVariables.gen_action_create_railway_bridge:
                    self.convert_to_railway_bridge(source_rule)

                elif action_name == TemplateVariables.gen_action_osmc_colors:
                    source_rule = self.add_osmc_colors(source_rule)

                elif action_name == TemplateVariables.gen_action_osmc_symbols_order:
                    source_rule = self.add_osmc_symbols_order(source_rule)

                elif action_name == TemplateVariables.gen_action_cycle_icn:
                    source_rule = self.create_cycle_sections(source_rule,TemplateVariables.color_cycle_icn_ncn )

                elif action_name == TemplateVariables.gen_action_cycle_basic_to_mtb_scale_0:
                    source_rule = self.create_cycle_sections(source_rule,TemplateVariables.color_cycle_mtb )

                else:
                    print("Warning unsupported action {}".format(action_name))

                # convert back xsdata object into soup
                tunnel_soup = BeautifulSoup(serializer.render(source_rule), 'xml')

                if action_name == TemplateVariables.gen_action_osmc_colors or action_name ==  TemplateVariables.gen_action_osmc_symbols_order:
                    # replace all childs in specific section by new child from created rules
                    child = tunnel_soup.findChild()
                    section_soup.replaceWith(child)
                else:
                    # append the created tunnel section into defined place in the tree
                    input_section.parent.extend(tunnel_soup.children)


                del section_soup['gen_section']

            # remove the
            input_section.extract()


        # write results to final XML file
        self.write_to_file(self.options.result_xml, self.soup)

    def write_to_file(self, output_f, soup):
        """
        Save resutl into XML file
        :param output_f:
        """
        formatter = SortAttributes(indent="\t")
        f = open(output_f, "w")
        f.write(soup.prettify(formatter=formatter))
        f.close()

    def _init_soup(self, output_template):
        """
        Initialize BeautifulSoup from output of Cheetag XML
        :param output_template:
        :return: soup instance
        """
        file = open(output_template, "r")
        return BeautifulSoup(file.read(), 'xml')

    def convert_to_highway_tunnel(self, rule: Rule, parent_rules=[], zoom_min = 0):
        """
        Find lines in the rulles and make them dashed
        :param rule:
        :param parent_rules:
        :param zoom_min:
        """
        # rember parent rules for
        parent_rules.append(rule)

        if rule.zoom_min and rule.zoom_min > zoom_min:
            zoom_min = rule.zoom_min

        #iterate child rules
        for child_rule in rule.rule:
            # inherit zoom and parent rules
            self.convert_to_highway_tunnel(child_rule, parent_rules, zoom_min)

        for line in rule.line:
            # customize the line
            line.stroke_dasharray = TemplateVariables.highway_tunnel_dash_array
            line.stroke_linecap = Cap.BUTT

    def convert_to_railway_bridge(self, rule: Rule, parent_rules=[], zoom_min = 0):
        """
        Find lines in the rulles and make them dashed
        :param rule:
        :param parent_rules:
        :param zoom_min:
        """
        # rember parent rules for
        parent_rules.append(rule)

        if rule.zoom_min and rule.zoom_min > zoom_min:
            zoom_min = rule.zoom_min

        #iterate child rules
        for child_rule in rule.rule:
            # inherit zoom and parent rules
            self.convert_to_railway_bridge(child_rule, parent_rules, zoom_min)

        if len(rule.line) > 0:
            # railway style can consist from multiple line > find the max width to know the width for bridge
            max_width = max (line.stroke_width for line in rule.line)
            bridge_case = Line(stroke_width = max_width + 0.5, stroke = "#000000", stroke_linecap = Cap.BUTT)
            bridge_core = Line(stroke_width = max_width + 0.25, stroke="#F7F7F7", stroke_linecap = Cap.BUTT)
            rule.line.clear()
            rule.line.extend([bridge_case, bridge_core])

    def add_osmc_colors(self, source_rule):

        color_rules = []

        for key in TemplateVariables.osmc_colors:
            # definition of line width,etc that will be recreated for every osmc color
            color_rule = copy.deepcopy(source_rule.rule[0])

            color_rules.append(self.create_osmc_color_definition(color_rule,key))

        source_rule.rule = color_rules

        return source_rule

    def create_osmc_color_definition (self, source_rule, color_key):

        if source_rule.k == 'osmc_color':
            source_rule.v = color_key

        for child_rule in source_rule.rule:
            # inherit zoom and parent rules
            self.create_osmc_color_definition(child_rule, color_key)

        for line in source_rule.line:
            line.stroke = TemplateVariables.osmc_colors[color_key]
            line.stroke_linecap = Cap.BUTT

        return source_rule

    ## --------------------------

    def create_cycle_sections(self, source_rule: Rule, cycle_line_color):
        """
        Find lines in the rules and set color for ICN
        :param rule:
                """
        # iterate child rules
        for child_rule in source_rule.rule:
            self.create_cycle_sections(child_rule,cycle_line_color)

        for line in source_rule.line:
            # customize the line
            line.stroke = cycle_line_color

        return source_rule

    ## OSMC SYMBOLS section ------------------------
    def add_osmc_symbols_order(self, source_rule):
        symbol_orders_rules = []

        for order in range(0, 3):
            # definition of line width,etc that will be recreated for every osmc color
            symbol_rule = copy.deepcopy(source_rule.rule[0])

            symbol_orders_rules.append(self.create_osmc_symbol_order(symbol_rule, order))

        source_rule.rule = symbol_orders_rules

        return source_rule

    def create_osmc_symbol_order(self, source_rule, order:int):

        if source_rule.k == 'osmc_order':
            if order == 0:
                source_rule.v = "~"  #for first order do not print counter
            else:
                source_rule.v = str(order)

        for child_rule in source_rule.rule:
            # inherit zoom and parent rules
            self.create_osmc_symbol_order(child_rule, order)

        for lineSymb in source_rule.line_symbol:
            lineSymb.repeat_start = lineSymb.repeat_start + 1.1 * order * lineSymb.symbol_width

        return source_rule


def transform(base_xml, result_xml):
    """
    Read input template xml with python variables and replace variables by value using cheetah
    :param base_xml: path to xml template
    :param result_xml:
    """
    template = TemplateVariables(file = base_xml)

    f = open(result_xml, "w")
    f.write(str(template))
    f.close()


def copy_theme_to_device(result_xml):
    # copy xml theme file to android device
    os.popen( "adb push {} /sdcard/Android/data/menion.android.locus/files/Locus/mapsVector/_themes/lomaps_v4/lomaps_v4.xml"
        .format(result_xml))
    # os.popen("adb shell am force-stop menion.android.locus")
    # os.popen("adb shell monkey -p menion.android.locus -c android.intent.category.LAUNCHER 1")
    os.popen("adb shell am broadcast -p menion.android.locus -a com.asamm.locus.ACTION_TASK --es tasks '''{ map_reload_theme: {} }'''")


if __name__ == '__main__':
    #options = parseOptions()
    options = Options('../xml_templates/base.xml',
                      '../xml_templates/base_output.xml',
                      '../lomaps_v4/lomaps_v4.xml')

    transform(options.input_template, options.output_template)

    GeneratorActions(options).process_actions()

    copy_theme_to_device(options.result_xml)



    print("=============  DONE  ================= ")
