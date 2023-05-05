# Simple script to convert Locus V3 LoMaps theme with custom Locus tags into official Mapsforge V4 theme
import argparse
import os

from bs4 import BeautifulSoup, Comment
from bs4.formatter import XMLFormatter


class SortAttributes(XMLFormatter):
    def attributes(self, tag):
        """Reorder a tag's attributes with specified order."""
        attrib_order = ['cat', 'e', 'k', 'v', 'zoom-min', 'zoom-max']
        new_order = []
        for element in attrib_order:
            if element in tag.attrs:
                new_order.append((element, tag[element]))
        for pair in tag.attrs.items():
            if pair not in new_order:
                new_order.append(pair)
        return new_order


# attributes that can't be replaced and it's needed to completely remove
attr_to_remove = ['render-db-only', 'symbol-color', 'scale-icon-size','sale', 'scale-radius']
attr_to_comment = ['scale-font-size', 'scale-dy-size', 'dx']


def parseOptions():
    """
    Parse command line parameters
    """

    parser = argparse.ArgumentParser(description='''
                        Convert Locus V3 theme with custom Locus tags into official Mapsforge V4 theme ''',
                                     add_help=True)

    parser.add_argument("-i", "--input_xml", type=str,
                        help="Path to LoMaps V3 theme",
                        default="theme.xml")

    parser.add_argument("-o", "--output_xml", type=str,
                        help="Path to save the new V4 theme",
                        default="theme_v4.xml")

    options = parser.parse_args()
    return options





def transform(input_f, output_f):
    file = open(input_f, "r")
    contents = file.read()
    soup = BeautifulSoup(contents, 'xml')

    # update render theme header
    update_render_theme_header(soup)

    # comment whole tags with highway numbers
    comment_bg_rectangles(soup)

    # completely remove unsupported tags
    remove_unsupported_attributes(soup)

    # remove but also comment what attribute was removed
    comment_attributes(soup, attr_to_comment)

    # replace rotate up
    replace_rotate_up(soup)
    replace_allign_center(soup)
    replace_force_draw(soup)
    replace_uppercase_to_text_transform(soup)
    replace_symbol_scale(soup)


    # recompute dp units to pixels
    process_dp_unit(soup)
    process_dy(soup)

    # symbol_icon_symbols(soup, options.output_xml)

    move_zooms_to_256(soup)

    # convert OSMC from symbol element to lineSymbol
    osmc_symbols_lineSymbol(soup)

    # finally save new XML
    write_to_file(options.output_xml, soup)

    # copy xml theme file to android device
    # os.popen(
    #     "adb push {} /sdcard/Android/data/menion.android.locus/files/Locus/mapsVector/_themes/Voluntary/Voluntary_v4.xml".format(
    #         options.output_xml))

def update_render_theme_header(soup):
    element = soup.find('rendertheme')

    element['version'] = '4'
    del element['locus-extended']
    del element['fill-sea-areas']
    del element['scale-line-dy-by-zoom']


def process_dp_unit(soup):
    """"
    Remove the 'dp' units and re-compute the offset to pixels for following attributes: stroke-width, repeat-gap, r, symbol-width, font-size
    :param soup:
    """
    # simple remove dp for following without any computation
    attr_to_remove_dp = ['stroke-width', 'repeat-gap', 'r']
    for attr in attr_to_remove_dp:
        for tag in soup.select('[{}]'.format(attr)):
            value = tag[attr].replace('dp', '')
            value = float(value) * 0.4
            tag[attr] = value

    # remove dp and round to int because symbol-with
    for tag in soup.select('[symbol-width]'):
        scale_factor = 1.5 if 'dp' in tag['symbol-width']  else 0.5
        value_float = float(tag['symbol-width'].replace('dp', ''))
        tag['symbol-width'] = round(value_float * scale_factor)

    for tag in soup.select('[symbol-height]'):
        scale_factor = 1.5 if 'dp' in tag['symbol-height'] else 0.5
        value_float = float(tag['symbol-height'].replace('dp', ''))
        tag['symbol-height'] = round(value_float * scale_factor)

    # remove dp and resize dp at path-text
    for tag in soup.select('[font-size]'):
        scale_factor = 1.4 if 'dp' in tag['font-size'] else 0.5
        value_float = float(tag['font-size'].replace('dp', ''))
        tag['font-size'] = round(value_float * scale_factor)


def process_dy(soup):
    """
    Remove the 'dp' units and re-compute the offset to pixels for lines, pathText, caption and symbol
    :param soup:
    """
    for tag in soup.select('[dy]'):
        value = tag['dy']
        if tag.name == 'line' or tag.name == 'pathText' or tag.name == 'lineSymbol':
            if 'dp' in value:
                value = float(value.replace('dp', ''))
                value = value / 4.3  #
                tag['dy'] = round(value, 1)

        if tag.name == 'caption':
            tag['dy'] = value.replace('dp', '')

        if tag.name == 'symbol':
            del tag['dy']
            tag['position'] = "above"


# def symbol_icon_symbols(soup, output_xml):
#
#
#     for tag in soup.select('[src]'):
#         if 'symbols' not in tag['src']:
#             continue
#
#         v3_file = os.path.splitext(os.path.basename(tag['src']))[0]
#         v3_icon_name = v3_file.split('_', 2)[2]
#
#         if v3_icon_name not in svg_icons_set:
#             print ("Warning can't find V4 icon for {}".format(v3_file))
#             continue
#
#         # copy icon from svg source
#         source_file = svg_icons_set[v3_icon_name][0]
#         output_dir = os.path.dirname(output_xml)
#         target_file = os.path.join(output_dir, "symbols", svg_icons_set[v3_icon_name][1])
#
#         tag['src'] = "file:symbols/{}".format(svg_icons_set[v3_icon_name][1])
#
#         shutil.copy2(source_file, target_file)

def move_zooms_to_256(soup):
    """
    Because 512 tiles was the LoMaps V3 moved for 1 - 2 zooms levels above
    :param soup:
    """

    for tag in soup.select('[zoom-min]'):
        zoom_min = int(tag['zoom-min'])
        if zoom_min > 8:
            tag['zoom-min'] = zoom_min - 1

    for tag in soup.select('[zoom-max]'):
        zoom_max = int(tag['zoom-max'])
        if zoom_max > 9:
            tag['zoom-max'] = zoom_max - 1


def osmc_symbols_lineSymbol(soup):
    """
    Convert OSMC from symbol element to lineSymbol
    :param soup:
    """
    for tag in soup.select('[src]'):
        if 'osmc/' not in tag['src']:
            continue  # filter only elements with OSM symbols

        lineSymbol = soup.new_tag("lineSymbol")
        lineSymbol['src'] = tag['src']
        lineSymbol['symbol-width'] = 12
        lineSymbol['rotate'] = 'true'
        lineSymbol['display'] = 'always'
        lineSymbol['repeat-gap'] = '100'
        lineSymbol['repeat'] = 'true'

        if 'osmc_background' in tag.parent['k']:
            lineSymbol['priority'] = 30
        if 'osmc_foreground' in tag.parent['k']:
            lineSymbol['priority'] = 35

        tag.insert_before(lineSymbol)
        tag.extract()


def comment_bg_rectangles(soup):
    """
    Add comment before bg-rect-fill to be able to remove it later
    :param soup:
    """
    elements = soup.select('[bg-rect-fill]')
    for element in elements:
        comment = Comment(str(element))
        element.insert_before(comment)
        element.extract()


def replace_rotate_up(soup):
    """
    Replace rotate_up with text-orientation for pathText and symbol-orientation for lineSymbol
    :param soup:
    """
    elements = soup.select('[rotate_up]')
    for element in elements:
        new_value = "left"
        if element['rotate_up'] == "true":
            new_value = "right"

        del element['rotate_up']
        if element.name == 'pathText':
            element['text-orientation'] = new_value
        elif element.name == 'lineSymbol':
            element['symbol-orientation'] = new_value
        else:
            element['rotate'] = "true"

def replace_uppercase_to_text_transform(soup):
    """
    Replace tag upper-case=true to text-transform:uppercase
    :param soup:
    """
    elements = soup.select('[upper-case]')
    for element in elements:
        del element['upper-case']
        element['text-transform'] = "uppercase"

def replace_symbol_scale(soup):
    elements = soup.select('[scale]')
    for element in elements:
        if element.name == 'symbol':
            value_float = float(element['scale'])
            element['symbol-percent'] = round(100 * value_float)
            del element['scale']

def replace_allign_center(soup):
    """
    Replace align-center and set position attribute
    :param soup:
    """
    elements = soup.select('[align-center]')
    for element in elements:
        del element['align-center']
        element['position'] = "center"


def replace_force_draw(soup):
    """
    Replace force-draw with display
    :param soup:
    """
    elements = soup.select('[force-draw]')
    for element in elements:
        del element['force-draw']
        element['display'] = "always"

def comment_attributes(soup, attributes_to_comment):
    """
    Remove attributes from soup and comment them
    :param soup:
    :param attributes_to_comment: attributes to comment
    """
    for attr_name in attributes_to_comment:
        elements = soup.select('[{}]'.format(attr_name))

        for element in elements:
            comment = Comment('#TODO removed attribute: {}="{}"'.format(attr_name, element[attr_name]))
            element.insert_before(comment)
            del element[attr_name]

def remove_unsupported_attributes(soup):
    """
    Completely delete unsupported tags
    :param soup:
    """
    for attr in attr_to_remove:
        elements = soup.select('[{}]'.format(attr))
        for element in elements:
            del element[attr]


def write_to_file(output_f, soup):
    """
    Save result into XML file
    :param output_f:
    """
    formatter = SortAttributes(indent="\t")
    f = open(output_f, "w")
    f.write(soup.prettify(formatter=formatter).replace("&", "&amp;"))
    f.close()


if __name__ == '__main__':
    options = parseOptions()

    transform(options.input_xml, options.output_xml)

    print("=============  DONE  ================= ")
