import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
import gui.account.verifier as verify
from db.new_account import create_account


class SignUp(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        bg_image_url = './gui/account/images/login_bg.png'
        login_image_url = './gui/account/images/sign_in.png'
        width = 533 // 2 * 3 - 10
        height = 800 // 5 * 3

        posx = 492
        posy = 292

        posyl = [posy + 50, posy + 100, posy + 150, posy + 200, posy + 250, posy + 300]
        posyl2 = [posy + 50 - 13, posy + 100 - 13, posy + 150 - 13, posy + 200 - 13, posy + 250 - 13, posy + 300 - 13]

        img = Image.open(login_image_url)
        login_img = img.resize((width, height), Image.ANTIALIAS)

        self.login_picture = tk.PhotoImage(file=bg_image_url)
        self.login_item_picture = ImageTk.PhotoImage(login_img)

        self.login_canvas = tk.Canvas(self, width=1680, height=1050, bg="blue")
        self.login_canvas.grid(row=0, column=0)
        self.login_canvas.create_image(0, 0, image=self.login_picture, anchor='nw')
        self.login_canvas.create_text(820, 150, text="SIGN UP", font=controller.title_font)

        self.login_canvas.create_text(posx - 10, posyl[0], text="Username", font=controller.normal_font, anchor="nw")
        self.username_e = tk.Entry(self.login_canvas, font=controller.entry_font)
        self.login_canvas.create_window(posx + 230, posyl2[0], height=50, width=500, window=self.username_e,
                                        anchor="nw")

        self.login_canvas.create_text(posx - 10, posyl[1], text="Password", font=controller.normal_font, anchor="nw")
        self.password_e = tk.Entry(self.login_canvas, show="*", font=controller.entry_font)
        self.login_canvas.create_window(posx + 230, posyl2[1], height=50, width=500, window=self.password_e,
                                        anchor="nw")

        self.login_canvas.create_text(posx - 10, posyl[2], text="Password Verify", font=controller.normal_font,
                                      anchor="nw")
        self.repassword_e = tk.Entry(self.login_canvas, show="*", font=controller.entry_font)
        self.login_canvas.create_window(posx + 230, posyl2[2], height=50, width=500, window=self.repassword_e,
                                        anchor="nw")

        self.login_canvas.create_text(posx - 10, posyl[3], text="Avatar Name", font=controller.normal_font, anchor="nw")
        self.an_e = tk.Entry(self.login_canvas, font=controller.entry_font)
        self.login_canvas.create_window(posx + 230, posyl2[3], height=50, width=500, window=self.an_e,
                                        anchor="nw")

        self.login_canvas.create_text(posx - 10, posyl[4], text="Email", font=controller.normal_font, anchor="nw")
        self.email_e = tk.Entry(self.login_canvas, font=controller.entry_font)
        self.login_canvas.create_window(posx + 230, posyl2[4], height=50, width=500, window=self.email_e,
                                        anchor="nw")

        self.login_canvas.create_text(posx - 10, posyl[5], text="Email Verify", font=controller.normal_font,
                                      anchor="nw")
        self.emailv_e = tk.Entry(self.login_canvas, font=controller.entry_font)
        self.login_canvas.create_window(posx + 230, posyl2[5], height=50, width=500, window=self.emailv_e,
                                        anchor="nw")

        self.send_verify = tk.Button(self.login_canvas, text="Back", command=self.verify_email)
        self.login_canvas.create_window(posx + 20, posyl[5] + 60, height=30, width=80, window=self.send_verify,
                                        anchor="nw")

        self.back_b = tk.Button(self.login_canvas, text="Back", command=lambda: controller.show_frame("Menu"))
        self.login_canvas.create_window(50, 50, height=30, width=80, window=self.back_b,
                                        anchor="nw")

        self.login_b = tk.Button(self.login_canvas, text="LOGIN", command=self.new_account)
        self.login_canvas.create_window(posx + 280, posy + 450, height=50, width=100, window=self.login_b,
                                        anchor="nw")

    def verify_email(self):
        pass

    def new_account(self):
        username = self.username_e.get()
        password = self.password_e.get()
        password_re = self.repassword_e.get()
        email = self.email_e.get()
        avatar = self.an_e.get()

        if username == "" or password == "" or password_re == "" or email == "" or avatar == "":
            messagebox.showwarning(title="NONONO", message="PLEASE DO NOT LEAVE ANY FIELDS EMPTY")
            return

        if password != password_re:
            messagebox.showwarning(title="NONONO", message="PLEASE ENSURE BOTH PASSWORDS ENTERED ARE THE SAME")
            return

        try:
            create_account(username, password, email, avatar)
        except:
            messagebox.showwarning(title="NONONO", message="USERNAME ALREADY EXIST")
            return

        self.username_e.delete(0, tk.END)
        self.password_e.delete(0, tk.END)
        self.repassword_e.delete(0, tk.END)
        self.email_e.delete(0, tk.END)
        self.an_e.delete(0, tk.END)
        self.emailv_e.delete(0, tk.END)
        self.controller.show_frame("Menu")
