from components.modules.kivy_imports import (
    utils, StringProperty, MDBoxLayout, TwoLineAvatarIconListItem, IRightBodyTouch, ILeftBodyTouch
)

utils.load_kv("chatitem.kv")

class RightContainer(IRightBodyTouch, MDBoxLayout):
		pass

class LeftContainer(ILeftBodyTouch, MDBoxLayout):
	pass

class ChatItem(TwoLineAvatarIconListItem):
	source = StringProperty()
	username = StringProperty()
	message = StringProperty()
	time = StringProperty()
	date = StringProperty()
	check_icon = StringProperty('numeric-1-circle')
