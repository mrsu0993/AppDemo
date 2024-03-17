from components.modules.kivy_imports import (Builder, os)

def load_kv(file_name, file_path=os.path.join("components", "kv")):
    '''
        thực hiện nối chuỗi thư mục đường dẫn: file_path=os.path.join("components", "kv")
        sau đó nối đường dẫn này với tên file lại để tạo thành đường dẫn hoàn chỉnh đến file kv
        os.path.join(file_path, file_name)
    '''
    with open(os.path.join(file_path, file_name), encoding="utf-8") as kv:
        Builder.load_string(kv.read())

# load file kv of screens
def load_kv_screens(file_name, file_path=os.path.join("screens", "kv")):
    '''
        thực hiện nối chuỗi thư mục đường dẫn: file_path=os.path.join("components", "kv")
        sau đó nối đường dẫn này với tên file lại để tạo thành đường dẫn hoàn chỉnh đến file kv
        os.path.join(file_path, file_name)
    '''
    with open(os.path.join(file_path, file_name), encoding="utf-8") as kv:
        Builder.load_string(kv.read())