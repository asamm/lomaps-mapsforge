from Cheetah.Template import Template

from xml_templates.config_common import CommonConfig
from xml_templates.colors_day import ColorsDay
from xml_templates.colors_night import ColorsNight


# Cheetah seeds a template's namespace from the instantiated class's OWN __dict__
# (inherited attributes are not collected). So we cannot simply subclass the color /
# common mixins - their attributes would be invisible to the renderer. Instead we
# flatten every attribute (colors + common settings) directly onto the generated
# Template subclass so both the Cheetah render and direct `TemplateVariables.x`
# access (used by actions/generator.py) keep working.
def _collect(cls):
    ns = {}
    for klass in reversed(cls.__mro__):          # base-first so overrides win
        for k, v in vars(klass).items():
            if not k.startswith('__'):
                ns[k] = v
    return ns


def _compose(name, colors_cls, common_cls):
    ns = {}
    ns.update(_collect(common_cls))
    ns.update(_collect(colors_cls))              # colors win on any name clash
    return type(name, (Template,), ns)


ThemeVariablesDay = _compose('ThemeVariablesDay', ColorsDay, CommonConfig)
ThemeVariablesNight = _compose('ThemeVariablesNight', ColorsNight, CommonConfig)

# Backward-compatible default (day). Existing `from xml_templates.config import
# TemplateVariables` keeps working and resolves to the day color set.
TemplateVariables = ThemeVariablesDay

MODES = {
    'day': ThemeVariablesDay,
    'night': ThemeVariablesNight,
}
