# Simple operation with colors, thickness etc...

def lighten(color: str, lighten_percent: int):
    """
    Make color lighter for specific percentage
    :type color: color in #RGB or #ARGB hex
    :type lighten_percent: percentage to lighten the color
    :rtype: color in #RGB or #ARGB hex

    """
    if abs(lighten_percent) > 100:
        raise Exception("Invalid percente value for lighten {}. Set value between 0 - 100".format(lighten_percent))

    a = ''
    if len(color) == 9:
        a = color[1:3] # alpha in hex
        color = '#{}'.format(color[3:9])  # remove alpha for further steps

    rgb = hex2rgb(color)
    # do bands lighter
    rgb_lighten = [int(band + (255 - band) * lighten_percent / 100) for band in rgb]
    # make sure new values are between 0 and 255
    rgb_lighten = [min([255, max([0, i])]) for i in rgb_lighten]

    return '#{}'.format(a) + "".join([hex(i)[2:] for i in rgb_lighten])

def darken(color: str, darken_percent: int):
    """
       Make color larker for specific percentage
       :type color: color in #RGB or #ARGB hex
       :type darken_percent: percentage to dark the color
       :rtype: color in #RGB or #ARGB hex

    """
    if abs(darken_percent) > 100:
        raise Exception("Invalid percente value for darken {}. Set value between 0 - 100".format(darken_percent))

    a = ''
    if len(color) == 9:
        a = color[1:3]  # alpha in hex
        color = '#{}'.format(color[3:9])  # remove alpha for further steps

    rgb = hex2rgb(color)
    # do bands darker
    rgb_darker = [int(band * (1 - darken_percent / 100)) for band in rgb]
    # make sure new values are between 0 and 255
    rgb_darker = [min([255, max([0, i])]) for i in rgb_darker]

    return '#{}'.format(a) + '%02x%02x%02x' % tuple(rgb_darker)

def hex2rgb (hex_color):
    # get RGB values in hex
    rgb_hex = [hex_color[x:x + 2] for x in [1, 3, 5]]
    # convert RGB values from hex to int
    return[int(hex_value, 16) for hex_value in rgb_hex]

