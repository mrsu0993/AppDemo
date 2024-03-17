from components.modules.kivy_imports import (
    OneLineAvatarListItem, utils, StringProperty
)

utils.load_kv("item.kv")

class Item(OneLineAvatarListItem):
    divider = None
    source = StringProperty()