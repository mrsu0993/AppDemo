from components.modules.kivy_imports import (
    MDScreen, utils, MDCustomBottomSheet, Factory, OneLineListItem
)

from components.class_uix.chat import Chat

utils.load_kv_screens("apple_screen.kv")

class Apple_Screen(MDScreen):
    custom_sheet = None
    profile_pic = "https://www1.showbizchaua.com/wp-content/uploads/2018/02/Rear-Mirror-cant-insert.jpg"

    def __init__(self, **kwargs):
        super(Apple_Screen, self).__init__(**kwargs)
        # hàm load_chats() nằm trong lớp Chat
        self.ids.chats.load_chats()
        self.home_others()

    
    def home_others(self):
        for i in range(40):
            self.ids.others.add_widget(
                OneLineListItem(text=f"Single-line item {i}")
            )