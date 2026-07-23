
class ColorsDay:
    color_map_background_land       = "#EBEADE"
    ### LANDUSE - Natural areas
    color_desert_z0                 = '#F4ECD9'
    color_flooded_grassland_z0      = '#C9E5BD'
    color_grassland_z0              = '#D4E2B7'
    color_ice_z0                    = '#FDFDFD'
    color_mangrove_z0               = '#8DCCA9'
    color_mediter_forest_z0         = '#F2ECCF'
    color_montane_grassland_z0      = '#D4E2B7'
    color_savannas_z0               = '#E9E5C2'
    color_taiga_z0                  = '#C1DBBD'
    color_tempr_conifer_forest_z0   = '#C1DBBD'
    color_tempr_mixed_forest_z0     = '#DBE7CB'
    color_trop_conif_forest_z0      = '#9BC595'
    color_trop_dry_forest_z0        = '#C6D3A9'
    color_trop_moist_forest_z0      = '#A9CDAC'
    color_tundra_z0                 = '#DFDED8'


    ### HIGHWAYS ###
    color_bridge_casing             = "#0d0d0d"
    color_bridge_no_casing          = "#4d4d4d"
    color_motorway_z6               = "#FF8C00"
    color_motorway_z7               = "#FF4500"
    color_motorway_z8_z11           = "#FF4500"
    color_trunk_z7                  = "#ff8c00"
    color_trunk_z8_z11              = "#FF4500"
    color_primary_z7_z11            = "#ff8c00"
    color_secondary_z10_z11         = "#dab614"
    color_tertiary_z11              = "#B4B4B4"
    color_highway_lowzoom_case      = '#FFFFFF'
    color_motorway                  = "#F7F008"
    color_trunk                     = "#E5DA1A"
    color_primary                   = "#FCC57C"
    color_secondary                 = "#ffee54"
    color_tertiary                  = "#FFFEE6"
    color_unclassified              = "#ffffff"
    color_construction              = "#d0d0d0"
    color_motorway_case             = "#E52C2C"
    color_trunk_case                = "#E52C2C"
    color_primary_case              = "#C6523D"
    color_secondary_case            = "#707070"
    color_tertiary_case             = "#707070"
    color_unclassified_case         = "#8a8a8a"
    color_footway_area              = "#EDEDED"
    color_track                     = "#8a8a8a"
    color_steps                     = "#8a8a8a"
    color_footway                   = "#8a8a8a"
    color_path                      = "#747474"
    color_path_case                 = "#FFFFFF"
    color_pedestrian                = "#d0d0d0"
    color_highway_label_primary     = "#005fb9"
    color_highway_label_motorway    = "#dc1b1b"

    ### RAILWAYS
    color_railway_main_case         = '#4d4d4d'
    color_railway_abandoned_case    = '#707070'
    color_railway_service_case      = '#707070'
    color_railway_tunnel            = '#707070'
    color_railway_tram              = '#707070'
    color_railway_main              = '#EDEDED'


    ### AERIALWAYS
    color_aerialway_core            = "#4d4d4d"
    color_aerialway_zipline         = "#707070"
    color_aerialway_cablecar_fill   = "#EDEDED"
    osmc_colors                     = {
        "red": "#EA3200",
        "black": "#330330",
        "blue": "#021cbc",
        "brown": "#93501B",
        "gray": "#575757",
        "green": "#267f00",
        "orange": "#ff9500",
        "purple": "#a78aff",
        "yellow": "#e2d21d",
        "white": "#fcfcfc"
    }
    color_hiking_iwn_nwn            = '#EA3200'


    ### BORDER ###
    color_country_border_low_z      = '#777777'
    color_country_border            = '#b58cb5'

    # CYCLING
    color_cycle_mtb                 = '#E588ED'
    color_cycle_standard            = '#d320dc'
    color_cycle_icn_ncn             = '#A90073'
    color_cycle_text_ref            = '#B11BB9'
    color_downhill_novice           = '#40ff40'  # was #9440ff40; apply $opacity(58.2%)
    color_downhill_easy             = '#52c1fe'  # was #9952c1fe; apply $opacity(60%)
    color_downhill_intermediate     = '#ff4a4a'  # was #99ff4a4a; apply $opacity(60%)
    color_downhill_advanced         = '#242424'  # was #90242424; apply $opacity(56.7%)
    color_downhill_freeride         = '#f7e337'  # was #99f7e337; apply $opacity(60%)

    # SKI PISTE
    color_nordic_easy               = '#006BD6'
    color_nordic_advanced           = '#590992'
    color_piste_hike                = '#326F9E'
    color_piste_skitour             = '#efa710'
    color_piste_sled                = '#77BF79'

    color_downhill_novice_label     = '#00e900'  # downhill novice caption
    color_downhill_easy_label       = '#07a6fe'  # downhill easy caption
    color_downhill_intermediate_lbl = '#ff4040'  # downhill intermediate caption
    color_piste_lit                 = '#fff41d'  # lit downhill (via $opacity)
    color_ski_nordic_halo           = '#ffffff'  # nordic/backcountry/hike halo  |  was #90ffffff; apply $opacity(56.7%)
    color_ski_tour_halo             = '#ffffff'  # skitour/sled halo  |  was #ccffffff; apply $opacity(80%)

    color_snowmobile                = '#ee7e00'  # snowmobile designated  |  was #90ee7e00; apply $opacity(56.7%)

    ## Summer areas
    color_forest_summer_z13         = '#a0ca6c'  # was #80a0ca6c; apply $opacity(50.4%)
    color_park_orchard_summer       = '#a0ca6c'  # was #80a0ca6c; apply $opacity(50.4%)
    ## Winter areas
    color_forest_winter_z13         = '#a4d4d9'  # was #80a4d4d9; apply $opacity(50.4%)
    color_park_orchard_winter       = '#b3dbcb'  # was #90b3dbcb; apply $opacity(56.7%)


    ##############
    ## TEXT & SYMBOL PRIORITIES
    color_standard_poi_text         = '#303030'
    color_attraction_poi_text       = '#5e5146'
    color_gray_poi_text             = '#747474'
    color_house_number_z18          = '#747474'

    ### neutral / grayscale (light -> dark) ###
    color_white                     = '#ffffff'  # was #ffffff - generic white text-halo / stroke (300x)
    color_gray_ededed               = '#ededed'  # was #ededed - railway main fill / footway area / aerialway cablecar (6x)
    color_gray_d7d7d7               = '#d7d7d7'  # aeroway apron
    color_gray_d5d5d5               = '#d5d5d5'  # tertiary CITY / private-access core
    color_gray_d4d4d4               = '#d4d4d4'  # dam / CITY building (via $darken)
    color_gray_d2d2d2               = '#d2d2d2'  # construction core >16 / tram branch
    color_gray_d0d0d0               = '#d0d0d0'  # was #d0d0d0 - highway-area outline / CITY building (5x)
    color_gray_cecece               = '#cecece'  # winter industrial / power areal / leisure stadium winter case
    color_gray_c1c1c1               = '#c1c1c1'  # parking/runway/taxiway/platform (via $lighten)
    color_gray_b8b8b8               = '#b8b8b8'  # SKI building fill
    color_gray_a8a8a8               = '#a8a8a8'  # SKI building stroke
    color_gray_9f9f9f               = '#9f9f9f'  # track/construction/footway casing
    color_gray_9c9c9c               = '#9c9c9c'  # residential highway stroke
    color_gray_9b9b9b               = '#9b9b9b'  # place=town circle stroke
    color_gray_8e8e8e               = '#8e8e8e'  # place=city circle stroke
    color_gray_8a8a8a               = '#8a8a8a'  # was #8a8a8a - natural area stroke + $opacity gully/embankment (3x)
    color_gray_797979               = '#797979'  # quarry / natural caption / embankment / tram tunnel
    color_gray_747474               = '#747474'  # was #747474 - shield bg-rect / abandoned-railway area (3x)
    color_gray_707070               = '#707070'  # was #707070 - mid-gray road/railway casing + $opacity wraps (52x)
    color_gray_666666               = '#666666'  # barrier fence/wall/chain/retaining_wall
    color_gray_626262               = '#626262'  # NE city/town name circle stroke
    color_gray_606060               = '#606060'  # railway halt stroke
    color_gray_3a3a3a               = '#3a3a3a'  # aerialway chair/mixed lift topo
    color_gray_333333               = '#333333'  # waterway-bridge stroke; runway text; CAR building fill; hospital/school captions
    color_black                     = '#000000'  # bridge casing city/car; street-name text; downhill-advanced label

    ### sea / water ###
    color_sea                       = '#94c3e6'  # sea + NE water/rivers + all standard water fill/stroke + bathymetry depth=0 (28x)
    color_nosea                     = '#f7fbfe'  # natural=nosea
    color_water_label               = '#4f9cbf'  # water/marine/glacier labels + marina text + waterfall (20x)
    color_swimming_pool_case        = '#2797dd'  # swimming_pool stroke

    ### NE bathymetry (shallow -> deep) ###
    color_ne_bathymetry_200         = '#92c1e4'  # bathymetry depth=200
    color_ne_bathymetry_1000        = '#88b7da'  # bathymetry depth=1000
    color_ne_bathymetry_2000        = '#7babcd'  # bathymetry depth=2000
    color_ne_bathymetry_3000        = '#6f9ec1'  # bathymetry depth=3000
    color_ne_bathymetry_4000        = '#6392b5'  # bathymetry depth=4000
    color_ne_bathymetry_5000        = '#5786a9'  # bathymetry depth=5000
    color_ne_bathymetry_6000        = '#4a7a9c'  # bathymetry depth=6000
    color_ne_bathymetry_7000        = '#3e6e90'  # bathymetry depth=7000
    color_ne_bathymetry_8000        = '#326284'  # bathymetry depth=8000
    color_ne_bathymetry_9000        = '#265578'  # bathymetry depth=9000
    color_ne_bathymetry_10000       = '#19496b'  # bathymetry depth=10000
    color_ne_bathymetry_11000       = '#0d3d5f'  # bathymetry depth=11000

    ### waterway / marina / glacier (ARGB) ###
    color_glacier                   = '#d3e9ff'  # natural=glacier fill  |  was #50d3e9ff; apply $opacity(31.6%)
    color_marina_case_outer         = '#4f9cbf'  # marina stroke (outer)  |  was #604f9cbf; apply $opacity(38%)
    color_marina_case_inner         = '#4f9cbf'  # marina stroke (inner)  |  was #404f9cbf; apply $opacity(25.3%)

    ### contour ###
    color_contour                   = '#a07f5f'  # contour minor/major/medium strokes
    color_contour_label             = '#7c583a'  # contour elevation labels

    ### landuse - residential / industrial / quarry ###
    color_landuse_residential_ne    = '#c9c9c9'  # NE residential + residential_city
    color_landuse_residential       = '#d1d1d1'  # residential/retail/industrial (city)
    color_landuse_residential_sum   = '#e0d4b3'  # SUMMER residential (via $darken) + leisure stadium/sports_centre/water_park case
    color_landuse_residential_sum_t = '#e0d4b3'  # SUMMER residential translucent  |  was #90e0d4b3; apply $opacity(56.7%)
    color_landuse_residential_win   = '#e2e2e2'  # WINTER residential
    color_landuse_industrial_sum    = '#bfbfcf'  # SUMMER industrial/brownfield/railway  |  was #90bfbfcf; apply $opacity(56.7%)
    color_landuse_quarry            = '#d6d6e1'  # quarry + power areal

    ### natural / landcover ###
    color_forest_summer_scrub       = '#a0ca6c'  # scrub/fell SUMMER  |  was #30a0ca6c; apply $opacity(19%)
    color_forest_winter_light       = '#cce0e5'  # forest/wood WINTER (distinct from color_forest_winter_z13)
    color_beach_sand                = '#fcf5e0'  # natural=beach / sand
    color_heath                     = '#f1f2e9'  # natural=heath
    color_scree_shingle             = '#dddfe5'  # natural=scree/shingle  |  was #80dddfe5; apply $opacity(50.4%)
    color_wetland_tidalflat         = '#8f5011'  # wetland=tidalflat  |  was #108f5011; apply $opacity(6.5%)
    color_meadow                    = '#34972d'  # meadow/nature_reserve/national_park/botanical (5x)
    color_wood_label                = '#39761a'  # wood/park/cemetery captions (7x)
    color_national_park_case        = '#3fb637'  # protected_area/nature_reserve/hedge stroke (via $opacity)
    color_national_park_border      = '#40be39'  # national_park stroke  |  was #9040be39; apply $opacity(56.7%)
    color_national_park_border2     = '#40be39'  # national_park stroke  |  was #cc40be39; apply $opacity(80%)

    ### leisure ###
    color_leisure_green_summer      = '#dbe5b2'  # golf/common/green SUMMER
    color_leisure_playground_sum    = '#cdeca7'  # playground/pitch/track SUMMER fill (via $darken)
    color_leisure_playground_sum_ln = '#9ccf5e'  # playground/track SUMMER stroke (via $darken)
    color_leisure_green_winter      = '#c7dcdb'  # golf/common/green WINTER
    color_leisure_playground_win    = '#a5e4da'  # playground/track WINTER fill (via $darken)
    color_leisure_playground_win_ln = '#8bb7b5'  # playground/track WINTER stroke (via $darken)
    color_leisure_stadium_city      = '#e1d5b6'  # stadium/sports_centre/water_park + camp/caravan/attraction tourism (via $opacity)

    ### cemetery / meadow / vineyard ###
    color_cemetery_fill             = '#bdd16c'  # cemetery/grave_yard/vineyard/orchard fill  |  was #80bdd16c; apply $opacity(50.4%)
    color_cemetery_case             = '#e4e4e4'  # cemetery/grave_yard stroke
    color_grave_yard_fill           = '#96bfbe'  # amenity=grave_yard fill  |  was #8096bfbe; apply $opacity(50.4%)

    ### tourism ###
    color_tourism_picnic            = '#c7f1a3'  # tourism=picnic_site
    color_tourism_poi_text          = '#826f60'  # attraction + amenity captions + waterway=dam label (6x)
    color_zoo_case                  = '#6e5036'  # zoo topo stroke (via $opacity)
    color_sport_area                = '#d6bfa2'  # sport=* / aeroway terminal / default building fill

    ### aeroway ###
    color_aerodrome_area            = '#cdeca7'  # aeroway=aerodrome translucent  |  was #20cdeca7; apply $opacity(12.7%)

    ### military ###
    color_military_fill             = '#e57a7a'  # landuse/military airfield fill  |  was #25e57a7a; apply $opacity(14.7%)
    color_military_case             = '#e57a7a'  # military stroke  |  was #70e57a7a; apply $opacity(44%)
    color_military_case2            = '#e57a7a'  # military stroke  |  was #90e57a7a; apply $opacity(56.7%)
    color_military_label            = '#925e5a'  # military label

    ### buildings ###
    color_building_default_case     = '#c1a074'  # building stroke
    color_building_city_fill        = '#d9c3c3'  # CITY building fill
    color_building_worship_fill     = '#f6c141'  # place_of_worship/church/... fill
    color_building_station_fill     = '#b178a6'  # train_station/transportation/bus_station fill
    color_building_hospital_fill    = '#ffbfcf'  # building hospital fill
    color_building_public_fill      = '#dbd1c7'  # kindergarten/school/college/university

    ### HIGHWAYS (by class > core > case > zoom/variant) ###
    # -- motorway & trunk --
    color_trunk_motorway_core       = '#f65a57'  # trunk/motorway core CAR (10x)
    color_motorway_link_core_hi     = '#fa9997'  # motorway_link core >16 + motorway
    color_trunk_motorway_city       = '#f99918'  # trunk/motorway CITY
    color_trunk_motorway_city_core  = '#ffd86d'  # trunk/motorway CITY core
    color_indoor_trunk_motorway     = '#fff387'  # trunk/motorway indoor
    color_motorway_toll_case        = '#db100c'  # motorway toll/link outline
    color_trunk_toll_case           = '#f42a27'  # trunk toll/link outline
    # -- primary --
    color_primary_core_car          = '#ed9a06'  # primary core CAR (5x)
    color_primary_trunk_link_core   = '#f3c032'  # primary_link/trunk_link core >16
    color_primary_toll_case         = '#e7740c'  # primary toll/link outline
    color_hw_shield_primary_bg      = '#01498e'  # primary/trunk shield bg-rect-fill
    # -- secondary --
    color_secondary_core_car        = '#daaf14'  # secondary CAR
    color_secondary_primary_city    = '#f1d263'  # secondary/primary CITY
    color_secondary_link_core_hi    = '#f8da76'  # secondary/secondary_link core >16
    color_secondary_shield          = '#e3c015'  # secondary caption stroke
    color_secondary_link_shield     = '#e3c715'  # secondary_link caption stroke
    color_hw_shield_secondary_bg    = '#017dc5'  # secondary shield bg-rect-fill
    # -- tertiary --
    color_tertiary_core_hi          = '#fcecc2'  # tertiary/raceway/tertiary_link core >16
    color_tertiary_case_car         = '#b29a91'  # tertiary/raceway stroke
    # -- raceway / indoor --
    color_raceway_winter            = '#fff6e6'  # raceway winter/indoor
    color_indoor_primary_secondary  = '#fffedc'  # primary/secondary indoor
    # -- motorway junction --
    color_motorway_junction_fill    = '#d97f05'  # motorway_junction fill
    color_motorway_junction_case    = '#ff5b58'  # motorway_junction stroke

    ### path halos ###
    color_path_halo_translucent     = '#ffffff'  # path standard/winter halo  |  was #aaffffff; apply $opacity(67%)
    color_footway_halo_winter       = '#ffffff'  # footway/corridor winter (no white halo)  |  was #40ffffff; apply $opacity(25.3%)

    ### railways ###
    color_railway_station_city      = '#cc6c49'  # railway=station fill CITY/CAR
    color_railway_station_topo      = '#9b9b79'  # railway=station fill TOPO
    color_railway_tram_city         = '#b8462e'  # tram CITY stroke
    color_railway_abandoned         = '#ff707070'  # abandoned main highlight
    color_railway_tunnel_subway     = '#8c0000'  # subway tunnel  |  was #408c0000; apply $opacity(25.3%)
    color_railway_tunnel_tram       = '#cf2b2e'  # tram tunnel
    color_railway_tunnel_tram_topo  = '#0f0f4c'  # tram/miniature tunnel topo  |  was #880f0f4c; apply $opacity(53.5%)
    color_railway_tunnel_rail       = '#4d4d4d'  # rail/light_rail/etc tunnel  |  was #904d4d4d; apply $opacity(56.7%)
    color_power_tower_label         = '#707070'  # power=tower label  |  was #90707070; apply $opacity(56.7%)

    ### man_made / barrier ###
    color_man_made_cutline          = '#b38d5d'  # man_made=cutline
    color_barrier_bollard           = '#488bc2'  # barrier=bollard z15



    ### place circles ###
    color_town_circle_fill          = '#f4f3e9'  # town circle fill + landuse=farm captions
