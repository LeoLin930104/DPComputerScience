import tkinter as tk
from tkinter.ttk import Frame, Label, Entry, Button
from .theme import PADX, PADY, ENTRY_WIDTH, LABEL_WIDTH

class SignInView(Frame):
    def __init__(self, master):
        super().__init__(master=master)

        self.layout_components()

    def layout_components(self):
        self.pack(fill = tk.BOTH, expand = False, padx = PADX, pady = PADY)

        self.username = tk.StringVar()
        self.username.set("")
        self.password = tk.StringVar()
        self.password.set("")

        # Username Row
        uFrame = Frame(self)
        uFrame.pack(fill = tk.X)
        uLabel = Label(uFrame, text = "Username: ", width = LABEL_WIDTH)
        uLabel.pack(side = tk.LEFT, padx = PADX, pady = PADY)
        uEntry = Entry(uFrame, width = ENTRY_WIDTH, textvariable = self.username)
        uEntry.pack(fill = tk.X, padx = PADX, pady = PADY, expand = True)

        # Password Row
        pFrame = Frame(self)
        pFrame.pack(fill = tk.X)
        pLabel = Label(pFrame, text = "Password: ", width = LABEL_WIDTH)
        pLabel.pack(side = tk.LEFT, padx = PADX, pady = PADY)
        pEntry = Entry(pFrame, width = ENTRY_WIDTH, textvariable = self.password, show = "*")
        pEntry.pack(fill = tk.X, padx = PADX, pady = PADY, expand = True)