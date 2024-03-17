from components.modules.kivy_imports import (
    MDRelativeLayout, utils, StringProperty
)

utils.load_kv("story_widget.kv")

class StoryWidget(MDRelativeLayout):
    name = StringProperty()
    avatar = StringProperty()
    image = StringProperty()