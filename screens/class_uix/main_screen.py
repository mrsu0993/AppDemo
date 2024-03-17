from components.modules.kivy_imports import (
    MDScreen, json, utils, Clock
)

from screens.class_uix.home_screen import Home_Screen
from screens.class_uix.youtube_screen import Youtube_Screen
from screens.class_uix.apple_screen import Apple_Screen
from screens.class_uix.tag_screen import Tag_Screen

utils.load_kv_screens("main_screen.kv")

class Main_Screen(MDScreen):
    profile_pic = "https://www1.showbizchaua.com/wp-content/uploads/2018/02/Rear-Mirror-cant-insert.jpg"

    def on_enter(self):
        self.home_screen()
        self.youtube_screen()
        self.apple_screen()
        self.tag_screen()


    def home_screen(self):
        self.ids.home.add_widget(
            Home_Screen()
        )

    def youtube_screen(self):
        self.ids.youtube.add_widget(
            Youtube_Screen()
        )

    def apple_screen(self):
        self.ids.apple.add_widget(
            Apple_Screen()
        )

    def tag_screen(self):
        self.ids.tag.add_widget(
            Tag_Screen()
        )

    
    '''
        self.list_online_friends()
        self.list_stories()
        self.list_posts()
    '''

'''
    def list_online_friends(self):
        with open("jsons/online_friends_data.json") as f:
            data = json.load(f)
            for friend in data:
                self.ids.online_friends.add_widget(
                    OnlineAvatarImage(
                        avatar=data[friend]["avatar"]
                    )
                )

    def list_stories(self):
        with open("jsons/stories_data.json") as f:
            data = json.load(f)
            for friend_name in data:
                self.ids.stories.add_widget(
                    StoryWidget(
                        name = friend_name,
                        image = data[friend_name]["image"],
                        avatar = data[friend_name]["avatar"]
                    )
                )

    def list_posts(self):
        with open("jsons/posts_data.json") as f:
            data = json.load(f)
            for friend_name in data:
                self.ids.timeline.add_widget(
                    Post(
                        name = friend_name,
                        avatar = data[friend_name]["avatar"],
                        post = data[friend_name]["post"],

                        likes = data[friend_name]["likes"],
                        comments = data[friend_name]["comments"],
                        caption = data[friend_name]["caption"],
                        updated_ago = data[friend_name]["updated_ago"]
                    )
                )


'''




## MẪU GIAO DIỆN KV: <HomePage>
'''

#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import AvatarImage components.avatar_image.AvatarImage
#:import ThreeButtons components.three_buttons.ThreeButtons

<HomePage>:

    # App background color
    md_bg_color: 1, 1, 1, 1

    MDBoxLayout:
        orientation: 'vertical'

        # Appbar
        MDTopAppBar:
            md_bg_color: 1, 1, 1, 1
            title: "facebook"
            specific_text_color: get_color_from_hex("#1777F2")
            right_action_items: [["magnify"], ["facebook-messenger"]]
            elevation: 0
            #md_bg_color: "#ffffff"


        # Tab Icons
        MDBoxLayout:
            adaptive_size: True
            height: 30
            pos_hint: {"center_x": .5}
            spacing: dp(15)

            MDIconButton:
                icon: "home"
            MDIconButton:
                icon: "account-circle-outline"
            MDIconButton:
                icon: "account-group-outline"
            MDIconButton:
                icon: "bell-outline"
            MDIconButton:
                icon: "menu"

        MDBoxLayout:
            ScrollView:
                bar_width: 0
                MDBoxLayout:
                    adaptive_height: True


                    # Profile pictube and update status button
                    MDBoxLayout:
                        adaptive_height: True
                        orientation: "vertical"
                        #id: timeline

                        MDSeparator:
                            size_hint_y: None
                            height: 8
                            md_bg_color: 1,1,1,1

                        MDBoxLayout: 
                            orientation: "horizontal"
                            padding: 10
                            spacing: 20
                            adaptive_height: True
                            height: 100

                            # Profile pictute
                            AvatarImage:
                                source: root.profile_pic

                            # Update status button
                            MDRoundFlatButton:
                                text: 'Write something here...\nWrite something here...'
                                size_hint: 1, 1
                                line_color: 0, 0, 0, 1
                                text_color: 0, 0, 0, 1

                        MDSeparator:
                            size_hint_y: None
                            height: 8
                            md_bg_color: 1,1,1,1

                        # Three buttons: live, Photo and Reels
                        MDBoxLayout: 
                            adaptive_height: True
                            height: 40
                            padding: 5
                            spacing: 10

                            ThreeButtons:
                                text: "Live"
                                icon: "video"
                                icon_color: get_color_from_hex("#F2413D")

                            MDSeparator:
                                size_hint_x: None
                                width: 1
                                height: 40
                                md_bg_color: 1,1,1,1

                            # Photo Button
                            ThreeButtons:
                                text: "Photo"
                                icon: "image-multiple"
                                icon_color: get_color_from_hex("#86BE49")

                            MDSeparator:
                                size_hint_x: None
                                width: 1
                                height: 40
                                md_bg_color: 1,1,1,1

                            # Reels button
                            ThreeButtons:
                                text: "Reels"
                                icon: "movie-play"
                                icon_color: get_color_from_hex("#00A4F5")

                        MDSeparator:
                            size_hint_y: None
                            height: 8
                            md_bg_color: 1,1,1,1

                        # List of all online friends
                        ScrollView:
                            size_hint_y: None
                            height: 70
                            bar_width: 0

                            MDBoxLayout:
                                adaptive_width: True
                                spacing: 10
                                padding: 10

                                MDRoundFlatIconButton:
                                    text: "Create\nRoom"
                                    icon: "video-plus"
                                    pos_hint: {"center_x": 0.5, "center_y": 0.5}
                                    line_color: "red"
                                    theme_icon_color: "Custom"
                                    icon_color: "orange"
                                    theme_text_color: "Custom"
                                    text_color: "green"
                                    

                                # List of all online friends images
                                MDBoxLayout:
                                    adaptive_width: True
                                    id: online_friends
                                    padding: 10
                                    spacing: 30
                                    pos_hint: {"center_x": 0.5, "center_y": 0.4}

                        MDSeparator:
                            size_hint_y: None
                            height: 8
                            md_bg_color: 1,1,1,1

                        MDBoxLayout:
                            adaptive_height: True
                            padding: 10
                            height: 200

                            ScrollView:
                                size_hint_y: None
                                height: dp(190)
                                bar_width: 0

                                MDBoxLayout: 
                                    adaptive_width: True
                                    spacing: 130

                                    # Creatory Story Widget
                                    MDBoxLayout:
                                        md_bg_color: 1,1,1,1
                                        size_hint_y: None
                                        size: '110dp','190dp'

                                        MDRelativeLayout:
                                            md_bg_color: get_color_from_hex("#EBEBEB")
                                            radius: 15
                                            pos_hint: {"top": 1, "left": 1}
                                            size_hint: None, None
                                            size: '100dp','190dp'

                                            FitImage:
                                                source: root.profile_pic
                                                radius: [15,15,0,0]
                                                mipmap: True
                                                size_hint: None, None
                                                size: dp(100), dp(100)
                                                pos_hint: {"top": 1, "left": 1}

                                            FitImage:
                                                source: "images/plus.png"
                                                pos_hint: {"center_x": .5, "center_y": .35}
                                                size_hint: None, None
                                                size: 40, 40

                                            MDLabel:
                                                text: "Create Story"
                                                theme_text_color: "Custom"
                                                text_color: 0,0,1,1
                                                halign: "center"
                                                font_size: 14
                                                pos_hint: {"center_x": .5, "center_y": .1}
                                                adaptive_height: True
                                    
                                    # Friends Stories
                                    MDBoxLayout: 
                                        adaptive_width: True
                                        id: stories

                                    
                        MDSeparator:
                            size_hint_y: None
                            height: 4
                            md_bg_color: 1,1,1,1

                        MDBoxLayout:
                            adaptive_height: True
                            orientation: "vertical"
                            id: timeline
                            spacing: dp(70)
                            padding: 0, dp(70), 0, 0


'''





## MẪU GIAO DIỆN KV: <Post>
'''

<Post>
    orientation: "vertical"
    size_hint_y: None
    height: dp(520)
    spacing: 10
    id: mrsu

    MDBoxLayout: 
        padding: dp(5)
        adaptive_height: True
        padding: 0, 0, 0, -15

        TwoLineAvatarIconListItem:
            text: root.name
            secondary_text: root.updated_ago
            divider: None
            _no_ripple_effect: True

            ImageLeftWidget:
                source: root.avatar
                radius: [20, ]
                

        MDIconButton:
            icon: "dots-horizon"

    MDBoxLayout:
        adaptive_height: True
        height: 10
        padding: 20, 0, 0, 0

        MDLabel:
            text: root.caption
            adaptive_height: True

    FitImage: 
        size_hint_y: None
        height: mrsu.height * 0.8
        source: root.post

    MDBoxLayout: 
        adaptive_height: True
        padding: 5
        spacing: 1

        # Reactions
        Reactions: 
            source: "assets/images/funny.jpg"
        Reactions: 
            source: "assets/images/love.png"
        Reactions: 
            source: "assets/images/cry.jpg"

        MDLabel:
            text: f"{root.likes}"
            font_size: 13

        Widget:

        MDLabel:
            text: f"{root.comments} comments"
            font_size: 13
            shorten: True

    # Like, comment, share buttons
    MDBoxLayout:
        adaptive_height: True
        padding: 0, -10, 0, 0

        ReactionButtons:
            icon: "thumb-up-outline"
            text: "Like"
        ReactionButtons:
            icon: "comment-outline"
            text: "Comment"
        ReactionButtons:
            icon: "share-outline"
            text: "Share"

<ReactionButtons@MDRectangleFlatIconButton>:
    theme_text_color: "Custom"                
    text_color: 0,0,0,1
    line_color: 1,1,1,1
    icon_color: 0,0,0,1

<Reactions@FitImage>:
    size_hint: None, None
    size: 15, 15
    radius: [10, ]

'''



## MẪU GIAO DIỆN KV: <StoryWidget>
'''

<StoryWidget>
    size_hint: None, None
    size: dp(110), dp(190)
    md_bg_color: 1,1,1,1

    MDCard:
        pos_hint: {"center_x": .5, "center_y": .5}
        id: card
        size_hint: None, None
        size: dp(100), dp(190)
        radius: 15

        FitImage:
            source: root.image
            radius: [15, ]
            mipmap: True

    MDCard:
        size_hint: None, None
        size: dp(30), dp(30)
        radius: 15
        x: 10
        y: card.height - self.height * 1.2
        elevation: 3

        FitImage:
            source: root.avatar
            radius: [27, ]
            mipmap: True

    MDLabel:
        halign: "center"
        pos_hint: {"center_x": .5, "center_y": .1}
        text: root.name
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        font_size: dp(10)

'''



## MẪU GIAO DIỆN KV: <OnlineAvatarImage> 

'''

#:import AvatarImage components.avatar_image.AvatarImage

<OnlineAvatarImage>
    size_hint: None, None
    md_bg_color: 1, 1, 1, 1
    size: 40, 40

    AvatarImage:
        source: root.avatar
        pos_hint: {"center_x": .5, "center_y": .5}

    # Green icon represents online
    FitImage:
        source: "images/red.png"
        size_hint: None, None
        size: dp(20), dp(20)
        pos_hint: {"x": 0.75, "y": -.2}


'''



## MẪU GIAO DIỆN KV: <AvatarImage>

'''

<AvatarImage>:
    radius: [40, ]
    size_hint: None,None
    size: '50dp','50dp'

'''



## MẪU GIAO DIỆN KV: <ThreeButtons>

'''

<ThreeButtons>
    size_hint: 1, 1
    theme_text_color: "Custom"
    text_color: 0, 0, 0, 1
    line_color: 1, 1, 1, 1
    _no_ripple_effect: True

'''