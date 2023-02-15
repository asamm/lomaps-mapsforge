import copy
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

    def __init__(self, config_poi_db_f, map_theme_f):
        """

        :param config_poi_db_f: configuration file that is used for generation of POI DB
        :param map_theme_f: path to location of map theme
        """
        self.config_poi_db_f = config_poi_db_f
        self.map_theme_f = map_theme_f

        self.cat_4_folder = {}
        # Map apdb config XML into objects
        parser_config = ParserConfig(
            fail_on_unknown_properties=True,
            fail_on_unknown_attributes=False,
        )
        parser = XmlParser(config=parser_config)

        self.poi_config = parser.from_path(pathlib.Path(config_poi_db_f), Configuration)

    def generate_render_themes(self):
        """
        For every theme (defined in POI DB configuration XML) creates a custom render theme. Every layer (hike_bike, ski)
        has separated theme file with icon definition
        """
        render_theme = self._get_render_theme_header()

        for folder in self.poi_config.pois.folder:
            keys_in_folder = []
            zoom_min = 127

            rule_folder = Rule(e = "any", v = '*', cat = folder.name)

            if folder.theme is None:
                print('WARNING - theme is not defined for folder: {}'.format(folder) )


            for sub_folder in folder.sub_folder:

                keys_tag = []
                values_tag = []

                # inherit zoom-min from parent folder
                if sub_folder.zoom_min is None or sub_folder.zoom_min == 127:
                    if folder.zoom_min is not None or folder.zoom_min != 127:
                        # inherit zoom from higher level (if not defined in subfolder)
                        sub_folder.zoom_min = folder.zoom_min

                # inherit name folder(is used as tag id) from parent
                if sub_folder.theme is None and folder.theme is not None:
                    sub_folder.theme = folder.theme

                for tag in sub_folder.tag:
                    keys_tag.append(tag.key)
                    values_tag.append(tag.value)

                rule_subs_folder = Rule(e = "any",
                            k = self._join_unique_items_to_rule_string(keys_tag),
                            v = self._join_unique_items_to_rule_string(values_tag),
                            cat = sub_folder.name,
                            zoom_min = sub_folder.zoom_min)
                rule_subs_folder.symbol.append(self._symbol_for_sub_folder(sub_folder))

                # check minimal zoom for whole folder
                if sub_folder.zoom_min < zoom_min:
                    zoom_min = sub_folder.zoom_min

                # remember what keys were used for sub-folder
                keys_in_folder.extend(keys_tag)
                rule_folder.rule.append(rule_subs_folder)

                if sub_folder.theme:
                    # remember theme value if theme is defined for this folder or subfolder
                    self.cat_4_folder[sub_folder.name] = sub_folder.theme

            # set minimal zoom for whole folder section
            rule_folder.zoom_min = zoom_min
            # all possible keys that may occurs in section
            rule_folder.k = self._join_unique_items_to_rule_string(keys_in_folder)

            if folder.theme:
                # remember theme value if theme is defined for this folder or subfolder
                self.cat_4_folder[folder.name] = folder.theme

            # add rule for folder
            render_theme.rule.append(rule_folder)

        # for every layer (theme) create custom render_theme to respect the visibility of icon for specific theme
        themes = self._organize_rules_for_themes(render_theme)

        return self._save_themes_to_files(themes)


    def _organize_rules_for_themes(self, render_theme: Rendertheme):
        """
        For every theme (layer) creates separated render_theme with specific rules only for such theme (layer)
        :param render_theme render theme for all layer (themes)
        :rtype: dict with structure {theme_id | render_theme}
        """
        theme_ids = self._get_possible_theme_ids()  # list of available themes

        themes_for_ids = {}

        for theme_id in theme_ids:
            render_theme_copy = copy.deepcopy(render_theme)
            self._remove_non_theme_rules(render_theme_copy.rule, theme_id)

            themes_for_ids[theme_id] = render_theme_copy

        return themes_for_ids

    def _remove_non_theme_rules(self, rules, theme_id):
        """
        From source theme remove rules that do not fit the theme
        :param rules: render theme rules to remove if doesn't fit to required theme
        :param theme_id: id of theme
        """
        for i in range(len(rules) - 1, -1, -1):
            rule = rules[i]
            if not self._is_rule_available_for_theme(rule, theme_id):
                del rules[i]
                continue
            if len(rule.rule) > 0:
                self._remove_non_theme_rules(rule.rule, theme_id)

    def _is_rule_available_for_theme(self, rule, theme_id):
        """
        Check if category of the rule can be used in specific theme
        :param rule: rule to check
        :param theme_id:
        :return: True if rule can be used in specific theme
        """
        themes_for_folder = self.cat_4_folder.get(rule.cat)
        if themes_for_folder is None:
            print('WARNING can not find theme for folder with name: {}'.format(rule.cat) )
            return True

        return theme_id in themes_for_folder
    def _get_possible_theme_ids(self):
        """

        :rtype: list[str] list of theme ids used in POI definition XML
        """
        # get list of 'theme' values used in config xml
        theme_values = list(self.cat_4_folder.values())

        # split values by comma in list of strings (theme values
        theme_values = [word for value in theme_values for word in value.split(',')]

        theme_ids = []
        for word in theme_values:
            if word not in theme_ids:
                theme_ids.append(word)

        return theme_ids

    def _save_themes_to_files(self, themes):
        """
        Export render themes to separated XML files
        :param themes: render themes to save into files
        """
        poi_theme_files = []
        for theme_id, render_theme in themes.items():
            filename_part = pathlib.Path(self.map_theme_f).stem
            filename_suffix = pathlib.Path(self.map_theme_f).suffix

            file = os.path.join(os.path.dirname(self.map_theme_f), '{}_{}.poi{}'.format(filename_part,theme_id,filename_suffix))
            self.write_result_to_file(file, render_theme)
            poi_theme_files.append(file)

        return poi_theme_files

    def write_result_to_file(self, file, render_theme: Rendertheme):

        #  convert back xsdata object
        serializer = XmlSerializer(config=SerializerConfig(
            pretty_print=True,
            xml_declaration=False,
            ignore_default_attributes=True,
            schema_location="http://mapsforge.org/renderTheme https://raw.githubusercontent.com/mapsforge/mapsforge/dev/resources/renderTheme.xsd",
            no_namespace_schema_location=None,
        ))

        with open(file, 'w') as f:
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


