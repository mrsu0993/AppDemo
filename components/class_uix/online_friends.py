from components.modules.kivy_imports import (
    MDRelativeLayout, StringProperty, utils
)

utils.load_kv("online_friends.kv")

class OnlineFriends(MDRelativeLayout):
    avatar = StringProperty()