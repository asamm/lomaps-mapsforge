# Generator of Mapsforge LoMaps V4 theme using templates and other variables
import copy
import fileinput
import glob
import os
import shutil
from dataclasses import dataclass
from distutils.dir_util import copy_tree

from bs4.formatter import XMLFormatter
from xsdata.formats.dataclass.parsers.config import ParserConfig

from bs4 import BeautifulSoup

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer

from config import TemplateVariables
from poi_theme import PoiThemeGenerator

from mapsforge.render_theme import Rule, Cap, Line, Linejoin, LineSymbol


@dataclass
class Options:
    input_template: str
    output_template: str
    result_xml: str
    android_module_path: str = '../android/src/main/assets/themes/mapsforgeV4/base/'


class SortAttributes(XMLFormatter):
    def attributes(self, tag):
        """Reorder a tag's attributes however you want."""
        attrib_order = ['cat', 'e', 'k', 'v', 'zoom-min', 'zoom-max']
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
            TemplateVariables.gen_action_sac_scale2lwn,

            TemplateVariables.gen_action_cycle_icn,
            TemplateVariables.gen_action_cycle_basic_to_mtb_scale_0,
            TemplateVariables.gen_action_osmc_symbols_order,
        ]

        self.non_supported_attributes = ['poidb']

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

                elif action_name == TemplateVariables.gen_action_sac_scale2lwn:
                    source_rule = self.gen_action_sac_scale2lwn(source_rule)

                elif action_name == TemplateVariables.gen_action_osmc_symbols_order:
                    source_rule = self.add_osmc_symbols_order(source_rule)

                elif action_name == TemplateVariables.gen_action_cycle_icn:
                    source_rule = self.create_cycle_sections(source_rule, TemplateVariables.color_cycle_icn_ncn)

                elif action_name == TemplateVariables.gen_action_cycle_basic_to_mtb_scale_0:
                    source_rule = self.create_cycle_sections(source_rule, TemplateVariables.color_cycle_mtb)

                else:
                    print("Warning unsupported action {}".format(action_name))

                # convert back xsdata object into soup
                tunnel_soup = BeautifulSoup(serializer.render(source_rule), 'xml')

                if action_name == TemplateVariables.gen_action_osmc_colors or action_name == TemplateVariables.gen_action_osmc_symbols_order:
                    # replace all childs in specific section by new child from created rules
                    child = tunnel_soup.findChild()
                    section_soup.replaceWith(child)
                else:
                    # append the created tunnel section into defined place in the tree
                    input_section.parent.extend(tunnel_soup.children)

                # remove attribute defining the source section for generation
                del section_soup['gen_section']

            # remove the input section from the base xml tree
            input_section.extract()

        # remove other non-supported tags or attributes
        self.remove_nonsupported_attributes(self.soup)

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

    def convert_to_highway_tunnel(self, rule: Rule, parent_rules=[], zoom_min=0):
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
        Find lines in the rulles and make them dashed
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

    def add_osmc_colors(self, source_rule):
        """
        For every defined color use original definition (for red color) and duplicate it
        :param source_rule:
        :return:
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
        :param rule:
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
        symbol_orders_rules = []

        for order in range(0, 3):
            # definition of line width,etc that will be recreated for every osmc color
            symbol_rule = copy.deepcopy(source_rule.rule[0])

            symbol_orders_rules.append(self.create_osmc_symbol_order(symbol_rule, order))

        source_rule.rule = symbol_orders_rules

        return source_rule

    def create_osmc_symbol_order(self, source_rule, order: int):

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

    def remove_nonsupported_attributes(self, soup):

        for attribute_name in self.non_supported_attributes:
            tags = soup.select('[{}]'.format(attribute_name))
            for tag in tags:
                del tag[attribute_name]


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


class IconValidator():

    def __init__(self, theme_soup, theme_location):

        self.soup = theme_soup
        self.theme_location = theme_location

    def validate(self):
        """
        Check if all icons(symbols) defined in the base xml are available in the theme folder
        Missing icons are reported in txt file "missing_icons.txt"
        """
        icon_paths = self._get_icon_paths()
        missing_icons = []
        for icon in icon_paths:
            full_path = os.path.normpath(os.path.join(os.path.dirname(self.theme_location), icon))
            if not os.path.exists(full_path):
                if icon not in missing_icons:
                    missing_icons.append(icon)

    def _write_missing_icons_to_file(self, missing_icons):
        log_file = 'missing_icons.txt'

        # remove file if exist
        if os.path.exists(log_file):
            os.remove(log_file)

        if len(missing_icons) > 0:
            # sort alphbetically the icons paths
            missing_icons.sort()
            with open(log_file, 'w') as f:
                f.writelines('\n'.join(missing_icons))

            print("WARNING: the theme contains definition of symbols that doesn't exist in theme folder. Check " +
                  "missing icons in text file: {}".format(log_file))

    def _get_icon_paths(self) -> list:
        """

        :return: list of local path used as sources for symbols
        """
        tags = self.soup.select('[src]')

        paths = []
        for tag in self.soup.select('[src]'):
            if tag['src'].startswith('file:'):
                paths.append(tag['src'].replace('file:/', '').replace('file:', ''))
        return paths


##################################
def transform(base_xml, result_xml):
    """
    Read input template xml with python variables and replace variables by value using cheetah
    :param base_xml: path to xml template
    :param result_xml:
    """
    template = TemplateVariables(file=base_xml)

    f = open(result_xml, "w")
    f.write(str(template))
    f.close()

def copy_theme_to_android_module(options: Options):

    # remove previous files
    delete_folder_content(options.android_module_path)

    # copy new generated theme
    copy_tree(os.path.dirname(options.result_xml), options.android_module_path)

    # replace path in theme files from 'file:' to 'assets:'
    for filename in os.listdir(options.android_module_path):
        if not filename.endswith('.xml'): continue

        filename = os.path.join(options.android_module_path, filename)

        with fileinput.FileInput(filename, inplace=True) as file:
            for line in file:
                print(line.replace('file:', 'assets:'), end='')

        # # Read in the file
        # with open(filename, 'r') as file :
        #     file_data = file.read()
        #     file.close()
        #
        # # Replace the target string
        # file_data = file_data.replace('file:', 'assets:')
        #
        # # Write the file out again
        # with open(filename, 'w') as f:
        #     file.write(file_data)
        #     file.close()

def copy_theme_to_device(result_xml):
    # copy xml theme file to android device
    os.popen(
        "adb push {} /sdcard/Android/data/menion.android.locus/files/Locus/mapsVector/_themes/lomaps_v4/{}"
        .format(result_xml, os.path.basename(result_xml)))
    # os.popen("adb shell am force-stop menion.android.locus")
    # os.popen("adb shell monkey -p menion.android.locus -c android.intent.category.LAUNCHER 1")
    os.popen(
        "adb shell am broadcast -p menion.android.locus -a com.asamm.locus.ACTION_TASK --es tasks '''{ map_reload_theme: {} }'''")

def delete_folder_content(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete {}}. Reason: {}}'.format(file_path, e))

if __name__ == '__main__':
    # options = parseOptions()
    options = Options('xml_templates/base.xml',
                      'xml_templates/base_output.xml',
                      '../theme/theme_v4.xml')

    # replace colors, width, etc in source XML
    transform(options.input_template, options.output_template)

    # generate custom parts (bridges, tourist paths)
    generator_actions = GeneratorActions(options)
    generator_actions.process_actions()

    # result of generation action in soup object
    theme_soup = generator_actions.soup
    icon_validator = IconValidator(theme_soup, options.result_xml)
    icon_validator.validate()

    # delete temp file
    os.remove(options.output_template)

    # copy map theme
    copy_theme_to_device(options.result_xml)

    # Generate custom theme that render only POI icons
    poi_theme_generator = PoiThemeGenerator('poidb/config_apDb.xml', options.result_xml)
    poi_theme_files = poi_theme_generator.generate_render_themes()
    # copy POI themes do device
    for poi_theme_file in poi_theme_files:
        # copy poi theme
        copy_theme_to_device(poi_theme_file)

    # for release
    copy_theme_to_android_module(options)



    print("=============  DONE  ================= ")