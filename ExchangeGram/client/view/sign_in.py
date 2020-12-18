import tkinter as tk
from tkinter.ttk import Frame, Label, Entry, Button
from .theme import PADX, PADY, ENTRY_WIDTH, LABEL_WIDTH
from tkinter import font

class SignInView(Frame):
    def __init__(self, master):
        super().__init__(master=master)
        self.layout_components()
        # Setup Callbacks
        self.show_register: Callable = None
        self.sign_in: Callable = None

    def layout_components(self):
        self.pack(fill = tk.BOTH, expand = False, padx = PADX, pady = PADY)
        error_font = font.Font(family = "Times New Roman", size = 8)

        # Variables
        self.username = tk.StringVar()
        self.username.set("")

        self.password = tk.StringVar()
        self.password.set("")

        # Username Row
        uFrame = Frame(self)
        uFrame.pack(fill = tk.X)
        uLabel = Label(uFrame, text = "Username:", width = LABEL_WIDTH)
        uLabel.pack(side = tk.LEFT, padx = PADX, pady = PADY)
        self.uEntry = Entry(uFrame, width = ENTRY_WIDTH, textvariable = self.username)
        self.uEntry.pack(fill = tk.X, padx = PADX, pady = PADY, expand = True)

        # Password Row
        pFrame = Frame(self)
        pFrame.pack(fill = tk.X)
        pLabel = Label(pFrame, text = "Password:", width = LABEL_WIDTH)
        pLabel.pack(side = tk.LEFT, padx = PADX, pady = PADY)
        self.pEntry = Entry(pFrame, width = ENTRY_WIDTH, textvariable = self.password, show = "*")
        self.pEntry.pack(fill = tk.X, padx = PADX, pady = PADY, expand = True)

        # Error Row
        eFrame = Frame(self)
        eFrame.pack(fill = tk.X)
        eLabel = Label(eFrame, text = "", foreground = "red", font = error_font)
        eLabel.pack(side = tk.LEFT, anchor = "center", expand = True, padx = PADX, pady = PADY)

        # Sign in and Cancel Button Row
        bFrame = Frame(self)
        bFrame.pack(fill = tk.X)
        cButton = Button(bFrame, text = "Cancel", command = self.cancel)
        cButton.pack(side = tk.RIGHT, padx = PADX, pady = PADY, expand = False)
        sButton = Button(bFrame, text = "Sign in")
        sButton.pack(side = tk.RIGHT, padx = PADX, pady = PADY, expand = False)

        # Register Row
        rFrame = Frame(self)
        rFrame.pack(fill = tk.X)
        rButton = Button(rFrame, text = "Register", command = self._show_register)
        rButton.pack(side = tk.RIGHT, padx = PADX, pady = PADY, expand = False)
        rLabel = Label(rFrame, text = "Not a Member of ExchangeGram?")
        rLabel.pack(side = tk.RIGHT, padx = PADX, pady = PADY)

    def cancel(self):
        self.username.set("")
        self.password.set("")
        self.uEntry.focus()

    def _show_register(self):
        if self.show_register is not None: self.show_register()
        else: pass