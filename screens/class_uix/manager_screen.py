from components.modules.kivy_imports import (
    Window, ScreenManager, utils, MDApp
)

utils.load_kv_screens("manager_screen.kv")

class Manager_Screen(ScreenManager):
    def __init__(self, **kwargs):
        super(Manager_Screen, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)
        self.screen_list = list() # Danh sách chứa các màn hình
    
    def _key_handler(self, instance, key, *args):
        
        if key is 27:
            # in Desktop this key 27 is Esc and in Phone it's Back btn
            self.previous_screen()
            return True
    
    # Hàm này cho trường hợp người dùng nhấn nút back trên android, nó là sự kiện handler
    def previous_screen(self):
        """
        Nếu người dùng đang ở cuối cùng mà click thì thoát luôn
        """
        last_screen=self.screen_list.pop()
        if last_screen == "main_screen" or last_screen == "login_screen":
            exit()

        #self.transition.direction = "left"
        self.current = self.screen_list[len(self.screen_list)-1]
 


    def change_screen1(self):
        app = MDApp.get_running_app()
        app.screen_manager.current = 'home'
        


    def change_screen(self,name):
        """
        Switch Screen using screen name and 
        """
        self.current = name 
        if name not in self.screen_list:
            self.screen_list.append(self.current)
        else:
            self.screen_list.remove(name)
            self.screen_list.append(self.current)