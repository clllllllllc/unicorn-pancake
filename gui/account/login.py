import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
from db.check_account import check_account

class Login(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        bg_image_url = './gui/account/images/login_bg.png'
        login_image_url = './gui/account/images/sign_in.png'
        width = 533 // 2 * 3 - 10
        height = 800 // 5 * 3

        posx = 492
        posy = 292

        img = Image.open(login_image_url)
        login_img = img.resize((width, height), Image.ANTIALIAS)

        self.login_picture = tk.PhotoImage(file=bg_image_url)
        self.login_item_picture = ImageTk.PhotoImage(login_img)

        self.login_canvas = tk.Canvas(self, width=1680, height=1050, bg="blue")
        self.login_canvas.grid(row=0, column=0)
        self.login_canvas.create_image(0, 0, image=self.login_picture, anchor='nw')
        self.login_canvas.create_text(820, 150, text="LOGIN", font=controller.title_font)

        self.login_canvas.create_text(posx - 10, posy + 193, text="USERNAME", font=controller.normal_font, anchor="nw")

        self.username_e = tk.Entry(self.login_canvas, font=controller.entry_font)
        self.login_canvas.create_window(posx + 230, posy + 180, height=50, width=500, window=self.username_e,
                                        anchor="nw")

        self.login_canvas.create_text(posx - 10, posy + 293, text="PASSWORD", font=controller.normal_font, anchor="nw")

        self.password_e = tk.Entry(self.login_canvas, show="*", font=controller.entry_font)
        self.login_canvas.create_window(posx + 230, posy + 280, height=50, width=500, window=self.password_e,
                                        anchor="nw")

        self.login_b = tk.Button(self.login_canvas, text="LOGIN", command=self.check)
        self.login_canvas.create_window(posx + 280, posy + 450, height=50, width=100, window=self.login_b,
                                        anchor="nw")

        self.back_b = tk.Button(self.login_canvas, text="Back", command=lambda: controller.show_frame("Menu"))
        self.login_canvas.create_window(50, 50, height=30, width=80, window=self.back_b,
                                        anchor="nw")

    def check(self):

        username = self.username_e.get()
        password = self.password_e.get()

        if username == "" or password == "":
            messagebox.showwarning(title="NONONO", message="PLEASE DO NOT LEAVE ANY FIELDS EMPTY")
            return

        if check_account(username, password):
            messagebox.showinfo(title="YEP", message="LOGIN SUCCESSFUL BUT THERE IS NOTHING AHEAD")
        else:
            messagebox.showinfo(title="NONONO", message="USERNAME OR PASSWORD INCORRECT")
