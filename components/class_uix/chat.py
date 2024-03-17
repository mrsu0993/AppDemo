from components.modules.kivy_imports import (
    ObjectProperty, MDFloatLayout, utils
)

utils.load_kv("chat.kv")

class Chat(MDFloatLayout):
	chat_container = ObjectProperty()
	
	def load_chats(self):
		data = [
			{
				'source':'assets/images/17.jpg',
				'username':'My Love',
				'message':'Good Morning Love',
				'date':'Today',
				'time':'10:12 AM'
			}
			for i in range(50)
		]
		self.chat_container.data = data