# Locus theme V3 to Mapsforge V4 converter

Locus used for LoMaps vector maps own implementation of render for Mapsforge vector maps.
This implementation was not compatible with the default Mapsforge rendering. 

As of May 2023, LoMaps maps are released as Mapsforge V4 maps.  
Therefore, it is not possible to use the existing "LoMaps V3 Themes" with the new LoMaps V4.

We have prepared a simple script to help transform an existing Locus V3 theme into a Mapsforge V4 
theme. So if you have a theme that contains special Locus attributes, you can use this script
to make it easier to create a theme for LoMaps V4.

Please note that the script does not convert the entire topic 1:1. 
Manual work will still be required, but should save time when editing attributes. 
The script does not copy icons or other resources and they must be copied manually.


### Script can help with the following

- removes unsupported attributes (`render-db-only`, `symbol-color`, `scale-icon-size`)
- comments several unsupported attributes (`scale-font-size`, `scale-dy-size`)
- converts 'dp' units to 'px' units (this transformation was defined based on the internal LoMaps style 
  and for this reason an additional customization will probably be required) 
- convert old attributes to the new ones:
  - `rotate` to `text-orienation`
  - `force-draw` to `display`
  - `align-center` to `position`
  - `upper-case` to `text-transform`

## Installation
- download the repository `git clone https://github.com/asamm/lomaps-mapsforge`
  - `cd lomaps-mapsforge/theme-v3-to-v4-converter`
  - you can also simple download the script https://github.com/asamm/lomaps-mapsforge/blob/main/theme-v3-to-v4-converter/theme_v3_to_v4_converter.py
- install Python 3 https://www.python.org/downloads/
- install python packages
    - ```pip instal -r requirements.txt```

## Usage

`python theme_V3_to_V4.py [-h] [-i INPUT_XML] [-o OUTPUT_XML]`


- `-h` - help
- `-i INPUT_XML` - path to V3 theme xml file (default: `theme_V3.xml`)
- `-o OUTPUT_XML` - path to save the converted V4 theme file (default: `theme_V4.xml`)

## Example

`python theme_V3_to_V4.py -i lomapsV3/theme_V3.xml -o lomapsV4/theme_V4.xml`

