from components.modules.kivy_imports import (
    MDApp, Window, FadeTransition
)

from screens.class_uix.manager_screen import Manager_Screen
from screens.class_uix.login_screen import Login_Screen
from screens.class_uix.signup_screen import Signup_Screen
from screens.class_uix.forgot_screen import Forgot_Screen
from screens.class_uix.profile_screen import Profile_Screen
from screens.class_uix.youtube_screen import Youtube_Screen
from screens.class_uix.apple_screen import Apple_Screen
from screens.class_uix.home_screen import Home_Screen
from screens.class_uix.tag_screen import Tag_Screen
from screens.class_uix.verification_screen import Verification_Screen

#Window.size = [350, 650]

class SuSpeakApp(MDApp):

    def __init__(self, **kwargs):
        super(SuSpeakApp, self).__init__(**kwargs)
        
        self.APP_NAME = "SuSpeak"
        self.COMPANY_NAME = "SuSpeak.org"

    def build(self):

        self.screen_manager = Manager_Screen(transition=FadeTransition())
        self.screen_manager.add_widget(Login_Screen())
        self.screen_manager.add_widget(Home_Screen()) 
        self.screen_manager.add_widget(Signup_Screen())
        self.screen_manager.add_widget(Forgot_Screen())      
        self.screen_manager.add_widget(Profile_Screen())
        self.screen_manager.add_widget(Youtube_Screen())
        self.screen_manager.add_widget(Apple_Screen())
        self.screen_manager.add_widget(Tag_Screen())
        self.screen_manager.add_widget(Verification_Screen())

        return self.screen_manager

    def on_start(self):
        self.screen_manager.change_screen("login_screen")

SuSpeakApp().run()