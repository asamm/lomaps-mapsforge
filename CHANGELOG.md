## [1.5.2] - 2024-06-03

### Added
- [tag-mapping] - add `tourism=theme_park`

### Changed
- changing the color of the water feature and the thickness of rivers, canals and streams to 
  make them more visible.
- remove the Foot & Drink category as it cannot affect the points of interest in the new V4 styles.

## [1.5.1] - 2024-06-03

### Changed
- parking as a light-gray area

## [1.5.0] - 2024-05-06

### Added
- new offline POIs (shipwrecks, bridges, aqueduct, bicycle repair station)
- add support for pump-tracks

### Changed
- unify style of country and state borders with online style

### Fixed
- add missing `building=sport`
- extend a list of osmc_foreground for straight green osmc line to fix a problem when green route may not be visible because not known osmc_foreground
- missing `leisure=track` when mapped as multipolygon

## [1.4.2] - 2024-01-23

### Added
- add minor power lines and customize the power tower/poles
- [tag-mapping] - add bicycle parking
## [1.4.1] - 2023-12-21

### Changed
- [tag-mapping] - mainly changes in zoom-levels for rendering of some elements in OS Map theme

## [1.4.0] - 2023-11-01

### Added
- borderline in `admin_level = 3` because Cyprus
- power poles

### Changed
- rendering white marked trails as red with a red outline
- marked trails along ferry routes are rendered as dashed lines
- [tag-mapping] - add special combination  `highway=ferry`

### Fixed
- missing MTB routes


## [1.3.3] - 2023-09-26

### Changed
-  improve visibility of national borders in day and also night mode https://help.locusmap.eu/agent/object/31979

## [1.3.2] - 2023-09-26

### Added
- mountain ridge (natural=arete)
- icon for ford

## [1.3.1] - 2023-09-14

### Added
- assisted trails are marked with red chain symbols
- render power poles
- [tag-mapping] - add power=minor_line

### Changed
- osmc blue color is a bit darker

## [1.3.0] - 2023-09-08

### Added
- add purple color to be supported as OSMC color
- railway miniature, monorail in tag mapping
- background color for tidal-flats
- overground pipelines, goods_conveyor
- bridges for paths, footways have inner color
- add road numbers (BETA)
- display areas for archaeological sites, fitness
- breakwaters, groynes
- borders and captions of zoo areas
- monorail railways
- name of trailheads
- zip lines
- [tag-mapping] - add railway miniature, monorail in tag mapping
- [tag-mapping] - add natural=mud

### Changed
- lift gate in same symbol as online LoMaps (smaller size and more decent)
- add cycling routes into zl 9 - 12 
- make highways wider to be more similar to online maps
- better SAC scales for osmc routes
- via ferrata with difficulty
- case line of highways is no more visible inside of parking areas
- [tag-mapping] -  cycling routes ICN & NCN available from zl=8 and RCN available from zl=10
- [tag-mapping] -  better support of difficulty level of via ferrata
- [tag-mapping] -  merge alternative type of bridges into 'bridge=yes' value

### Fixed
- incorrect position for piers (were above roads)

## [1.2.3] - 2023-08-02

### Added
- wind turbines 
- [tag-mapping] - add man_made breakwater and groyne, underground location
- [tag-mapping] - add zoo types (aviary, birds, reptile, safari_park, etc...)
- [tag-mapping] - add highway=trailhead
- [tag-mapping] - add leisure=fitness_centre, natural=arete

### Changed
- dams in lighter gray color, add captions for dams
- gates for zl=15 - 16 in smaller size
- improve rendering of pedestrian areas (avoid thick stroke line)
- [tag-mapping] - forest areas available from ZL 9

### Fixed
- MTB cycle ways were rendered for every bicycle=yes

## [1.2.2] - 2023-05-23

### Added
- [tag-mapping] add elements to display ford and pipelines, and service types

### Changed
- osmc symbol visible from ZL 15
- attraction areas semitransparent to avoid problems with incorrect layer definition in OSM
- increase width of contours lines to be more visible

## [1.2.1] - 2023-05-15

### Added
- observation towers to POI DB

### Changed
- change order of iwn,rwn and osmc routes with defined main color (hiking route without defined) 
  OSMC color has lower priority
- change priority of the osmc symbol vs name of route

## [1.2.0] - 2023-05-05

### Added
- script that helps to convert Locus V3 theme to Mapsforge V4 theme
- display oneway symbol for pedestrians/hikers
- display name for `place=islet`
- tag-mapping file supports: `place=islet`, `oneway:foot`, `foot:backward` for pedestrians/hikers, 

### Fixed
- improve dashed lines (to be more visible) for routes with defined `sac_scale`


## [1.1.4] - 2023-04-24

### Added
- support for new symbols defined in `osmc:symbol`
- osmc hiking routes may be rendered as dashed lines when `sac_scale` is defined

### Changed
- all network types IWN, NWN, RWN, LWN are rendered as red
- forest are rendered transparent in ZL 9 - 13 (to avoid rendering of forest on top of tunnels)
- change width of `aerialways` to be more visible

### Fixed
- fix incorrect rendering of hiking routes when sac_scale in hiking routes


## [1.1.3] - 2023-04-06

### Added

- display tidal areas with mud or sand

### Changed
- improve offset for MTB routes (avoid hidden route by highway)
- tag-mapping file supports new tags especially for OS theme (surface, residential areas, special 
  buildings) 
- from tag-mapping file were removed unused tag (`wheelchair=*`, `oneway=no`, `horse=*`) 

### Fixed
- display missing IWN, NWN, RWN, LWN hiking routes


## [1.1.2] - 2023-03-10

### Added

- missing minimal and target API for Android module

## [1.1.1] - 2023-03-09

### Changed

- prepare workaround to remove blue (sea) tiles when default theme loaded for OpenAndroMaps

## [1.1.0] - 2023-02-28

### Added

- a symbol allowing cyclists to enter a one-way streets (Hike&Bike)
- symbol for one way nordic pistes (Ski)
- lit for nordic and downhill pistes (Ski)
- intermittent reservoirs
- and many more

### Changed

- lots of changes related to new MF V4 styling, unify theme with online LoMaps

## [1.0.0] - 2023-02-16

- Initial beta release
