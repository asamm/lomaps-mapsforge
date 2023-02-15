from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

__NAMESPACE__ = ""


class Cap(Enum):
    BUTT = "butt"
    ROUND = "round"
    SQUARE = "square"


@dataclass
class Cat:
    class Meta:
        name = "cat"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Circle:
    class Meta:
        name = "circle"

    cat: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    radius: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        }
    )
    scale_radius: bool = field(
        default=False,
        metadata={
            "name": "scale-radius",
            "type": "Attribute",
        }
    )
    fill: str = field(
        default="#00000000",
        metadata={
            "type": "Attribute",
            "pattern": r"#([0-9a-fA-F]{6}|[0-9a-fA-F]{8})",
        }
    )
    stroke: str = field(
        default="#00000000",
        metadata={
            "type": "Attribute",
            "pattern": r"#([0-9a-fA-F]{6}|[0-9a-fA-F]{8})",
        }
    )
    stroke_width: float = field(
        default=0.0,
        metadata={
            "name": "stroke-width",
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )


class Closed(Enum):
    YES = "yes"
    NO = "no"
    ANY = "any"


class Display(Enum):
    ALWAYS = "always"
    NEVER = "never"
    IFSPACE = "ifspace"


class ElementList(Enum):
    NODE = "node"
    WAY = "way"
    ANY = "any"


class FontFamily(Enum):
    DEFAULT = "default"
    MONOSPACE = "monospace"
    SANS_SERIF = "sans_serif"
    SERIF = "serif"


class FontStyle(Enum):
    BOLD = "bold"
    BOLD_ITALIC = "bold_italic"
    ITALIC = "italic"
    NORMAL = "normal"


@dataclass
class HillShading:
    """
    :ivar cat:
    :ivar zoom_min:
    :ivar zoom_max:
    :ivar magnitude:
    :ivar always: Apply neutral shading when tiles are missing or
        shading is disabled to keep colors consistent (for themes that
        compensate color intensity for hillshading desaturation)
    :ivar layer:
    """
    class Meta:
        name = "hillShading"

    cat: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    zoom_min: int = field(
        default=5,
        metadata={
            "name": "zoom-min",
            "type": "Attribute",
        }
    )
    zoom_max: int = field(
        default=17,
        metadata={
            "name": "zoom-max",
            "type": "Attribute",
        }
    )
    magnitude: int = field(
        default=64,
        metadata={
            "type": "Attribute",
        }
    )
    always: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    layer: int = field(
        default=5,
        metadata={
            "type": "Attribute",
        }
    )


class Linejoin(Enum):
    MITER = "miter"
    ROUND = "round"
    BEVEL = "bevel"


@dataclass
class Name:
    class Meta:
        name = "name"

    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Overlay:
    class Meta:
        name = "overlay"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class Position(Enum):
    AUTO = "auto"
    CENTER = "center"
    BELOW = "below"
    BELOW_LEFT = "below_left"
    BELOW_RIGHT = "below_right"
    ABOVE = "above"
    ABOVE_LEFT = "above_left"
    ABOVE_RIGHT = "above_right"
    LEFT = "left"
    RIGHT = "right"


class Scale(Enum):
    ALL = "all"
    NONE = "none"
    STROKE = "stroke"


class TextKey(Enum):
    ELE = "ele"
    ADDR_HOUSENUMBER = "addr:housenumber"
    NAME = "name"
    REF = "ref"


@dataclass
class Area:
    class Meta:
        name = "area"

    cat: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    src: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"((jar|file|assets):)?.+",
        }
    )
    symbol_width: Optional[int] = field(
        default=None,
        metadata={
            "name": "symbol-width",
            "type": "Attribute",
        }
    )
    symbol_height: Optional[int] = field(
        default=None,
        metadata={
            "name": "symbol-height",
            "type": "Attribute",
        }
    )
    symbol_percent: Optional[int] = field(
        default=None,
        metadata={
            "name": "symbol-percent",
            "type": "Attribute",
        }
    )
    fill: str = field(
        default="#000000",
        metadata={
            "type": "Attribute",
            "pattern": r"#([0-9a-fA-F]{6}|[0-9a-fA-F]{8})",
        }
    )
    scale: Scale = field(
        default=Scale.STROKE,
        metadata={
            "type": "Attribute",
        }
    )
    stroke: str = field(
        default="#00000000",
        metadata={
            "type": "Attribute",
            "pattern": r"#([0-9a-fA-F]{6}|[0-9a-fA-F]{8})",
        }
    )
    stroke_width: float = field(
        default=0.0,
        metadata={
            "name": "stroke-width",
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )


@dataclass
class Caption:
    class Meta:
        name = "caption"

    cat: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    priority: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    k: Optional[TextKey] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    display: Display = field(
        default=Display.IFSPACE,
        metadata={
            "type": "Attribute",
        }
    )
    dy: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
        }
    )
    font_family: FontFamily = field(
        default=FontFamily.DEFAULT,
        metadata={
            "name": "font-family",
            "type": "Attribute",
        }
    )
    font_style: FontStyle = field(
        default=FontStyle.NORMAL,
        metadata={
            "name": "font-style",
            "type": "Attribute",
        }
    )
    font_size: float = field(
        default=0.0,
        metadata={
            "name": "font-size",
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    fill: str = field(
        default="#000000",
        metadata={
            "type": "Attribute",
            "pattern": r"#([0-9a-fA-F]{6}|[0-9a-fA-F]{8})",
        }
    )
    stroke: str = field(
        default="#000000",
        metadata={
            "type": "Attribute",
            "pattern": r"#([0-9a-fA-F]{6}|[0-9a-fA-F]{8})",
        }
    )
    stroke_width: float = field(
        default=0.0,
        metadata={
            "name": "stroke-width",
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    position: Position = field(
        default=Position.AUTO,
        metadata={
            "type": "Attribute",
        }
    )
    symbol_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "symbol-id",
            "type": "Attribute",
        }
    )


@dataclass
class Layer:
    class Meta:
        name = "layer"

    name: List[Name] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    cat: List[Cat] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    overlay: List[Overlay] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    parent: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    visible: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    enabled: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Line:
    class Meta:
        name = "line"

    cat: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    src: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"((jar|file|assets):)?.+",
        }
    )
    symbol_width: Optional[int] = field(
        default=None,
        metadata={
            "name": "symbol-width",
            "type": "Attribute",
        }
    )
    symbol_height: Optional[int] = field(
        default=None,
        metadata={
            "name": "symbol-height",
            "type": "Attribute",
        }
    )
    symbol_percent: Optional[int] = field(
        default=None,
        metadata={
            "name": "symbol-percent",
            "type": "Attribute",
        }
    )
    dy: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
        }
    )
    scale: Scale = field(
        default=Scale.STROKE,
        metadata={
            "type": "Attribute",
        }
    )
    stroke: str = field(
        default="#000000",
        metadata={
            "type": "Attribute",
            "pattern": r"#([0-9a-fA-F]{6}|[0-9a-fA-F]{8})",
        }
    )
    stroke_width: float = field(
        default=0.0,
        metadata={
            "name": "stroke-width",
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    stroke_dasharray: Optional[str] = field(
        default=None,
        metadata={
            "name": "stroke-dasharray",
            "type": "Attribute",
            "pattern": r"([0-9]+(\.[0-9]+)? *, *[0-9]+(\.[0-9]+)? *, *)*[0-9]+(\.[0-9]+)? *, *[0-9]+(\.[0-9]+)?",
        }
    )
    stroke_linecap: Cap = field(
        default=Cap.ROUND,
        metadata={
            "name": "stroke-linecap",
            "type": "Attribute",
        }
    )
    stroke_linejoin: Linejoin = field(
        default=Linejoin.ROUND,
        metadata={
            "name": "stroke-linejoin",
            "type": "Attribute",
        }
    )


@dataclass
class LineSymbol:
    class Meta:
        name = "lineSymbol"

    cat: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    display: Display = field(
        default=Display.IFSPACE,
        metadata={
            "type": "Attribute",
        }
    )
    dy: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
        }
    )
    scale: Scale = field(
        default=Scale.STROKE,
        metadata={
            "type": "Attribute",
        }
    )
    src: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"((jar|file|assets):)?.+",
        }
    )
    symbol_width: Optional[int] = field(
        default=None,
        metadata={
            "name": "symbol-width",
            "type": "Attribute",
        }
    )
    symbol_height: Optional[int] = field(
        default=None,
        metadata={
            "name": "symbol-height",
            "type": "Attribute",
        }
    )
    symbol_percent: Optional[int] = field(
        default=None,
        metadata={
            "name": "symbol-percent",
            "type": "Attribute",
        }
    )
    position: Position = field(
        default=Position.BELOW_RIGHT,
        metadata={
            "type": "Attribute",
        }
    )
    priority: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    repeat: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    repeat_gap: float = field(
        default=200.0,
        metadata={
            "name": "repeat-gap",
            "type": "Attribute",
        }
    )
    repeat_start: float = field(
        default=30.0,
        metadata={
            "name": "repeat-start",
            "type": "Attribute",
        }
    )
    rotate: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class PathText:
    class Meta:
        name = "pathText"

    cat: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    display: Display = field(
        default=Display.IFSPACE,
        metadata={
            "type": "Attribute",
        }
    )
    k: Optional[TextKey] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    dy: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
        }
    )
    font_family: FontFamily = field(
        default=FontFamily.DEFAULT,
        metadata={
            "name": "font-family",
            "type": "Attribute",
        }
    )
    font_style: FontStyle = field(
        default=FontStyle.NORMAL,
        metadata={
            "name": "font-style",
            "type": "Attribute",
        }
    )
    font_size: float = field(
        default=0.0,
        metadata={
            "name": "font-size",
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    fill: str = field(
        default="#000000",
        metadata={
            "type": "Attribute",
            "pattern": r"#([0-9a-fA-F]{6}|[0-9a-fA-F]{8})",
        }
    )
    priority: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    scale: Scale = field(
        default=Scale.STROKE,
        metadata={
            "type": "Attribute",
        }
    )
    stroke: str = field(
        default="#000000",
        metadata={
            "type": "Attribute",
            "pattern": r"#([0-9a-fA-F]{6}|[0-9a-fA-F]{8})",
        }
    )
    stroke_width: float = field(
        default=0.0,
        metadata={
            "name": "stroke-width",
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    repeat: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )
    repeat_gap: float = field(
        default=100.0,
        metadata={
            "name": "repeat-gap",
            "type": "Attribute",
        }
    )
    repeat_start: float = field(
        default=10.0,
        metadata={
            "name": "repeat-start",
            "type": "Attribute",
        }
    )
    rotate: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Symbol:
    class Meta:
        name = "symbol"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    cat: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    display: Display = field(
        default=Display.IFSPACE,
        metadata={
            "type": "Attribute",
        }
    )
    priority: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    src: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"((jar|file|assets):)?.+",
        }
    )
    symbol_width: Optional[int] = field(
        default=None,
        metadata={
            "name": "symbol-width",
            "type": "Attribute",
        }
    )
    symbol_height: Optional[int] = field(
        default=None,
        metadata={
            "name": "symbol-height",
            "type": "Attribute",
        }
    )
    symbol_percent: Optional[int] = field(
        default=None,
        metadata={
            "name": "symbol-percent",
            "type": "Attribute",
        }
    )
    position: Position = field(
        default=Position.CENTER,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class   Rule:
    class Meta:
        name = "rule"

    rule: List["Rule"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    area: List[Area] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    caption: List[Caption] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    circle: List[Circle] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    line: List[Line] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    line_symbol: List[LineSymbol] = field(
        default_factory=list,
        metadata={
            "name": "lineSymbol",
            "type": "Element",
        }
    )
    path_text: List[PathText] = field(
        default_factory=list,
        metadata={
            "name": "pathText",
            "type": "Element",
        }
    )
    symbol: List[Symbol] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    e: Optional[ElementList] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    k: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    v: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    cat: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    closed: Closed = field(
        default=Closed.ANY,
        metadata={
            "type": "Attribute",
        }
    )
    zoom_min: int = field(
        default=0,
        metadata={
            "name": "zoom-min",
            "type": "Attribute",
        }
    )
    zoom_max: int = field(
        default=127,
        metadata={
            "name": "zoom-max",
            "type": "Attribute",
        }
    )


@dataclass
class Stylemenu:
    class Meta:
        name = "stylemenu"

    layer: List[Layer] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    defaultvalue: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    defaultlang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class Rendertheme:
    class Meta:
        name = "rendertheme"

    stylemenu: Optional[Stylemenu] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    rule: List[Rule] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    hillshading: List[HillShading] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "sequential": True,
        }
    )
    version: int = field(
        init=False,
        default=5,
        metadata={
            "type": "Attribute",
        }
    )
    map_background: str = field(
        default="#ffffff",
        metadata={
            "name": "map-background",
            "type": "Attribute",
            "pattern": r"#([0-9a-fA-F]{6}|[0-9a-fA-F]{8})",
        }
    )
    map_background_outside: str = field(
        default="#ffffff",
        metadata={
            "name": "map-background-outside",
            "type": "Attribute",
            "pattern": r"#([0-9a-fA-F]{6}|[0-9a-fA-F]{8})",
        }
    )
    base_stroke_width: float = field(
        default=1.0,
        metadata={
            "name": "base-stroke-width",
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
    base_text_size: float = field(
        default=1.0,
        metadata={
            "name": "base-text-size",
            "type": "Attribute",
            "min_inclusive": 0.0,
        }
    )
