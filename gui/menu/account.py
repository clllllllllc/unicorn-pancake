import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
from db.check_account import check_account
from com.client_message import start_chat


class Account(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        bg_image_url = './gui/account/images/login_bg.png'

        self.account_picture = tk.PhotoImage(file=bg_image_url)

        self.account_canvas = tk.Canvas(self, width=1680, height=1050, bg="blue")
        self.account_canvas.grid(row=0, column=0)
        self.account_canvas.create_image(0, 0, image=self.account_picture, anchor='nw')
        self.account_canvas.create_text(820, 100, text="MAIN MENU", font=controller.title_font)

        self.logout_b = tk.Button(self.account_canvas, text="Log Out", command=self.logout)
        self.account_canvas.create_window(50, 50, height=30, width=80, window=self.logout_b,
                                          anchor="nw")

    def logout(self):
        self.controller.username = ''
        self.controller.password = ''
        controller.show_frame("Menu")
