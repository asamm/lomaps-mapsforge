import copy
import os

import svgutils
from bs4 import BeautifulSoup
from svgutils.compose import SVG
from svgutils.transform import SVGFigure

from options import Options
from mapsforge.render_theme import Rule, LineSymbol
from xml_templates.config import TemplateVariables


class SvgIconColorizer():

    def __init__(self, export_dir, options: Options):
        self.export_dir = export_dir
        self.options = options

    def generate_icons(self):

        """
        Iterate through svg icons in resources/osmc. Make copy of SVG icon and replace full black (#000000) to color
        defined on #TemplateVariables.colors
        """

        # find all SVG files in resources/osmc
        svg_icons = []
        for file in os.listdir('resources/osmc'):
            if file.endswith('.svg') :
                svg_icons.append(os.path.join('resources/osmc', file))

        for svg_icon in svg_icons:
            for color_name in self.options.osmc_symbol.color:
                # get hex code of color from TemplateVariables.colors
                if color_name not in TemplateVariables.osmc_colors and color_name != 'white':
                    print('Color ' + color_name + ' not found in TemplateVariables.osmc_colors. '
                                                  'Can not generate icon for this color.')
                    continue

                # set custom color for white that isn't defined in TemplateVariables.colors
                if color_name == 'white':
                    color_value = '#fcfcfc'
                else:
                    color_value = TemplateVariables.osmc_colors[color_name]

                # colorize icon
                svg_str = self._colorize_icon(svg_icon, color_value)

                # get icon file name from path
                icon_name = os.path.basename(svg_icon)

                # find occurrence of first '_' in file name and insert color name after it into file name and
                colorized_icon_name = icon_name[:icon_name.find('_')+1] + color_name + icon_name[icon_name.find('_'):]

                # remove potential trailing '_' in file name part
                colorized_icon_name = colorized_icon_name.replace('_.', '.')

                # check if destination directory exists, if not create it
                if not os.path.exists(self.export_dir):
                    os.makedirs(self.export_dir)

                # save colored svg to file
                with open(os.path.join(self.export_dir, colorized_icon_name), 'w') as f:
                    f.write(svg_str)

    def _colorize_icon(self, svg_icon, color: str = '#000000'):
        """
        Read SVG file, use beautiful soup to find all black elements and replace it by color. Return SVG as string
        :param svg_icon: path to icon to colorize
        :param color: color to replace black with

        """

        with open(svg_icon, 'r') as f:
            soup = BeautifulSoup(f, 'xml')

        black_elements = soup.find_all(lambda tag: tag.has_attr('fill') and tag['fill'] == '#000000' or
                                              tag.has_attr('stroke') and tag['stroke'] == '#000000')

        # Find all elements without fill and stroke attributes and append them to black_elements list
        black_elements.extend(soup.find_all(lambda tag: not tag.has_attr('fill') and not tag.has_attr('stroke')))

        for elem in black_elements:
            elem['fill'] = color
            elem['stroke'] = color

        # return string representation of svg file
        return soup.prettify()


class OsmcSymbolGenerator():

    def __init__(self, options: Options):

        self.options = options

    def generate(self, source_rule: Rule):
        """
        :param source_rule: rule for whole osmc_order section
        :return: :Rule with defined osmc line symbols and orders

        """


        rule = self._generate_symbols_rules(source_rule)

        rule = self._generate_osmc_symbols_order(rule)

        return rule

    def _generate_symbols_rules(self, source_rule: Rule):
        """
        From the basic firs symbol definition generate all possible alternatives for symbol foreground and background
        :param source_rule: rule for whole osmc_order section
        :return: :Rule
        """
        line_symbol_def = self.get_line_symbol_def(source_rule)

        first_symbol_rule = source_rule.rule[0]

        for color in self.options.osmc_symbol.color:
            for foreground in self.options.osmc_symbol.foreground:
                icon_value = '{}_{}'.format(color, foreground)
                rule = Rule(e=first_symbol_rule.e, cat=first_symbol_rule.cat, k="osmc_foreground", v=icon_value)

                icon_path = 'file:osmc/frg_{}.svg'.format(icon_value)
                line_symbol = copy.deepcopy(line_symbol_def)
                line_symbol.src = icon_path
                rule.line_symbol.append(line_symbol)

                source_rule.rule.append(rule)

            for background in self.options.osmc_symbol.background:
                if background:
                    icon_value = '{}_{}'.format(color, background)
                else:
                    # special background symbol with rectangle filled with color has the same name as color
                    icon_value = color

                rule = Rule(e=first_symbol_rule.e, cat=first_symbol_rule.cat, k="osmc_background", v=icon_value)

                icon_path = 'file:osmc/bcg_{}.svg'.format(icon_value)
                line_symbol = copy.deepcopy(line_symbol_def)
                line_symbol.src = icon_path
                line_symbol.priority = line_symbol.priority - 1
                rule.line_symbol.append(line_symbol)

                source_rule.rule.append(rule)

        return source_rule

    def _generate_osmc_symbols_order(self, source_rule) -> Rule:
        """
        Generate almost identical rules for OSMC symbol only repeat start is change to print multiple symbols next each other
        :param source_rule: definition for the section with not defined order
        :return: :Rule containing multiple definition for osmc symbols with different repeat-start for line_symbol
        """
        parent_rule = Rule(e="any", k="*", v="*")

        for order in range(0, 3):
            # definition of line width,etc. that will be recreated for every osmc color
            symbol_rule = copy.deepcopy(source_rule)

            parent_rule.rule.append(self.create_osmc_symbol_order(symbol_rule, order))

        return parent_rule

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

    def get_line_symbol_def(self, source_rule) -> LineSymbol:
        """
        Obtain default definition for render style of osmc symbol
        :param source_rule: section specified line symbol for osm
        :return: :LineSymbol
        """

        if len(source_rule.rule) != 1 and source_rule.rule.k != 'osmc_order':
            raise Exception("Rule for OSMC symbol has to parent for 'osmc_order' section")
        if len(source_rule.rule[0].line_symbol) != 1:
            raise Exception("Rule for OSMC symbol has to contain single LineSymbol definition")
        return source_rule.rule[0].line_symbol[0]
