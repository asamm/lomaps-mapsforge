from dataclasses import dataclass, field
from typing import List


@dataclass
class OsmcSymbolDef:
    color: List[str] = field(default_factory=list)
    foreground: List[str] = field(default_factory=list)
    background: List[str] = field(default_factory=list)


class Options():
    def __init__(self,
                 theme_template,
                 apdb_config_xml,
                 template_config,
                 result_xml,
                 generate_osmc_svg,
                 copy_to_device,
                 publish_for_android,
                 android_module_path='',
                 locus_theme_path='',
                 output_template='',
                 osmc_symbol_def=OsmcSymbolDef()):
        self.theme_template = theme_template
        self.apdb_config_xml = apdb_config_xml
        self.template_config = template_config
        self.result_xml = result_xml
        self.android_module_path = android_module_path
        self.locus_theme_path = locus_theme_path

        self.generate_osmc_svg = generate_osmc_svg
        self.copy_to_device = copy_to_device
        self.publish_for_android = publish_for_android
        self.output_template = output_template

        self.osmc_symbol = osmc_symbol_def
