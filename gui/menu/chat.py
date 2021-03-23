import tkinter as tk
from tkinter import font as tkfont
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
from db.check_account import check_account
from tkinter import ttk as ttk
import com.client_message as cm
import threading
import socket


class Chat(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.menu_canvas = tk.Canvas(self, width=1680, height=1050, bg="blue")
        self.menu_canvas.grid(row=0, column=0)
        self.menu_canvas.create_text(820, 80, text="CHAT", font=controller.title_font)
        self.menu_canvas.create_line(0, 150, 1680, 150)

        self.entryf = tk.Entry(self.menu_canvas)
        self.menu_canvas.create_window(0, 900, height=150, width=1380, window=self.entryf,
                                       anchor="nw")
        self.sendb = tk.Button(self.menu_canvas, text="SEND", font=controller.normal_font, command=self.write)
        self.menu_canvas.create_window(1380, 900, height=150, width=300, window=self.sendb, anchor="nw")

        scrollbar = ttk.Scrollbar(self.menu_canvas)
        self.menu_canvas.create_window(1630, 150, height=750, width=50, window=scrollbar, anchor="nw")

        self.textCons = tk.Text(self.menu_canvas, yscrollcommand=scrollbar.set)
        self.menu_canvas.create_window(0, 150, height=750, width=1680, window=self.textCons, anchor="nw")

        scrollbar.config(command=self.textCons.yview)
        self.textCons.config(state=tk.DISABLED)

        host = '127.0.0.1'
        port = 55554

        self.nickname = "Text Holder"

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()
        # write_thread = threading.Thread(target=write)
        # write_thread.start()

    def receive(self):
        while True:
            try:
                message = self.client.recv(1024).decode('ascii')
                if message == "nick":
                    self.client.send(self.nickname.encode('ascii'))
                else:
                    self.textCons.config(state=tk.NORMAL)
                    self.textCons.insert(tk.END, message + "\n\n")

                    self.textCons.config(state=tk.DISABLED)
                    self.textCons.see(tk.END)
            except:
                print("error occurred")
                self.client.close()
                break

    def write(self):
        try:
            m = self.entryf.get()
            message = f'{self.nickname}: {m}'
            self.client.send(message.encode('ascii'))
            entryf.delete(0, tk.END)
        except:
            pass
