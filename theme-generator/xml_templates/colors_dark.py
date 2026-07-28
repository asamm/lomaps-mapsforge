from xml_templates.colors_day import ColorsDay

# ==========================================================================
# DARK palette - FIRST DRAFT, auto-generated from colors_day.py using the
# hybrid transform (see _work/dark_theme_study.md):
#   bg->dark blue | water kept-blue+dark | vegetation->teal+dark |
#   roads kept chromatic (desaturated) | routes kept vivid |
#   labels inverted to light | gray ramp flipped.
# Values are a starting point for manual tuning, not final.
# ==========================================================================

class ColorsDark(ColorsDay):

    color_map_background_land       = '#12151c'  # day #EBEADE
    ### LANDUSE - Natural areas
    color_desert_z0                 = '#283824'  # day #F4ECD9
    color_flooded_grassland_z0      = '#1a4231'  # day #C9E5BD
    color_grassland_z0              = '#1a402d'  # day #D4E2B7
    color_ice_z0                    = '#343131'  # day #FDFDFD
    color_mangrove_z0               = '#173433'  # day #8DCCA9
    color_mediter_forest_z0         = '#4b4216'  # day #F2ECCF
    color_montane_grassland_z0      = '#1a402d'  # day #D4E2B7
    color_savannas_z0               = '#454119'  # day #E9E5C2
    color_taiga_z0                  = '#203a33'  # day #C1DBBD
    color_tempr_conifer_forest_z0   = '#203a33'  # day #C1DBBD
    color_tempr_mixed_forest_z0     = '#1e4130'  # day #DBE7CB
    color_trop_conif_forest_z0      = '#1b312b'  # day #9BC595
    color_trop_dry_forest_z0        = '#1c372a'  # day #C6D3A9
    color_trop_moist_forest_z0      = '#1e3433'  # day #A9CDAC
    color_tundra_z0                 = '#3b3826'  # day #DFDED8


    ### HIGHWAYS ###
    color_bridge_casing             = "#2e2e2e"
    color_bridge_no_casing          = "#4d4d4d"
    color_bridge_core               = "#0d0d0d"

    color_motorway_z6               = '#cc8733'  # day #FF8C00
    color_motorway_z7_z11           = '#cc5c33'  # day #FF4500
    color_trunk_z7                  = '#cc8733'  # day #ff8c00
    color_trunk_z8_z11              = '#cc5c33'  # day #FF4500
    color_primary_z7_z11            = '#cc8733'  # day #ff8c00
    color_secondary_z10_z11         = '#b7a13d'  # day #dab614
    color_tertiary_z11              = '#baaeae'  # day #B4B4B4
    color_motorway                  = '#c7c338'  # day #F7F008
    color_trunk                     = '#bcb643'  # day #E5DA1A
    color_primary                   = '#e2c196'  # day #FCC57C
    color_secondary                 = '#ddd376'  # day #ffee54
    color_tertiary                  = '#d2cfa2'  # day #FFFEE6
    color_construction              = '#d4cccc'  # day #d0d0d0
    color_motorway_case             = '#4c2121'  # day #E52C2C
    color_trunk_case                = color_motorway_case
    color_primary_case              = '#422a26'  # day #C6523D
    color_secondary_case            = '#2e2e2e'  # day #707070
    color_tertiary_case             = color_secondary_case
    color_footway_area              = '#131c26'  # day #EDEDED
    color_path_track                = '#767676'  # day #8a8a8a | track / steps / footway
    color_unclassified_case         = '#2e2e2e'
    color_road                      = '#525252'
    color_path                      = '#767676'  # day #747474
    color_pedestrian                = '#2e2e2e'  # day #d0d0d0
    color_parking_area              = "#131c26"
    color_road_core_light           = '#2e2e2e'  # day #ffffff | was #ffffff - generic white text-halo / stroke (300x)

    color_highway_label_primary     = '#206db6'  # day #005fb9
    color_highway_label_motorway    = '#bf3838'  # day #dc1b1b
    color_highway_label_text        = '#ffffff'

    ### RAILWAYS
    color_railway_main_case         = '#a8a8a8'  # day #4d4d4d
    color_railway_line_light        = '#525252'  # day #707070 | railway abandoned/service casing, tunnel, tram
    color_railway_main              = '#767676'  # day #EDEDED


    ### AERIALWAYS
    color_aerialway_core            = '#525252'  # day #4d4d4d
    color_aerialway_zipline         = '#525252'  # day #707070
    color_aerialway_cablecar_fill   = '#767676'  # day #EDEDED
    osmc_colors                     = {
        "red": "#a5290a",   # day #EA3200
        "black": "#a97d7d",   # day #330330
        "blue": "#0b22ad",   # day #021cbc
        "brown": "#955523",   # day #93501B
        "gray": "#6e4a4a",   # day #575757
        "green": "#267106",   # day #267f00
        "orange": "#c2760a",   # day #ff9500
        "purple": "#6231f4",   # day #a78aff
        "yellow": "#ada21f",   # day #e2d21d
        "white": "#a97d7d",   # day #fcfcfc
    }
    color_hiking_iwn_nwn            = '#a5290a'  # day #EA3200


    ### BORDER ###
    color_country_border_low_z      = '#777777'  # day #777777
    color_country_border            = '#907993'  # day #b58cb5

    # CYCLING
    color_cycle_mtb                 = '#981ca3'  # day #E588ED
    color_cycle_standard            = '#6c1470'  # day #d320dc
    color_cycle_icn_ncn             = '#72034f'  # day #A90073
    color_cycle_text_ref            = '#d320dc'  # day #B11BB9
    color_downhill_novice           = '#37c837'  # day #40ff40
    color_downhill_easy             = '#15a8f8'  # day #52c1fe
    color_downhill_intermediate     = '#c93e3e'  # day #ff4a4a
    color_downhill_advanced         = '#753f3f'  # day #242424
    color_downhill_freeride         = '#e3cc0f'  # day #f7e337

    # SKI PISTE
    color_nordic_easy               = '#0564c0'  # day #006BD6
    color_nordic_advanced           = '#660ea5'  # day #590992
    color_piste_hike                = '#2e5f86'  # day #326F9E
    color_piste_skitour             = '#ba8412'  # day #efa710
    color_piste_sled                = '#52a654'  # day #77BF79

    color_downhill_novice_label     = '#86d286'  # day #00e900 | downhill novice caption
    color_downhill_easy_label       = '#80b2cf'  # day #07a6fe | downhill easy caption
    color_downhill_intermediate_lbl = '#c83737'  # day #ff4040 | downhill intermediate caption
    color_piste_lit                 = '#ddd306'  # day #fff41d | lit downhill (via $opacity)

    color_snowmobile                = '#ba6505'  # day #ee7e00 | snowmobile designated  |  was #90ee7e00; apply $opacity(56.7%)

    ## Summer areas
    color_forest_summer_orchard_z13 = '#123222'  # day #a0ca6c | was #80a0ca6c; apply $opacity(50.4%)
    ## Winter areas
    color_forest_winter_z13         = '#19383b'  # day #a4d4d9 | was #80a4d4d9; apply $opacity(50.4%)
    color_park_orchard_winter       = '#1c3b3a'  # day #b3dbcb | was #90b3dbcb; apply $opacity(56.7%)


    ##############
    ## TEXT & SYMBOL PRIORITIES
    color_standard_poi_text         = '#ebebeb'  # day #303030
    color_attraction_poi_text       = '#e5e2e0'  # day #5e5146
    color_label_poi                 = '#d6d6d6'  # day #747474

    ### neutral / grayscale (light -> dark) ###
    color_text_stroke               = '#000000'  # text halo/outline (black for dark theme)
    color_road_halo_lz              = '#131c26'  # low-zoom (z<10) road halo/border, not a true casing
    color_area_fill_light           = '#2f2f2f'  # day #d0d0d0 | merged ultra-light grays (aeroway apron, tertiary CITY, dam, CITY building, construction>16, tram, winter industrial, power, leisure stadium winter, parking/runway/platform)
    color_building_ski_fill         = '#474747'  # day #b8b8b8 | SKI building fill
    color_building_ski_outline      = '#575757'  # day #a8a8a8 | SKI building stroke
    color_place_circle              = '#696969'  # place town/city circle stroke
    color_road_soft                 = '#696969'  # minor-road/path/track/natural line (soft casing)
    color_railway_fill_light        = '#141414'  # day #ededed | was #ededed - railway main fill / footway area / aerialway cablecar (6x)
    color_railway_line              = '#8b8b8b'  # day #747474 | merged medium grays (quarry/natural caption/embankment/tram tunnel, shield bg-rect/abandoned railway, road+railway casing + $opacity wraps)
    color_barrier_circle            = '#9c9c9c'  # day #636363 | merged dark-mid grays (barrier fence/wall/chain, NE city/town circle stroke, railway halt stroke)
    color_label_amenity_dark        = '#c8c8c8'  # day #373737 | merged dark grays (aerialway chair/mixed lift topo, waterway-bridge stroke/runway text/CAR building/hospital+school captions)
    color_road_labels_fill          = '#e0e0e0'  # day #000000 | bridge casing city/car; street-name text; downhill-advanced label

    ### sea / water ###
    color_sea                       = '#1a4a6e'  # day #94c3e6 | sea + NE water/rivers + all standard water fill/stroke + bathymetry depth=0 (28x)
    color_nosea                     = '#12151c'  # day #f7fbfe | natural=nosea
    color_water_label               = '#a8bac8'  # day #4f9cbf | water/marine/glacier labels + marina text + waterfall (20x)
    color_swimming_pool_case        = '#0d3751'  # day #2797dd | swimming_pool stroke

    ### NE bathymetry (shallow -> deep) ###
    color_ne_bathymetry_200         = '#1a486a'  # day #92c1e4 | bathymetry depth=200
    color_ne_bathymetry_1000        = '#1f4765'  # day #88b7da | bathymetry depth=1000
    color_ne_bathymetry_2000        = '#244760'  # day #7babcd | bathymetry depth=2000
    color_ne_bathymetry_3000        = '#28465d'  # day #6f9ec1 | bathymetry depth=3000
    color_ne_bathymetry_4000        = '#294255'  # day #6392b5 | bathymetry depth=4000
    color_ne_bathymetry_5000        = '#273c4c'  # day #5786a9 | bathymetry depth=5000
    color_ne_bathymetry_6000        = '#213746'  # day #4a7a9c | bathymetry depth=6000
    color_ne_bathymetry_7000        = '#1c3241'  # day #3e6e90 | bathymetry depth=7000
    color_ne_bathymetry_8000        = '#162c3b'  # day #326284 | bathymetry depth=8000
    color_ne_bathymetry_9000        = '#112636'  # day #265578 | bathymetry depth=9000
    color_ne_bathymetry_10000       = '#0b2130'  # day #19496b | bathymetry depth=10000
    color_ne_bathymetry_11000       = '#061b2b'  # day #0d3d5f | bathymetry depth=11000

    ### waterway / marina / glacier (ARGB) ###
    color_glacier                   = '#0e457c'  # day #d3e9ff | natural=glacier fill  |  was #50d3e9ff; apply $opacity(31.6%)
    color_marina_case_outer         = '#1a3947'  # day #4f9cbf | marina stroke (outer)  |  was #604f9cbf; apply $opacity(38%)
    color_marina_case_inner         = '#1a3947'  # day #4f9cbf | marina stroke (inner)  |  was #404f9cbf; apply $opacity(25.3%)

    ### contour ###
    color_contour                   = '#51473e'  # day #a07f5f | contour minor/major/medium strokes
    color_contour_label             = '#e6dfd9'  # day #7c583a | contour elevation labels

    ### landuse - residential / industrial / quarry ###
    color_landuse_residential_ne    = '#292727'  # day #c9c9c9 | NE residential + residential_city
    color_landuse_residential       = '#2b2929'  # day #d1d1d1 | residential/retail/industrial (city)
    color_landuse_residential_sum   = '#242f22'  # day #e0d4b3 | SUMMER residential (via $darken) + leisure stadium/sports_centre/water_park case
    color_landuse_residential_sum_t = '#242f22'  # day #e0d4b3 | SUMMER residential translucent  |  was #90e0d4b3; apply $opacity(56.7%)
    color_landuse_residential_win   = '#2f2c2c'  # day #e2e2e2 | WINTER residential
    color_landuse_industrial_sum    = '#26262a'  # day #bfbfcf | SUMMER industrial/brownfield/railway  |  was #90bfbfcf; apply $opacity(56.7%)
    color_landuse_quarry            = '#292a2f'  # day #d6d6e1 | quarry + power areal

    ### natural / landcover ###
    color_forest_summer_scrub       = '#123222'  # day #a0ca6c | scrub/fell SUMMER  |  was #30a0ca6c; apply $opacity(19%)
    color_forest_winter_light       = '#20393f'  # day #cce0e5 | forest/wood WINTER (distinct from color_forest_winter_z13)
    color_beach_sand                = '#283a25'  # day #fcf5e0 | natural=beach / sand
    color_heath                     = '#243d30'  # day #f1f2e9 | natural=heath
    color_scree_shingle             = '#2b2c2f'  # day #dddfe5 | natural=scree/shingle  |  was #80dddfe5; apply $opacity(50.4%)
    color_wetland_tidalflat         = '#1c2518'  # day #8f5011 | wetland=tidalflat  |  was #108f5011; apply $opacity(6.5%)
    color_meadow                    = '#0e2f29'  # day #34972d | meadow/nature_reserve/national_park/botanical (5x)
    color_wood_label                = '#e3efdd'  # day #39761a | wood/park/cemetery captions (7x)
    color_national_park_case        = '#236543'  # day #3fb637 | protected_area/nature_reserve/hedge stroke (

    ### leisure ###
    color_leisure_green_summer      = '#17432d'  # day #dbe5b2 | golf/common/green SUMMER
    color_leisure_playground_sum    = '#14452c'  # day #cdeca7 | playground/pitch/track SUMMER fill (via $darken)
    color_leisure_playground_sum_ln = '#0f3321'  # day #9ccf5e | playground/track SUMMER stroke (via $darken)
    color_leisure_green_winter      = '#233938'  # day #c7dcdb | golf/common/green WINTER
    color_leisure_playground_win    = '#14433b'  # day #a5e4da | playground/track WINTER fill (via $darken)
    color_leisure_playground_win_ln = '#1b2c2b'  # day #8bb7b5 | playground/track WINTER stroke (via $darken)
    color_leisure_stadium_city      = '#242f22'  # day #e1d5b6 | stadium/sports_centre/water_park + camp/caravan/attraction tourism (via $opacity)

    ### cemetery / meadow / vineyard ###
    color_cemetery_fill             = '#19261b'  # day #bdd16c | cemetery/grave_yard/vineyard/orchard fill  |  was #80bdd16c; apply $opacity(50.4%)
    color_cemetery_case             = '#5b5b5b'  # day #e4e4e4 | cemetery/grave_yard stroke
    color_grave_yard_fill           = '#1f2425'  # day #96bfbe | amenity=grave_yard fill  |  was #8096bfbe; apply $opacity(50.4%)

    ### tourism ###
    color_tourism_picnic            = '#203125'  # day #c7f1a3 | tourism=picnic_site
    color_tourism_poi_text          = '#dbd7d4'  # day #826f60 | attraction + amenity captions + waterway=dam label (6x)
    color_zoo_case                  = '#362d26'  # day #6e5036 | zoo topo stroke (via $opacity)
    color_sport_area                = '#232b20'  # day #d6bfa2 | sport=* / aeroway terminal / default building fill

    ### aeroway ###
    color_aerodrome_area            = '#1f3124'  # day #cdeca7 | aeroway=aerodrome translucent  |  was #20cdeca7; apply $opacity(12.7%)

    ### military ###
    color_military_fill             = '#252b1b'  # day #e57a7a | landuse/military airfield fill  |  was #25e57a7a; apply $opacity(14.7%)
    color_military_label            = '#dbd1d0'  # day #925e5a | military label

    ### buildings ###
    color_building_default_case     = '#323438'  # day #c1a074 | building stroke
    color_building                  = '#323438'
    color_building_city_fill        = '#323438'  # day #d9c3c3 | CITY building fill
    color_building_worship_fill     = '#2b303a'  # day #f6c141 | place_of_worship/church/... fill
    color_building_station_fill     = '#2e3135'  # day #b178a6 | train_station/transportation/bus_station fill
    color_building_hospital_fill    = '#2e333e'  # day #ffbfcf | building hospital fill
    color_building_public_fill      = '#323438'  # day #dbd1c7 | kindergarten/school/college/university

    ### HIGHWAYS (by class > core > case > zoom/variant) ###
    # -- motorway & trunk --
    color_trunk_motorway_core       = '#d67977'  # day #f65a57 | trunk/motorway core CAR (10x)
    color_motorway_link_core_hi     = '#e6acab'  # day #fa9997 | motorway_link core >16 + motorway
    color_trunk_motorway_city       = '#cc9245'  # day #f99918 | trunk/motorway CITY
    color_trunk_motorway_city_core  = '#e2ca8a'  # day #ffd86d | trunk/motorway CITY core
    color_indoor_trunk_motorway     = '#e7e09f'  # day #fff387 | trunk/motorway indoor
    color_motorway_toll_case        = '#431a1a'  # day #db100c | motorway toll/link outline
    color_trunk_toll_case           = '#52201f'  # day #f42a27 | trunk toll/link outline
    # -- primary --
    color_primary_core_car          = '#c08e35'  # day #ed9a06 | primary core CAR (5x)
    color_primary_trunk_link_core   = '#ccae59'  # day #f3c032 | primary_link/trunk_link core >16
    color_primary_toll_case         = '#46301b'  # day #e7740c | primary toll/link outline
    color_hw_shield_primary_bg      = '#216db5'  # day #01498e | primary/trunk shield bg-rect-fill
    # -- secondary --
    color_secondary_core_car        = '#b79d3d'  # day #daaf14 | secondary CAR
    color_secondary_primary_city    = '#d5c27f'  # day #f1d263 | secondary/primary CITY
    color_secondary_link_core_hi    = '#decc90'  # day #f8da76 | secondary/secondary_link core >16
    color_secondary_shield          = '#c4ac34'  # day #e3c015 | secondary caption stroke
    color_secondary_link_shield     = '#c4b034'  # day #e3c715 | secondary_link caption stroke
    color_hw_shield_secondary_bg    = '#217fb5'  # day #017dc5 | secondary shield bg-rect-fill
    # -- tertiary --
    color_tertiary_core_hi          = '#eadcb8'  # day #fcecc2 | tertiary/raceway/tertiary_link core >16
    color_tertiary_case_car         = '#463e3b'  # day #b29a91 | tertiary/raceway stroke
    # -- raceway / indoor --
    color_raceway_winter            = '#edd9b6'  # day #fff6e6 | raceway winter/indoor
    color_indoor_primary_secondary  = '#edebb6'  # day #fffedc | primary/secondary indoor
    # -- motorway junction --
    color_motorway_junction_fill    = '#d09a51'  # day #d97f05 | motorway_junction fill
    color_motorway_junction_case    = '#672422'  # day #ff5b58 | motorway_junction stroke

    ### path halos ###

    ### railways ###
    color_railway_station_city      = '#64493f'  # day #cc6c49 | railway=station fill CITY/CAR
    color_railway_station_topo      = '#56564d'  # day #9b9b79 | railway=station fill TOPO
    color_railway_tram_city         = '#65453e'  # day #b8462e | tram CITY stroke
    color_railway_abandoned         = '#525252'  # day #ff707070 | abandoned main highlight
    color_railway_tunnel_subway     = '#723131'  # day #8c0000 | subway tunnel  |  was #408c0000; apply $opacity(25.3%)
    color_railway_tunnel_tram       = '#673c3d'  # day #cf2b2e | tram tunnel
    color_railway_tunnel_tram_topo  = '#3c3c67'  # day #0f0f4c | tram/miniature tunnel topo  |  was #880f0f4c; apply $opacity(53.5%)
    color_railway_tunnel_rail       = '#525252'  # day #4d4d4d | rail/light_rail/etc tunnel  |  was #904d4d4d; apply $opacity(56.7%)
    color_power_tower_label         = '#d8d8d8'  # day #707070 | power=tower label  |  was #90707070; apply $opacity(56.7%)

    ### man_made / barrier ###
    color_man_made_cutline          = '#1d231a'  # day #b38d5d | man_made=cutline
    color_barrier_bollard           = '#181f25'  # day #488bc2 | barrier=bollard z15



    ### place circles ###
    color_town_circle_fill          = '#d1cfbd'  # day #f4f3e9 | town circle fill + landuse=farm captions

    ### PATTERN ICONS (dark = _dark.svg) ###
    pattern_wood_coniferous         = 'patterns/wood_coniferous_transparent_dark.svg'
    pattern_wood_deciduous          = 'patterns/wood_deciduous_transparent_dark.svg'
    pattern_wood_mixed              = 'patterns/wood_mixed_transparent_dark.svg'
    pattern_scrub                   = 'patterns/scrub_dark.svg'
    pattern_glacier                 = 'patterns/glacier_dark.svg'
    pattern_heath                   = 'patterns/heath_dark.svg'
    pattern_medow                   = 'patterns/medow_dark.svg'
    pattern_graveyard               = 'patterns/graveyard_dark.svg'
    pattern_vineyard                = 'patterns/vineyard_dark.svg'
    pattern_orchard                 = 'patterns/orchard_dark.svg'
    pattern_hop_garden              = 'patterns/hop_garden_dark.svg'
    pattern_intermittent_water      = 'patterns/intermittent_water_dark.svg'
    pattern_marsh                   = 'patterns/marsh_dark.svg'
    pattern_tidalflat               = 'patterns/tidalflat_64_dark.svg'
    pattern_bare_rock               = 'patterns/bare_rock_dark.png'  # #3b3835 stipple (same alpha texture as day)
