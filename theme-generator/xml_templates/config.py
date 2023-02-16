import math

from Cheetah.Template import Template


class TemplateVariables(Template):

    ### HIGHWAYS ###

    color_bridge_casing = "#0d0d0d"
    color_bridge_no_casing = "#4d4d4d"

    color_motorway_z6 = "#ff8c00"
    color_motorway_z7 = "#ff6200"

    color_motorway_z8_z11 = "#FF4500"
    color_trunk_z7 = "#ff8c00"
    color_trunk_z8_z11 = "#FF4500"
    color_primary_z7_z11 = "#ff8c00"
    color_secondary_z10_z11 = "#dab614"
    color_tertiary_z11 = "#B4B4B4"

    color_highway_lowzoom_case = '#FFFFFF'

    color_motorway = "#F7F008"
    color_trunk = "#E5DA1A"
    color_primary = "#FCC57C"
    color_secondary = "#ffee54"
    color_tertiary = "#FFFEE6"
    color_unclassified = "#ffffff"
    color_construction = "#d0d0d0"

    color_motorway_case = "#E52C2C"
    color_trunk_case = "#E52C2C"
    color_primary_case = "#C6523D"
    color_secondary_case = "#938C7A"
    color_tertiary_case = "#707070"
    color_unclassified_case = "#8a8a8a"
    color_footway_area = "#EDEDED"

    color_track = "#8a8a8a"
    color_steps = "#8a8a8a"
    color_footway = "#8a8a8a"
    color_path = "#747474"
    color_path_case = "#FFFFFF"
    color_pedestrian = "#d0d0d0"


    scale_factor = 1.2
    scale_factor_high_zoom = 1.75

    hiking_line_smooth_z13 = 0.25

    ## --- WIDTHS ---

    motorway_width_z6 = 1

    motorway_width_z7 = 2
    trunk_width_z7 = 1
    primary_width_z7 = 1

    motorway_width_z8 = 4
    trunk_width_z8 = 3
    primary_width_z8 = 3
    secondary_width_z10 = 2.5

    motorway_width_z11 = 5.5
    trunk_width_z11 = 5
    primary_width_z11 = 4.5
    secondary_width_z11 = 3.5
    tertiary_width_z11 = 3

    motorway_width_z12 = 4
    trunk_width_z12 = 4
    primary_width_z12 = 3
    secondary_width_z12 = 2
    tertiary_width_z12 = 1.75
    unclassified_width_z12 = 0.9

    motorway_width_z13 = 3.5
    trunk_width_z13 = 3.5
    primary_width_z13 = 3
    secondary_width_z13 = 2.5
    tertiary_width_z13 = 2
    unclassified_width_z13 = 1

    # ZL > 14
    unclassified_width_z14 = unclassified_width_z13
    track_grade1_width_z14 = 0.6
    track_grade2_width_z14 = track_grade1_width_z14
    track_grade3_4_width_z14 = 0.4
    path_width_z14 = 1.1
    footway_width_z14 = 0.4
    steps_width_z14 = 0.6
    construction_width_z14 = 0.4

    # ZL > 16
    scale_factor_z16 = math.pow(1.25, 16 - 13)
    steps_width_z16 = steps_width_z14 / math.pow(1.25, 16 - 15)
    motorway_width_z16 = motorway_width_z13 / scale_factor_z16
    trunk_width_z16 = trunk_width_z13 / scale_factor_z16
    primary_width_z16 = primary_width_z13 / scale_factor_z16
    secondary_width_z16 = secondary_width_z13 / scale_factor_z16
    tertiary_width_z16 = tertiary_width_z13 / scale_factor_z16
    unclassified_width_z16 = unclassified_width_z13 / scale_factor
    track_grade1_width_z16 = track_grade1_width_z14 / scale_factor
    track_grade2_width_z15 = track_grade2_width_z14 / math.pow(1.25, 16 - 14)
    track_grade3_4_width_z15 = track_grade3_4_width_z14 / math.pow(1.25, 16 - 14)
    track_grade5_width_z15 = track_grade3_4_width_z15 * 0.75
    path_width_z15 = path_width_z14 * scale_factor
    footway_width_z16 = footway_width_z14 / math.pow(1.25, 16 - 14)


    ## consistent case size
    highway_case_lowlevel = 2
    highway_case = 1.5
    highway_case_z13 = 0.5
    highway_case_z16 = 0.4

    #tunnel dash specification for highways
    highway_tunnel_dash_array = "20,8"

    ### RAILWAYS

    color_railway_main_case =           '#4d4d4d'
    color_railway_abandoned_case =		'#707070'
    color_railway_service_case =		'#707070'
    color_railway_tunnel = 			    '#707070'
    color_railway_tram =				'#707070'
    color_railway_main =			    '#EDEDED'

    railway_main_width_z10 = 1
    railway_main_width_z13 = 1.5
    railway_main_width_z15 = railway_main_width_z13 / math.pow(1.25, 2)
    railway_main_width_z17 = railway_main_width_z15 / math.pow(1.25, 2)

    railway_service_width_z13 = railway_main_width_z13 * 0.6
    railway_service_width_z15 = railway_main_width_z15 * 0.75
    railway_service_width_z17 = railway_main_width_z17 * 0.75

    railway_spur_narrow_width_z16 = 	2

    ### AERIALWAYS
    color_aerialway_core =          "#4d4d4d"
    color_aerialway_cablecar_fill = "#EDEDED"


    ### OSMC ###

    # Hiking

    osmc_hiking_width_z13 = 1.1
    osmc_hiking_width_z16 = 0.6
    osmc_hiking_width_z18 = 0.3

    # sac scales
    sac_scale_T2_dash_z12 = "11,9"
    sac_scale_T3_dash_z12 = "1,5"

    sac_scale_T2_dash_z16 = "11,9"
    sac_scale_T3_dash_z16 = "0.5,7"

    sac_scale_T2_dash_z18 = "11,9"
    sac_scale_T3_dash_z18 = "1,10"

    osmc_colors = {
        "red": "#EA3200",
        "black": "#330330",
        "blue": "#0026ff",
        "brown": "#93501B",
        "gray": "#575757",
        "green": "#267f00",
        "orange": "#ff9500",
        "purple": "#b399ff",
        "yellow": "#dbbf00",

    }

    osmc_symbol_repeat_start = 30

    ## MTB && Cyclo

    color_cycle_mtb =           '#E588ED'
    color_cycle_standard =      '#d320dc'
    color_cycle_icn_ncn =       '#A90073'
    color_cycle_text_ref =      '#B11BB9'

    text_size_nlbe_junction_z12 = 10
    text_size_nlbe_junction_z14 = text_size_nlbe_junction_z12 * scale_factor
    text_size_nlbe_junction_z17 = text_size_nlbe_junction_z14 * scale_factor

    ##############
    ## WINTER / SKI

    pistes_nordic_width_z13 = 1.6
    pistes_nordic_width_z16 = 0.9

    color_downhill_novice =     '#9940ff40'
    color_downhill_easy =       '#9952c1fe'
    color_downhill_intermediate='#99FF4A4A'
    color_downhill_advanced =   '#90000000'
    color_downhill_freeride =   '#99f7e337'

    color_nordic_easy =         '#006BD6'
    color_nordic_advanced =     '#590992'
    color_piste_hike =          '#326F9E'
    color_piste_skitour =       '#efa710'
    color_piste_sled =          '#77BF79'


    ##############
    ## TEXT & SYMBOL PRIORITIES

    color_standard_poi_text =   '#303030'
    color_attraction_poi_text = '#5e5146'
    color_gray_poi_text =       '#747474'
    color_house_number_z18 =    '#747474'

    text_halo = 4
    text_wrap_standard = 110
    street_text_size_z15 = 11
    street_text_size_z18 = 11 * scale_factor * scale_factor

    # Priorities

    priority_city_1 = 500
    priority_city_2 = 490
    priority_town_1 = 480
    priority_town_2 = 470
    priority_village_1 = 460
    priority_village_2 = 450
    priority_suburb = 440
    priority_hamlet = 430
    priority_locality = 420
    priority_street = 400


    priority_poi_caption_cat1 = 415
    priority_poi_caption_cat2 = 414
    priority_poi_caption_cat3 = 413


    priority_cyclo_nlbe_junction_circle = 410
    priority_cyclo_nlbe_junction_number = priority_cyclo_nlbe_junction_circle + 1

    priority_tourist_route_name = 200
    priority_tourist_osmc_symbol = 35

    priority_water_area = 395
    priority_river = 390
    priority_canal = 385
    priority_stream = 1





    #### Generator actions
    # Tunnels
    gen_action_create_highway_tunnels = "action_create_tunnels"

    # Bridges
    gen_action_create_railway_bridge = "action_create_railway_bridge"

    # OSMC colored lines
    gen_action_osmc_colors = "action_create_osmc_colors"
    # replace osmc by sac scale
    gen_action_sac_scale2lwn = "action_sac_scales_to_lwn"


    # Duplicate style of RCN to ICN cycle routes to change it's color
    gen_action_cycle_icn = "action_create_cycle_icn"
    gen_action_cycle_basic_to_mtb_scale_0 = "action_create_mtb_scale_0_from_basic"

    # Duplicate OSMC symbols part to order symbols along line
    gen_action_osmc_symbols_order = "action_create_osmc_symbols_order"

