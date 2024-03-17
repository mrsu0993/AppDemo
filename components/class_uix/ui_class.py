from components.modules.kivy_imports import (
    MDBoxLayout, utils
)

utils.load_kv("ui_class.kv")

class OneLineTextDialog(MDBoxLayout):
    
    def input_text(self):
        return self.ids.dialog_text.text
