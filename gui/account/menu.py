import tkinter as tk
from tkinter import font as tkfont
from PIL import Image
from PIL import ImageTk


class Menu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        image_url = './gui/account/images/menu_image.png'
        self.controller = controller
        self.label = tk.Label(self, text="AAABBBCCC", font=controller.title_font)
        self.label.grid(row=1, column=1)
        self.menu_picture = tk.PhotoImage(file=image_url)
        self.menu_canvas = tk.Canvas(self, width=300, height=200, bg='green')

        self.menu_canvas.grid(row=2, column=1)
        self.menu_canvas.create_image(100, 100, image=self.menu_picture, anchor='nw')
        self.login_button = tk.Button(self, text="LOGIN", command=lambda: controller.show_frame("Login"),
                                      font=controller.normal_font)
        self.login_button.grid(row=3, column=1)

        self.signup_button = tk.Button(self, text="SIGN UP", command=lambda: controller.show_frame("SignUp"),
                                       font=controller.normal_font)
        self.signup_button.grid(row=3, column=2)
