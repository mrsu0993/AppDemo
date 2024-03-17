from components.modules.kivy_imports import (
    MDBoxLayout, utils, json, MDScreen
)

from components.class_uix.online_friends import OnlineFriends
from components.class_uix.posts import Post

utils.load_kv_screens("home_screen.kv")

class Home_Screen(MDScreen):
    profile_pic = "https://www1.showbizchaua.com/wp-content/uploads/2018/02/Rear-Mirror-cant-insert.jpg"

    def __init__(self, **kwargs):
        super(Home_Screen, self).__init__(**kwargs)
        self.list_online_friends()
        self.list_posts()


    def list_online_friends(self, *args):
        with open("assets/json/online_friends.json") as f:
            data = json.load(f)
            for name in data:
                self.ids.online_friends.add_widget(
                    OnlineFriends(
                        avatar = data[name]["avatar"]
                    )
                )


    def list_posts(self):
        with open("assets/json/posts_data.json") as f:
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