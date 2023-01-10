import os
import pathlib

from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from mapsforge.render_theme import Rule, Rendertheme, Symbol
from poidb.config_apdm import Configuration, SubFolder

default_symbol_width = 20
symbol_directory = 'symbols'


class PoiThemeGenerator:

    def __init__(self, config_poi_db_f, output_theme_f):

        self.config_poi_db_f = config_poi_db_f
        self.output_theme_f = output_theme_f

        # Map apdb config XML into objects
        parser_config = ParserConfig(
            fail_on_unknown_properties=True,
            fail_on_unknown_attributes=False,
        )
        parser = XmlParser(config=parser_config)

        self.poi_config = parser.from_path(pathlib.Path(config_poi_db_f), Configuration)

    def generate_render_theme(self):

        render_theme = self._get_render_theme_header()

        for folder in self.poi_config.pois.folder:
            keys_in_folder = []
            zoom_min = 127
            rule_section = Rule()
            for sub_folder in folder.sub_folder:
                rule = Rule()
                keys_tag = []
                values_tag = []

                for tag in sub_folder.tag:
                    keys_tag.append(tag.key)
                    values_tag.append(tag.value)

                rule.e = "any"
                rule.k = self._join_unique_items_to_rule_string(keys_tag)
                rule.v = self._join_unique_items_to_rule_string(values_tag)
                rule.zoom_min = sub_folder.zoom_min
                rule.symbol.append(self._symbol_for_sub_folder(sub_folder))

                # check minimal zoom for whole folder
                if sub_folder.zoom_min < zoom_min:
                    zoom_min = sub_folder.zoom_min

                # remember what keys were used for sub-folder
                keys_in_folder.extend(keys_tag)
                rule_section.rule.append(rule)

            # set minimal zoom for whole folder section
            rule_section.zoom_min = zoom_min
            # all possible keys that may occurs in section
            rule_section.k = self._join_unique_items_to_rule_string(keys_in_folder)
            rule_section.v = '*'
            rule_section.e = "any"

            # add rule for folder
            render_theme.rule.append(rule_section)

        self.write_result_to_file(render_theme)

    def write_result_to_file(self, render_theme: Rendertheme):

        #  convert back xsdata object
        serializer = XmlSerializer(config=SerializerConfig(
            pretty_print=True,
            xml_declaration=False,
            ignore_default_attributes=True,
            schema_location="http://mapsforge.org/renderTheme https://raw.githubusercontent.com/mapsforge/mapsforge/dev/resources/renderTheme.xsd",
            no_namespace_schema_location=None,
        ))

        with open(self.output_theme_f, 'w') as f:
            serializer.write(f, render_theme)

    def _join_unique_items_to_rule_string(self, keys):
        """
        Join Keys or Values to be possible use them in Rule.k or Rule.v attributes
        :rtype: str
        """
        unique_items = list(dict.fromkeys(keys))  # obtain only unique values from source list
        return '|'.join(unique_items)

    def _symbol_for_sub_folder(self, sub_folder: SubFolder):
        """
        Prepare the symbol object (definition of icon for sub-folder)
        :rtype: Symbol
        """
        symbol: Symbol = Symbol()
        symbol.symbol_width = 20
        symbol.src = 'file:{}/poi_{}.svg'.format(symbol_directory, sub_folder.icon)

        return symbol

    def _get_render_theme_header(self) -> Rendertheme:
        """
        Prepare the root element of mapsforge theme XML. Set also version, background color
        :rtype: Rendertheme
        """
        render_theme = Rendertheme()
        render_theme.version = 4
        render_theme.base_stroke_width = 0.8
        render_theme.map_background = "#ebeade"

        return render_theme
