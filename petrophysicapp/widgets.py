import ttkbootstrap as tkb
import tkinter as tk

class MainWidgets:
    def __init__(self, root):
        self.root = root

        self.button = tkb.Button(self.root, text="Clique-me")
        self.button.pack(pady=20)
