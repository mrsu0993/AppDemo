from components.modules.kivy_imports import (
    MDDialog, MDFlatButton, MDGridBottomSheet, MDScreen, utils, MDApp
)

from components.class_uix.ui_class import OneLineTextDialog
from components.class_uix.item import Item

utils.load_kv_screens("profile_screen.kv")

class Profile_Screen(MDScreen):
    dialog = None

    def chevron_back(self):
	    app = MDApp.get_running_app()
	    app.screen_manager.current = 'main_screen'
    
    def change_profile_data(self,widget):
        """force=True: nghĩa là Dialog đóng lập tức mà
        không phụ thuộc các điều kiện khác"""
        dialogObj = None
        Dialog=OneLineTextDialog()
        def cancel_btn(btn):
            # use function when CANCEL btn click
            dialogObj.dismiss(force=True)
        def ok_btn(btn):
            # use function when OK btn click
            widget.text = Dialog.ids.dialog_text.text
            cancel_btn(btn)
            
        '''
            Do đó, nếu dialogObj chưa được khởi tạo hoặc có giá trị None, 
            nó sẽ tạo một đối tượng MDDialog mới và gán cho dialogObj. 
            Nếu dialogObj đã tồn tại, tức là Dialog đang hiển thị
            câu lệnh trong khối if sẽ được bỏ qua và không tạo mới MDDialog
        '''
        if not dialogObj:
            dialogObj=MDDialog(
                auto_dismiss=True,
                title= widget.secondary_text,
                type="custom",
                content_cls=Dialog,
                buttons=[
                    MDFlatButton(
                        text="CANCEL", 
                        # text_color=self.theme_cls.primary_color,
                        on_release=cancel_btn,
                    ),
                    MDFlatButton(
                        text="OK", 
                        # text_color=self.theme_cls.primary_color,
                        on_release=ok_btn,
                    ),
                ],
            )
        dialogObj.open()
        
    
    def change_profile_img(self):
        """
        method call when image click on profile_view page.
        if it's user own profile than show options of change.
        """
        bottom_sheet_menu = MDGridBottomSheet(
        )
        data = {
            "Upload": "cloud-upload",
            "Camera": "camera",
        }
        for item in data.items():
            bottom_sheet_menu.add_item(
                item[0],
                lambda x, y=item[0]: print("hello",x,y),
                icon_src=item[1],
            )
        bottom_sheet_menu.open()


    def show_simple_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Set backup account",
                type="simple",
                items=[
                    Item(text="user01@gmail.com", source="assets/images/love.png"),
                    Item(text="user02@gmail.com", source="assets/images/funny.jpg"),
                ],
            )
        self.dialog.open()