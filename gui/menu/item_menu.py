import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
from db.check_account import check_account
from com.client_message import start_chat


class Item(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        bg_image_url = './gui/account/images/login_bg.png'

        self.menu_picture = tk.PhotoImage(file=bg_image_url)

        self.menu_canvas = tk.Canvas(self, width=1680, height=1050, bg="blue")
        self.menu_canvas.grid(row=0, column=0)
        self.menu_canvas.create_image(0, 0, image=self.menu_picture, anchor='nw')
        self.menu_canvas.create_text(820, 100, text="MAIN MENU", font=controller.title_font)

        self.join_chat = tk.Button(self.menu_canvas, text="Join Chat Sever", command=self.chat_start)
        self.menu_canvas.create_window(500, 350, height=50, width=130, window=self.join_chat,
                                       anchor="nw")
        self.account_info = tk.Button(self.menu_canvas, text="Join Chat Sever", command=self.chat_start)
        self.menu_canvas.create_window(500, 350, height=50, width=130, window=self.account_info,
                                       anchor="nw")

        self.logout_b = tk.Button(self.menu_canvas, text="Log Out", command=self.logout)
        self.menu_canvas.create_window(50, 50, height=30, width=80, window=self.logout_b,
                                       anchor="nw")

    def chat_start(self):
        self.controller.show_frame("Chat")

    def account_menu(self):
        self.controller.show_frame("Account")

    def logout(self):
        self.controller.username = ''
        self.controller.password = ''
        controller.show_frame("Menu")
