from components.modules.kivy_imports import (
    MDTabsBase, MDFloatLayout, utils
)

utils.load_kv("tab.kv")

class Tab(MDTabsBase, MDFloatLayout):
	pass