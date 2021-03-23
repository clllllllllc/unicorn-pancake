import tkinter as tk
from tkinter import font as tkfont
from PIL import Image
from PIL import ImageTk
from gui.account.menu import Menu
from gui.account.login import Login
from gui.account.sign_up import SignUp
from gui.menu.item_menu import Item
from gui.menu.chat import Chat


class Operation(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Helvetica', size=128, weight="bold", slant="italic")
        self.normal_font = tkfont.Font(family='Helvetica', size=24, weight="bold", slant="italic")
        self.entry_font = tkfont.Font(family='Helvetica', size=20)
        # self.transparent_bg = tk.PhotoImage(file='./images/nothing.png')
        self.geometry("1680x1050")
        container = tk.Frame(self, height=1050, width=1680)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (Menu, Login, SignUp, Item, Chat):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("Menu")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
