# IMPORT LIBRARIES PYTHON

#################################################################################### KIVY

# IMPORT LIBRARIES KIVY
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.core.window import Window


#################################################################################### KIVYMD

'''
Components

    List                      (su0)
    Backdrop                  (su1)
    Banner                    (su2)
    BottomNavigation          (su3)
    BottomSheet               (su4)
    BoxLayout                 (su5)
    Button                    (su6)
    Card                      (su7)
    Carousel                  (su8)
    Chip                      (su9)
    CircularLayout            (su10)
    ColorPicker               (su11)
    DataTables                (su12)
    DatePicker                (su13)
    Dialog                    (su14)
    DropdownItem              (su15)
    ExpansionPanel            (su16)
    FileManager               (su17)
    FitImage                  (su18)
    FloatLayout               (su19)
    GridLayout                (su20)
    Hero                      (su21)
    ImageList                 (su22)
    Label                     (su23)
    Menu                      (su24)
    NavigationDrawer          (su25)
    NavigationRail            (su26)
    ProgressBar               (su27)
    RecycleGridLayout         (su28)
    RecycleView               (su29)
    RefreshLayout             (su30)
    RelativeLayout            (su31)
    ResponsiveLayout          (su32)
    Screen                    (su33)
    ScreenManager             (su34)
    ScrollView                (su35)
    SegmentedControl          (su36)
    Selection                 (su37)
    SelectionControls         (su38)
    Slider                    (su39)
    SliverAppbar              (su40)
    Snackbar                  (su41)
    Spinner                   (su42)
    StackLayout               (su43)
    Swiper                    (su44)
    Tabs                      (su45)
    TapTargetView             (su46)
    TextField                 (su47)
    TimePicker                (su48)
    Toolbar                   (su49)
    Tooltip                   (su50)
    Transition                (su51)
    Widget                    (su52)
    AnchorLayout              (su53)

'''

# IMPORT LIBRARIES KIVYMD
from kivymd.app import MDApp
from kivymd.icon_definitions import md_icons

# List (su0)
from kivymd.uix.list import (
    MDList,
    BaseListItem,
    IRightBodyTouch, ILeftBodyTouch,
    OneLineListItem, TwoLineListItem, ThreeLineListItem,
    OneLineAvatarListItem, TwoLineAvatarListItem, ThreeLineAvatarListItem,
    OneLineIconListItem, TwoLineIconListItem, ThreeLineIconListItem,
    OneLineRightIconListItem, TwoLineRightIconListItem, ThreeLineRightIconListItem, 
    OneLineAvatarIconListItem, TwoLineAvatarIconListItem, ThreeLineAvatarIconListItem,
    ImageLeftWidget, ImageRightWidget, 
    IconRightWidget, IconLeftWidget,
    ImageRightWidgetWithoutTouch, IconRightWidgetWithoutTouch, IconLeftWidgetWithoutTouch,
    CheckboxLeftWidget
)
from kivymd.uix.selectioncontrol import MDCheckbox

'''
    CÁC THUỘC TÍNH TRONG LỚP List

    text

    text_color

    font_style

    theme_text_color

    secondary_text

    tertiary_text

    secondary_text_color

    tertiary_text_color

    secondary_theme_text_color

    tertiary_theme_text_color

    secondary_font_style

    tertiary_font_style

    divider

    divider_color

    bg_color

    radius

    on_touch_down

    on_touch_move

    on_touch_up

    propagate_touch_to_touchable_widgets

    add_widget

    remove_widget

    pos_hint

'''

# Backdrop (su1)
from kivymd.uix.backdrop.backdrop import (
    MDBackdrop,
    MDBackdropToolbar,
    MDBackdropFrontLayer,
    MDBackdropBackLayer
)


'''
        anchor_title
        padding
        left_action_items
        right_action_items
        title
        back_layer_color
        front_layer_color
        radius_left
        radius_right
        header
        header_text
        close_icon
        opening_time
        opening_transition
        closing_time
        closing_transition
        on_open
        on_close
        on_left_action_items
        on_header
        open
        close
        animate_opacity_icon
        set_new_icon
        add_widget
'''


# MDBanner (su2)
from kivymd.uix.banner import (
    MDBanner
)

'''

    vertical_pad
    opening_transition
    icon
    over_widget
    text
    left_action
    right_action
    type
    opening_timeout
    opening_time
    closing_time
    add_actions_buttons
    show
    hide
    set_type_banner
    animation_display_banner

    

'''


# Bottomnavigation (su3)
from kivymd.uix.bottomnavigation.bottomnavigation import (
    MDTab,
    MDBottomNavigationItem,
    TabbedPanelBase,
    MDBottomNavigation
)

'''
    text

    icon

    badge_icon

    on_tab_touch_down

    on_tab_touch_move

    on_tab_touch_up

    on_tab_press

    on_tab_release

    header

    animate_header

    on_tab_press

    on_disabled

    on_leave

    current

    previous_tab

    panel_color

    tabs

    transition

    transition_duration

    text_color_normal

    text_color_active

    use_text

    selected_color_background

    font_name

    first_widget

    tab_header

    set_bars_color

    widget_index

    set_status_bar_color

    switch_tab

    refresh_tabs

    on_font_name

    on_selected_color_background

    on_use_text

    on_text_color_normal

    on_text_color_active

    on_switch_tabs

    on_size

    on_resize

    add_widget

    remove_widget


'''


# MDBottomSheet (su4)
from kivymd.uix.bottomsheet import (
    MDBottomSheet,
    MDCustomBottomSheet,
    MDListBottomSheet,
    GridBottomSheetItem,
    MDGridBottomSheet

)

'''
    background

    duration_opening

    duration_closing

    radius

    radius_from

    animation

    bg_color

    value_transparent

    open

    add_widget

    dismiss

    resize_content_layout

    screen

    sheet_list

    add_item

    source

    caption

    icon_size

    add_item

'''


# MDBoxLayout (su5)
from kivymd.uix.boxlayout import (
    MDBoxLayout
)

'''
    adaptive_height: True
    adaptive_width: True
    adaptive_size: True
    size_hint_y: None
    md_bg_color
    size_hint_x: None
    height: self.minimum_width, height: self.minimum_height
    size_hint: None, None
    size: self.minimum_size
'''


# button (su6)
from kivymd.uix.button import (  
    BaseButton,
    MDFlatButton,
    MDRaisedButton,
    MDRectangleFlatButton,
    MDRectangleFlatIconButton,
    MDRoundFlatButton,
    MDRoundFlatIconButton,
    MDFillRoundFlatButton,
    MDFillRoundFlatIconButton,
    MDIconButton,
    MDFloatingActionButton,
    MDTextButton,
    MDFloatingActionButtonSpeedDial
)

'''
    padding

    halign

    valign

    text

    icon

    font_style

    theme_text_color

    theme_icon_color

    text_color

    icon_color

    font_name

    font_size

    icon_size

    line_width

    line_color

    line_color_disabled

    md_bg_color

    md_bg_color_disabled

    disabled_color

    rounded_button

    set_disabled_color

    set_all_colors

    set_button_colors

    set_text_color

    set_icon_color

    set_radius

    on_touch_down

    on_touch_up

    on_disabled

    padding

    icon

    set_size

    type

    set_font_size

    set__radius

    set_size_and_radius

    set_size

    on_type

    color

    color_disabled

    animation_label

    on_press

    on_disabled

    icon

    anchor

    label_text_color

    label_bg_color

    label_radius

    data

    right_pad

    right_pad_value

    root_button_anim

    opening_transition

    closing_transition

    opening_transition_button_rotation

    closing_transition_button_rotation

    opening_time

    closing_time

    opening_time_button_rotation

    closing_time_button_rotation

    state

    bg_color_root_button

    bg_color_stack_button

    color_icon_stack_button

    color_icon_root_button

    bg_hint_color

    hint_animation

    stack_buttons

    on_open

    on_close

    on_leave

    on_enter

    on_data

    on_icon

    on_label_text_color

    on_color_icon_stack_button

    on_hint_animation

    on_bg_hint_color

    on_color_icon_root_button

    on_bg_color_stack_button

    on_bg_color_root_button

    on_press_stack_button

    on_release_stack_button

    set_pos_labels

    set_pos_root_button

    set_pos_bottom_buttons

    open_stack

    do_animation_open_stack

    close_stack


'''


# card (su7)
from kivymd.uix.card import (
    MDSeparator,
    MDCard,
    MDCardSwipe,
    MDCardSwipeFrontBox,
    MDCardSwipeLayerBox
)

'''
    color

    on_orientation

    focus_behavior

    ripple_behavior

    radius

    style

    update_md_bg_color

    set_style

    set_line_color

    set_elevation

    set_radius

    on_ripple_behavior

    open_progress

    opening_transition

    closing_transition

    closing_interval

    anchor

    swipe_distance

    opening_time

    state

    max_swipe_x

    max_opened_x

    type_swipe

    add_widget

    on_swipe_complete

    on_anchor

    on_open_progress

    on_touch_move

    on_touch_up

    on_touch_down

    complete_swipe

    open_card

    close_card

'''


# carousel (su8)
from kivymd.uix.carousel import (
    MDCarousel
)

'''

    on_slide_progress

    on_slide_complete

    on_touch_down

    on_touch_up


'''


# chip (su9)
from kivymd.uix.chip import (
    MDChip
)

'''

    text

    icon_left

    icon_right

    text_color

    icon_right_color

    icon_left_color

    icon_check_color

    active

    on_long_touch

    on_active

    do_animation_check

    on_press


'''


# circularlayout (su10)
from kivymd.uix.circularlayout import (
    MDCircularLayout
)

'''

    degree_spacing

    circular_radius

    start_from

    max_degree

    circular_padding

    row_spacing

    clockwise

    get_angle

    remove_widget

    do_layout


'''


# colorpicker (su11)
from kivymd.uix.pickers.colorpicker import (
    MDColorPicker
)

'''

    adjacent_color_constants

    default_color

    type_color

    background_down_button_selected_type_color

    radius_color_scale

    text_button_ok

    text_button_cancel

    selected_color

    update_color_slider_item_bottom_navigation

    update_color_type_buttons

    get_rgb

    on_background_down_button_selected_type_color

    on_type_color

    on_open

    on_select_color

    on_switch_tabs

    on_release


'''


# datatables (su12)
from kivymd.uix.datatables import (
    MDDataTable
)

'''

    column_data

    row_data

    sorted_on

    sorted_order

    check

    use_pagination

    elevation

    rows_num

    pagination_menu_pos

    pagination_menu_height

    background_color

    background_color_header

    background_color_cell

    background_color_selected_cell

    effect_cls

    update_row_data

    add_row

    remove_row

    update_row

    on_row_press

    on_check_press

    get_row_checks

    create_pagination_menu


'''


# datepicker (su13)
from kivymd.uix.pickers.datepicker import (
    BaseDialogPicker,
    DatePickerInputField,
    MDDatePicker

)

'''

    title_input

    title

    radius

    primary_color

    accent_color

    selector_color

    text_toolbar_color

    text_color

    text_current_color

    text_button_color

    input_field_background_color_normal

    input_field_background_color_focus

    input_field_background_color

    input_field_text_color

    input_field_text_color_normal

    input_field_text_color_focus

    font_name

    on_input_field_background_color

    on_input_field_text_color

    on_save

    on_cancel

    helper_text_mode

    owner

    set_error

    input_filter

    is_numeric

    get_list_date

    text_weekday_color

    helper_text

    day

    month

    year

    min_year

    max_year

    mode

    min_date

    max_date

    date_range_text_error

    input_field_cls

    sel_year

    sel_month

    sel_day

    on_device_orientation

    on_ok_button_pressed

    is_date_valaid

    transformation_from_dialog_select_year

    transformation_to_dialog_select_year

    transformation_to_dialog_input_date

    transformation_from_dialog_input_date

    compare_date_range

    update_calendar_for_date_range

    update_text_full_date

    update_calendar

    get_field

    get_date_range

    set_text_full_date

    set_selected_widget

    set_month_day

    set_position_to_current_year

    generate_list_widgets_years

    generate_list_widgets_days

    change_month

'''


# dialog (su14)
from kivymd.uix.dialog import (
    BaseDialog,
    MDDialog
)

'''

    elevation

    shadow_softness

    shadow_offset

    radius

    title

    text

    buttons

    items

    width_offset

    type

    content_cls

    md_bg_color

    update_width

    update_height

    update_items

    on_open

    get_normal_height

    edit_padding_for_item

    create_items

    create_buttons


'''


# dropdownitem (su15)
from kivymd.uix.dropdownitem.dropdownitem import (
    MDDropDownItem
)

'''

    text

    current_item

    font_size

    on_text

    set_item


'''


# expansionpanel (su16)
from kivymd.uix.expansionpanel import (   
    MDExpansionPanelOneLine,
    MDExpansionPanelTwoLine,
    MDExpansionPanelThreeLine,
    MDExpansionPanelLabel,
    MDExpansionPanel
)

'''
    set_paddings

    content

    icon

    opening_transition

    opening_time

    closing_transition

    closing_time

    panel_cls

    on_open

    on_close

    check_open_panel

    set_chevron_down

    set_chevron_up

    close_panel

    open_panel

    get_state

    add_widget

'''


# filemanager (su17)
from kivymd.uix.filemanager import (
    MDFileManager
)

'''
    icon

    icon_selection_button

    background_color_selection_button

    background_color_toolbar

    icon_folder

    icon_color

    exit_manager

    select_path

    ext

    search

    current_path

    use_access

    preview

    show_hidden_files

    sort_by

    sort_by_desc

    selector

    selection

    selection_button

    show_disks

    show

    get_access_string

    get_content

    close

    select_dir_or_file

    back

    select_directory_on_press_button

    on_icon

    on_background_color_toolbar

    on_pre_open

    on_open

    on_pre_dismiss

    on_dismiss

'''


# fitimage (su18)
from kivymd.uix.fitimage import (
    FitImage
)

'''
    source

    mipmap

    reload

'''


# floatlayout (su19)
from kivymd.uix.floatlayout import (
    MDFloatLayout
)

'''
    radius
    md_bg_color
'''


# gridlayout (su20)
from kivymd.uix.gridlayout import (
    MDGridLayout
)

'''
    size_hint: None, None
    size: self.minimum_size
    adaptive_size: True
    size_hint_x: None
    width: self.minimum_width
    adaptive_width: True
    size_hint_y: None
    height: self.minimum_height
    adaptive_height: True
'''


# hero (su21)
from kivymd.uix.hero import (
    MDHeroFrom,
    MDHeroTo
)

'''
    tag

    on_transform_in

    on_transform_out

    tag

'''


# imagelist (su22)
from kivymd.uix.imagelist import (
    MDSmartTile
)

'''
    box_radius

    box_color

    box_position

    overlap

    lines

    source

    mipmap

    on_release

    on_press

    add_widget

'''


# label (su23)
from kivymd.uix.label import ( 
    MDLabel,
    MDIcon
)

'''

    font_style

    text

    theme_text_color

    text_color

    parent_background

    can_capitalize

    canvas_bg

    check_font_styles

    update_font_style

    on_theme_text_color

    on_text_color

    on_opposite_colors

    on_md_bg_color

    on_size

    update_canvas_bg_pos

    icon

    badge_icon

    badge_icon_color

    badge_bg_color

    badge_font_size

    source

    adjust_size

'''


# menu (su24)
from kivymd.uix.menu import (
    MDDropdownMenu
)

'''

    header_cls

    items

    width_mult

    max_height

    border_margin

    ver_growth

    hor_growth

    background_color

    opening_transition

    opening_time

    caller

    position

    radius

    elevation

    check_position_caller

    set_menu_properties

    ajust_radius

    adjust_position

    open

    on_header_cls

    on_touch_down

    on_touch_move

    on_touch_up

    on_dismiss

    dismiss

'''


# navigationdrawer (su25)
from kivymd.uix.navigationdrawer import (
    MDNavigationLayout,
    MDNavigationDrawerLabel,
    MDNavigationDrawerDivider,
    MDNavigationDrawerHeader,
    MDNavigationDrawerItem,
    MDNavigationDrawerMenu,
    MDNavigationDrawer
)

'''

    update_pos

    add_scrim

    update_scrim_rectangle

    add_widget

    text

    padding

    padding

    color

    source

    title

    title_halign

    title_color

    title_font_style

    title_font_size

    text

    text_halign

    text_color

    text_font_style

    text_font_size

    check_content

    selected

    icon

    icon_color

    selected_color

    right_text

    text_right_color

    spacing

    add_widget

    reset_active_color

    type

    anchor

    scrim_color

    padding

    close_on_click

    state

    status

    open_progress

    enable_swiping

    swipe_distance

    swipe_edge_width

    scrim_alpha_transition

    opening_transition

    opening_time

    closing_transition

    closing_time

    set_state

    update_status

    get_dist_from_side

    on_touch_down

    on_touch_move

    on_touch_up

    on_radius

    on_type

'''


# navigationrail (su26)
from kivymd.uix.navigationrail import (
    MDNavigationRailFabButton,
    MDNavigationRailMenuButton,
    MDNavigationRailItem,
    MDNavigationRail
)

'''
    
    icon

    icon

    navigation_rail

    icon

    text

    badge_icon

    badge_icon_color

    badge_bg_color

    badge_font_size

    active

    on_active

    animation_size_ripple_area

    on_press

    on_release

    radius

    padding

    anchor

    type

    text_color_item_normal

    text_color_item_active

    icon_color_item_normal

    icon_color_item_active

    selected_color_background

    ripple_color_item

    ripple_transition

    current_selected_item

    font_name

    on_item_press

    on_item_release

    deselect_item

    get_items

    set_pos_panel_items

    set_current_selected_item

    set_pos_menu_fab_buttons

    add_widget

'''


# progressbar (su27)
from kivymd.uix.progressbar import (
    MDProgressBar
)

'''
    
    reversed

    orientation

    color

    back_color

    running_transition

    catching_transition

    running_duration

    catching_duration

    type

    check_size

    start

    stop

    running_away

    catching_up

'''


# recyclegridlayout (su28)
from kivymd.uix.recyclegridlayout import (
    MDRecycleGridLayout
)

'''
    adaptive_height: True
    size_hint_y: None
    height: self.minimum_height
    adaptive_width: True
    size_hint_x: None
    width: self.minimum_width
    adaptive_size: True
    size_hint: None, None
    size: self.minimum_size

'''


# recycleview (su29)
from kivymd.uix.recycleview import (
    MDRecycleView
)

'''
    md_bg_color
'''


# refreshlayout (su30)
from kivymd.uix.refreshlayout import (
    MDScrollViewRefreshLayout
)

'''
    
    root_layout

    refresh_callback

    on_touch_up

    refresh_done

'''


# relativelayout (su31)
from kivymd.uix.relativelayout import (
    MDRelativeLayout
)

'''
    radius: [25, ]
    md_bg_color
'''


# responsivelayout (su32)
from kivymd.uix.responsivelayout import (
    MDResponsiveLayout
)

'''
    
    mobile_view

    tablet_view

    desktop_view

    on_change_screen_type

    on_size

    set_screen

'''


# screen (su33)
from kivymd.uix.screen import (
    MDScreen
)

'''
    
    hero_to

    heroes_to

    on_hero_to

'''


# screenmanager (su34)
from kivymd.uix.screenmanager import (
    MDScreenManager
)

'''
    
    current_hero

    current_heroes

    check_transition

    get_hero_from_widget

    on_current_hero

    add_widget

'''


# scrollview (su35)
from kivymd.uix.scrollview import (
    MDScrollView
)

'''
    md_bg_color
'''


# segmentedcontrol (su36)
from kivymd.uix.segmentedcontrol import (   
    MDSegmentedControlItem,
    MDSegmentedControl
)

'''
    
    md_bg_color

    segment_color

    segment_panel_height

    separator_color

    radius

    segment_switching_transition

    segment_switching_duration

    current_active_segment

    set_default_colors

    animation_segment_switch

    update_segment_panel_width

    update_separator_color

    add_widget

    on_active

    on_press_segment

'''


# selection (su37)
from kivymd.uix.selection import (
    MDSelectionList
)

'''
    
    icon

    icon_pos

    icon_bg_color

    icon_check_color

    overlay_color

    progress_round_size

    progress_round_color

    add_widget

    get_selected

    get_selected_list_items

    unselected_all

    selected_all

    on_selected

    on_unselected

'''


# selectioncontrol (su38)
from kivymd.uix.selectioncontrol import ( 
    MDCheckbox,
    MDSwitch
)

'''
    
    active

    checkbox_icon_normal

    checkbox_icon_down

    radio_icon_normal

    radio_icon_down

    color_active

    color_inactive

    disabled_color

    selected_color

    unselected_color

    update_primary_color

    update_icon

    update_color

    on_state

    on_active

    active

    icon_active

    icon_inactive

    icon_active_color

    icon_inactive_color

    thumb_color_active

    thumb_color_inactive

    thumb_color_disabled

    track_color_active

    track_color_inactive

    track_color_disabled

    set_icon

    on_active

    on_thumb_down

'''


# slider (su39)
from kivymd.uix.slider import ( 
    MDSlider
)

'''
    
    active

    color

    hint

    hint_bg_color

    hint_text_color

    hint_radius

    thumb_color_active

    thumb_color_inactive

    thumb_color_disabled

    track_color_active

    track_color_inactive

    track_color_disabled

    show_off

    set_thumb_icon

    on_hint

    on_value_normalized

    on_show_off

    on__is_off

    on_active

    on_touch_down

    on_touch_up

'''


# sliverappbar (su40)
from kivymd.uix.sliverappbar import ( 
    MDSliverAppbarContent,
    MDSliverAppbarHeader,
    MDSliverAppbar
)

'''
    
    md_bg_color

    set_bg_color

    toolbar_cls

    background_color

    max_height

    hide_toolbar

    radius

    max_opacity

    on_scroll_content

    on_background_color

    on_toolbar_cls

    on_vbar

    get_default_toolbar

    add_widget

'''


# snackbar (su41)
from kivymd.uix.snackbar import ( 
    BaseSnackbar,
    Snackbar
)

'''
    
    duration

    auto_dismiss

    bg_color

    buttons

    radius

    snackbar_animation_dir

    snackbar_x

    snackbar_y

    dismiss

    open

    on_open

    on_dismiss

    on_buttons

    text

    font_size

'''


# spinner (su42)
from kivymd.uix.spinner import ( 
    MDSpinner
)

'''
    
    determinate

    determinate_time

    line_width

    active

    color

    palette

    on__rotation_angle

    on_palette

    on_active

    on_determinate_complete

    check_determinate

'''


# stacklayout (su43)
from kivymd.uix.stacklayout import ( 
    MDStackLayout
)

'''
    size_hint: None, None
    size: self.minimum_size
    adaptive_size: True
    size_hint_x: None
    width: self.minimum_width
    adaptive_width: True
    size_hint_y: None
    height: self.minimum_height
    adaptive_height: True
'''


# swiper (su44)
from kivymd.uix.swiper import (  
    MDSwiperItem,
    MDSwiper
)

'''
    
    items_spacing

    transition_duration

    size_duration

    size_transition

    swipe_transition

    swipe_distance

    width_mult

    swipe_on_scroll

    add_widget

    remove_widget

    set_current

    get_current_index

    get_current_item

    get_items

    on_swipe

    on_pre_swipe

    on_overswipe_right

    on_overswipe_left

    on_swipe_left

    on_swipe_right

    swipe_left

    swipe_right

    on_scroll_start

    on_touch_down

    on_touch_up

'''


# tab (su45)
from kivymd.uix.tab import (   
    MDTabsBase,
    MDTabs
)

'''
    
    icon

    title_icon_mode

    title

    title_is_capital

    tab_label_text

    tab_label

    tab_label_font_style

    update_label_text

    tab_bar_height

    tab_padding

    tab_indicator_anim

    tab_indicator_height

    tab_indicator_type

    tab_hint_x

    anim_duration

    anim_threshold

    allow_stretch

    fixed_tab_label_width

    background_color

    underline_color

    text_color_normal

    text_color_active

    shadow_softness

    shadow_color

    shadow_offset

    elevation

    indicator_color

    lock_swiping

    font_name

    ripple_duration

    no_ripple_effect

    title_icon_mode

    force_title_icon_mode

    update_icon_color

    switch_tab

    get_tab_list

    get_slides

    get_current_tab

    add_widget

    remove_widget

    on_slide_progress

    on_carousel_index

    on_ref_press

    on_tab_switch

    on_size

'''


# taptargetview (su46)
from kivymd.uix.taptargetview import ( 
    MDTapTargetView
)

'''
    
    widget

    outer_radius

    outer_circle_color

    outer_circle_alpha

    target_radius

    target_circle_color

    title_text

    title_text_size

    title_text_color

    title_text_bold

    description_text

    description_text_size

    description_text_color

    description_text_bold

    draw_shadow

    cancelable

    widget_position

    title_position

    stop_on_outer_touch

    stop_on_target_touch

    state

    start

    stop

    on_open

    on_close

    on_draw_shadow

    on_description_text

    on_description_text_size

    on_description_text_bold

    on_title_text

    on_title_text_size

    on_title_text_bold

    on_outer_radius

    on_target_radius

    on_target_touch

    on_outer_touch

    on_outside_click

'''


# textfield (su47)
from kivymd.uix.textfield import (   
    MDTextFieldRect,
    MDTextField
)

'''
    
    line_anim

    get_rect_instruction

    get_color_instruction

    anim_rect

    helper_text

    helper_text_mode

    max_text_length

    required

    mode

    phone_mask

    validator

    line_color_normal

    line_color_focus

    line_anim

    error_color

    fill_color_normal

    fill_color_focus

    active_line

    error

    hint_text_color_normal

    hint_text_color_focus

    helper_text_color_normal

    helper_text_color_focus

    icon_right_color_normal

    icon_right_color_focus

    icon_left_color_normal

    icon_left_color_focus

    max_length_text_color

    icon_right

    icon_left

    text_color_normal

    text_color_focus

    font_size

    max_height

    radius

    font_name_helper_text

    font_name_hint_text

    font_name_max_length

    cancel_all_animations_on_double_click

    set_colors_to_updated

    set_default_colors

    set_notch_rectangle

    set_active_underline_width

    set_static_underline_color

    set_active_underline_color

    set_fill_color

    set_helper_text_color

    set_max_length_text_color

    set_icon_right_color

    set_icon_left_color

    set_hint_text_color

    set_pos_hint_text

    set_hint_text_font_size

    set_max_text_length

    check_text

    set_text

    set_x_pos

    set_objects_labels

    on_helper_text

    on_focus

    on_icon_left

    on_icon_right

    on_disabled

    on_error

    on_hint_text

    on_width

    on_height

    on_text_color_normal

    on_hint_text_color_normal

    on_helper_text_color_normal

    on_icon_right_color_normal

    on_line_color_normal

    on_max_length_text_color

'''


# timepicker (su48)
from kivymd.uix.pickers.timepicker import ( 
    MDTimePicker
)

'''
    
    hour

    minute

    minute_radius

    hour_radius

    am_pm_radius

    am_pm_border_width

    am_pm

    animation_duration

    animation_transition

    time

    set_time

    get_state

'''


# toolbar (su49)
from kivymd.uix.toolbar.toolbar import ( 
    ActionTopAppBarButton,
    MDTopAppBar,
    MDBottomAppBar
)

'''
    
    overflow_text

    left_action_items

    right_action_items

    title

    mode

    type

    opposite_colors

    md_bg_bottom_color

    set_bars_color

    use_overflow

    overflow_cls

    icon

    icon_color

    anchor_title

    headline_text

    headline_text_color

    type_height

    set_headline_font_style

    on_width

    return_action_button_to_toolbar

    remove_overflow_button

    add_overflow_button

    overflow_action_button_is_added

    add_action_button_to_overflow

    check_overflow_cls

    on_type

    on_type_height

    on_action_button

    on_overflow_cls

    on_md_bg_color

    on_left_action_items

    on_right_action_items

    on_icon

    on_icon_color

    on_md_bg_bottom_color

    on_anchor_title

    on_mode

    set_md_bg_color

    set_notch

    set_shadow

    get_default_overflow_cls

    update_overflow_menu_items

    update_bar_height

    update_floating_radius

    update_anchor_title

    update_action_bar

    update_md_bg_color

    update_action_bar_text_colors

    remove_notch

    remove_shadow

    md_bg_color

    add_widget

'''


# tooltip (su50)
from kivymd.uix.tooltip import ( 
    MDTooltip,
    MDTooltipViewClass
)

'''
    
    tooltip_bg_color

    tooltip_text_color

    tooltip_text

    tooltip_font_style

    tooltip_radius

    tooltip_display_delay

    shift_y

    shift_right

    shift_left

    delete_clock

    adjust_tooltip_position

    display_tooltip

    animation_tooltip_show

    animation_tooltip_dismiss

    remove_tooltip

    on_long_touch

    on_enter

    on_leave

    on_show

    on_dismiss

    tooltip_bg_color

    tooltip_text_color

    tooltip_text

    tooltip_font_style

    tooltip_radius

'''


# transition (su51)
from kivymd.uix.transition.transition import (    
    MDTransitionBase,
    MDSwapTransition,
    MDSlideTransition,
    MDFadeSlideTransition
)

'''
    
    start

    animated_hero_in

    animated_hero_out

    on_complete

    start

    on_progress

'''


# widget (su52)
from kivymd.uix.widget import ( 
    MDWidget
)

'''
    size_hint: .5, None
    height: self.width
    radius: self.height / 2
    md_bg_color: app.theme_cls.primary_color
'''


# widget (su53)
from kivymd.uix.anchorlayout import ( 
    AnchorLayout
)

'''
    size_hint: .5, None
    height: self.width
    radius: self.height / 2
    md_bg_color: app.theme_cls.primary_color
'''


