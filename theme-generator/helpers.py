import fileinput
import os
import shutil
from datetime import datetime
from distutils.dir_util import copy_tree

from xml_templates.config import TemplateVariables


## Set of utils and help method

def transform_cheetah_template(theme_template_xml, cheetah_output_xml):
    """
    Read input template xml with python variables and replace variables by value using cheetah
    :param theme_template_xml: path to xml base theme template
    :param cheetah_output_xml: path to export the input for theme generator
    """
    template = TemplateVariables(file=theme_template_xml)

    f = open(cheetah_output_xml, "w")
    f.write(str(template))
    f.close()


def copy_theme_to_device(result_xml, android_theme_dir):
    """
    Copy specific file to the android device
    :param result_xml: path to generated theme xml
    :param android_theme_dir: android path into theme folder in Locus working directory
    """
    # copy xml theme file to android device
    print('Copy theme {} to the android device'.format(result_xml))

    android_path = os.path.join(android_theme_dir, os.path.basename(result_xml)).replace("\\", "/")

    os.popen("adb push {} {}".format(result_xml, android_path))

    # refresf theme for renderer
    os.popen(
        "adb shell am broadcast -p menion.android.locus -a com.asamm.locus.ACTION_TASK --es tasks '''{ map_reload_theme: {} }'''")

def create_theme_zip_for_publish(result_theme_dir, zip_file):
    """
    Create zip file with generated theme
    :param result_theme_dir: directory with generated theme
    :param zip_file: path to zip file to export
    """
    # remove extension from the path
    if zip_file.endswith('.zip'):
        zip_file = zip_file[:-4]
    shutil.make_archive(zip_file, 'zip', result_theme_dir)

    zip_file = zip_file + '.zip'
    zip_file_size = os.path.getsize(zip_file)
    date = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = os.path.basename(zip_file)

    xml = """<?xml version="1.0" encoding="utf-8"?>
<locusActions>
  <download>
    <source size="{}" date="{}">
      <![CDATA[ https://asamm.github.io/lomaps-mapsforge/lomaps_theme.zip ]]>
    </source>
    <dest><![CDATA[ /mapsVector/_themes/LoMaps_theme.zip ]]></dest>
    <after>refreshMap</after>
  </download>
</locusActions>""".format(zip_file_size, date)

    # write xml to file
    with open(zip_file.replace('.zip', '.xml'), 'w') as f:
        f.write(xml)


def publish_theme_to_android_module(result_theme_dir, android_module_dir):
    """
    Copy generated theme and all required files into specific project folder with android module
    The icons paths in the theme are changed from original `file:` to `assets:`
    Previous data are deleted in #android_module_dir

    :param result_theme_dir: directory with generated theme
    :param android_module_dir: directory of android module to copy the theme
    """

    # remove previous files
    delete_folder_content(android_module_dir)

    # copy new generated theme
    copy_tree(result_theme_dir, android_module_dir)

    # replace path in theme files from 'file:' to 'assets:'
    for filename in os.listdir(android_module_dir):
        if not filename.endswith('.xml'): continue

        filename = os.path.join(android_module_dir, filename)

        with fileinput.FileInput(filename, inplace=True) as file:
            for line in file:
                print(line.replace('file:', 'assets:'), end='')


def delete_folder_content(folder):
    """
    Delete content (files, directories-recursively) of defined folder
    :param folder: folder to delete its content
    """
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete {}. Reason: {}'.format(file_path, e))
