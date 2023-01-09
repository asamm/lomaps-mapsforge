import os
import pathlib

from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers import XmlSerializer

from poidb.config_apdm import Configuration

class PoiThemeGenerator:

    def __init__(self, config_poi_db_f):

        parser_config = ParserConfig(
            fail_on_unknown_properties=True,
            fail_on_unknown_attributes=False,
        )
        parser = XmlParser(config=parser_config)
        serializer = XmlSerializer()
        poi_config = parser.from_path(pathlib.Path(config_poi_db_f),Configuration)

        print(poi_config)