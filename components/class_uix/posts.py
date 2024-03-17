from components.modules.kivy_imports import (
    MDCard, StringProperty, utils
)

utils.load_kv("posts.kv")

class Post(MDCard):
    name = StringProperty()
    avatar = StringProperty()
    post = StringProperty()

    likes = StringProperty()
    comments = StringProperty()
    caption = StringProperty()
    updated_ago = StringProperty()