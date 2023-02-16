# Generator of Mapsforge LoMaps V4 theme using templates and other variables
import argparse
import fileinput
import os
from distutils.dir_util import copy_tree

import yaml

from actions.generator import GeneratorActions, Options
from actions.icon_validator import IconValidator
from helpers import copy_theme_to_device, delete_folder_content
from poi_theme import PoiThemeGenerator
from xml_templates.config import TemplateVariables


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
                        default='xml_templates/base.xml')

    parser.add_argument("-rt", "--resultTheme", type=str,
                        help="Path to file to export the generated themes. Set the path for the main map theme." +
                             "The POIs themes are generated in the same location",
                        default='../theme/theme.xml')

    parser.add_argument("-tc", "--templateConfig", type=str,
                        help="Path to file with variables for base template. " +
                             "Cheetah used it to replace the values in base tamplate",
                        default='xml_templates/config.py')

    parser.add_argument("-ac", "--apdbConfig", type=str,
                        help="Path to file with configuration of Offline POI database",
                        default='xml_templates/config_apDb.xml')

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
                     parser_options.copyToDevice,
                     parser_options.publishForAndroid)

    return option


def read_options_yaml(file, option) -> Options:
    option_yaml = yaml.safe_load(open(file))

    option.android_module_path = option_yaml['Options']['android_module_path'],
    option.locus_theme_path = option_yaml['Options']['locus_theme_path'],
    option.output_template = option_yaml['Options']['output_template']

    return option


if __name__ == '__main__':

    # get parameters from CMD (or default ones)
    options = parse_cmd()

    # read default parameters from config yaml
    options = read_options_yaml('options.yaml', options)

    # replace colors, width, etc in source XML
    transform(options.theme_template, options.output_template)

    # generate custom parts (bridges, tourist paths), write results to final XML theme file
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
    poi_theme_generator = PoiThemeGenerator(options.apdb_config_xml, options.result_xml)
    poi_theme_files = poi_theme_generator.generate_render_themes()

    # copy POI themes do device
    for poi_theme_file in poi_theme_files:
        # copy poi theme
        copy_theme_to_device(poi_theme_file)

    # for release
    # copy_theme_to_android_module(options)

    print("=============  DONE  ================= ")
