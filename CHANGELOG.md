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
