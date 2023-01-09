from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Filter:
    class Meta:
        name = "filter"

    key: Optional[str] = field(
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
class Tag:
    class Meta:
        name = "tag"

    key: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "filter",
                    "type": Filter,
                },
            ),
        }
    )


@dataclass
class PoiDetails:
    """
    :ivar tag: name a company for hotel, restaurant, shop ...  hotel
        classification  Is human readable title of the article, eg:
        wikipedia=en:St Paul's Cathedral
    """
    class Meta:
        name = "poi-details"

    tag: List[Tag] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class PoiEmail:
    class Meta:
        name = "poi-email"

    tag: List[Tag] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class PoiPhone:
    class Meta:
        name = "poi-phone"

    tag: List[Tag] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class PoiUrl:
    """
    :ivar tag: OSM suggest to use web site but URL key is also possible
    """
    class Meta:
        name = "poi-url"

    tag: List[Tag] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class SubFolder:
    class Meta:
        name = "sub-folder"

    tag: List[Tag] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    filter: List[Filter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    zoom_min: Optional[int] = field(
        default=0,
        metadata={
            "name": "zoom-min",
            "type": "Attribute",
        }
    )
    icon: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Folder:
    """
    :ivar sub_folder: &#13; &lt;sub-folder name="telephone" zoom-
        min="17" icon="toilets" &gt;&#13; &lt;tag key="amenity"
        value="telephone" type="poi,way" /&gt; Deleted first revision
        2014-10-24&#13; &lt;/sub-folder&gt;&#13; &#13; &lt;sub-folder
        name="map" zoom-min="15" icon="hiking_cycling" &gt;&#13; &lt;tag
        key="information" value="map" type="poi" /&gt; Deleted first
        revision 2014-10-24&#13; &lt;/sub-folder&gt;&#13;
    :ivar name:
    :ivar zoom_min:
    :ivar icon:
    """
    class Meta:
        name = "folder"

    sub_folder: List[SubFolder] = field(
        default_factory=list,
        metadata={
            "name": "sub-folder",
            "type": "Element",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    zoom_min: Optional[int] = field(
        default=None,
        metadata={
            "name": "zoom-min",
            "type": "Attribute",
        }
    )
    icon: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Params:
    class Meta:
        name = "params"

    poi_details: Optional[PoiDetails] = field(
        default=None,
        metadata={
            "name": "poi-details",
            "type": "Element",
            "required": True,
        }
    )
    poi_email: Optional[PoiEmail] = field(
        default=None,
        metadata={
            "name": "poi-email",
            "type": "Element",
            "required": True,
        }
    )
    poi_phone: Optional[PoiPhone] = field(
        default=None,
        metadata={
            "name": "poi-phone",
            "type": "Element",
            "required": True,
        }
    )
    poi_url: Optional[PoiUrl] = field(
        default=None,
        metadata={
            "name": "poi-url",
            "type": "Element",
            "required": True,
        }
    )


@dataclass
class Pois:
    class Meta:
        name = "pois"

    folder: List[Folder] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Configuration:
    class Meta:
        name = "configuration"

    pois: Optional[Pois] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    params: Optional[Params] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
