import ttkbootstrap as tkb
from functions import Functions
from widgets import MainWidgets

class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Exemplo Tkinter")

        self.root.geometry("500x250")
        
        self.widgets = MainWidgets(self.root)
        self.func = Functions()
        
        self.widgets.button.config(command=self.func.organize_velocity_data())

    def show_message(self):
        self.message_box.show_greeting()
