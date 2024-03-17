from components.modules.kivy_imports import (
    MDBoxLayout, utils, MDCustomBottomSheet, Factory, MDScreen
)

# from components.class_uix.story_widget import StoryWidget
# from components.class_uix.posts import Post

utils.load_kv_screens("tag_screen.kv")

class Tag_Screen(MDScreen):
    custom_sheet = None


    def show_sheet(self):
        self.custom_sheet = MDCustomBottomSheet(screen=Factory.CustomSheet())
        self.custom_sheet.open()