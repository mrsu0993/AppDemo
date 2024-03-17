from components.modules.kivy_imports import (
    MDBoxLayout, utils, json, MDScreen
)

from components.class_uix.story_widget import StoryWidget
from components.class_uix.posts import Post

utils.load_kv_screens("youtube_screen.kv")

class Youtube_Screen(MDScreen):
    profile_pic = "https://www1.showbizchaua.com/wp-content/uploads/2018/02/Rear-Mirror-cant-insert.jpg"

    def __init__(self, **kwargs):
        super(Youtube_Screen, self).__init__(**kwargs)
        self.list_stories()
        self.list_posts()


    def list_stories(self):
        with open("assets/json/stories_data.json") as f:
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
        with open("assets/json/posts_data.json") as f:
            data = json.load(f)
            for friend_name in data:
                self.ids.post.add_widget(
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