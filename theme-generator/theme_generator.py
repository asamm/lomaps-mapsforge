# Generator of Mapsforge LoMaps V4 theme using templates and other variables
import argparse
import os
from venv import create

import yaml

from actions.generator import GeneratorActions
from options import Options, OsmcSymbolDef
from actions.icon_validator import IconValidator
from helpers import copy_theme_to_device, transform_cheetah_template, publish_theme_to_android_module, \
    create_theme_zip_for_publish
from osmc_symbols.osmc_gen import SvgIconColorizer
from poi_theme import PoiThemeGenerator


def get_osmc_folder_path(result_xml):
    """
    Prepare path to folder where are stored osmc symbols
    :param result_xml: path to result_xml file
    :return: path to folder where are store osmc symbols
    """
    return os.path.join(os.path.dirname(result_xml), 'osmc')
def parse_cmd() -> Options:
    """
    Parse command line parameters
    """

    parser = argparse.ArgumentParser(
        description='Tools to generate LoMaps theme from XML template',
        add_help=True
    )

    parser.add_argument("-bt", "--baseTemplate", type=str,
                        help="Path to folder with theme template (custom theme file with directives to " +
                             "generated specific parts of the theme",
                        default='xml_templates/theme_template.xml')

    parser.add_argument("-rt", "--resultTheme", type=str,
                        help="Path to file to export the generated themes. Set the path for the main map theme." +
                             "The POIs themes are generated in the same location",
                        default='../theme/theme.xml')

    parser.add_argument("-tc", "--templateConfig", type=str,
                        help="Path to file with variables for base template. " +
                             "Cheetah used it to replace the values in base template",
                        default='xml_templates/config.py')

    parser.add_argument("-ac", "--apdbConfig", type=str,
                        help="Path to file with configuration of Offline POI database",
                        default='xml_templates/config_apDb.xml')

    parser.add_argument("-i", "--generateOsmcSvg", action='store_true', default=False,
                        help="Generate all types of OSMC svg symbols from black SVG file that contains all icons")

    parser.add_argument("-c", "--copyToDevice", action='store_true', default=False,
                        help="Copy theme files to the Android device")

    parser.add_argument("-pa", "--publishForAndroid", action='store_true', default=False,
                        help='Copy theme files to the custom Android module folder. ' +
                             'To be ready for publish release version.')

    parser_options = parser.parse_args()

    # store CMD params in options

    option = Options(parser_options.baseTemplate,
                     parser_options.apdbConfig,
                     parser_options.templateConfig,
                     parser_options.resultTheme,
                     parser_options.generateOsmcSvg,
                     parser_options.copyToDevice,
                     parser_options.publishForAndroid)

    return option


def read_options_yaml(file, option) -> Options:
    option_yaml = yaml.safe_load(open(file))

    option.android_module_path = option_yaml['Options']['android_module_path']
    option.locus_theme_path = option_yaml['Options']['locus_theme_path']
    option.output_template = option_yaml['Options']['output_template']
    option.locus_action_zip = option_yaml['Options']['locus_action_zip']

    option.osmc_symbol = OsmcSymbolDef(
        option_yaml['OsmcSymbol']['color'],
        option_yaml['OsmcSymbol']['foreground'],
        option_yaml['OsmcSymbol']['background']
    )

    return option


if __name__ == '__main__':

    # get parameters from CMD
    options = parse_cmd()

    # read default parameters from config yaml
    options = read_options_yaml('options.yaml', options)

    # generate OSMC symbols from black SVG file
    if options.generate_osmc_svg:
        svg_generator = SvgIconColorizer(get_osmc_folder_path(options.result_xml), options)
        svg_generator.generate_icons()

    # replace colors, width, etc in source XML
    transform_cheetah_template(options.theme_template, options.output_template)

    # generate custom parts (bridges, tourist paths), write results to final XML theme file
    generator_actions = GeneratorActions(options)
    theme_soup_generated = generator_actions.process_actions()  # in this method is result exported in to the result xml

    # result of generation action in soup object for validation if required icons exists
    icon_validator = IconValidator(theme_soup_generated, options.result_xml)
    icon_validator.validate()

    # delete temp file (export from cheetah)
    os.remove(options.output_template)

    # POI THEMES - generate custom theme that render only POI icons
    poi_theme_generator = PoiThemeGenerator(options.apdb_config_xml, options.result_xml)
    poi_theme_files = poi_theme_generator.generate_render_themes()

    if options.copy_to_device:
        # copy map theme to phone
        copy_theme_to_device(options.result_xml, options.locus_theme_path)
        # copy POI themes do device
        for poi_theme_file in poi_theme_files:
            # copy poi theme
            copy_theme_to_device(poi_theme_file, options.locus_theme_path)

    if options.publish_for_android:
        publish_theme_to_android_module(os.path.dirname(options.result_xml), options.android_module_path)

        # create archive that can be downloaded from github for direct usage on android device
        create_theme_zip_for_publish(os.path.dirname(options.result_xml), options.locus_action_zip)

    print("=============  DONE  ================= ")
