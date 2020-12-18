import tkinter as tk
from tkinter.ttk import Frame, Label, Entry, Button
from .theme import PADX, PADY, ENTRY_WIDTH, LABEL_WIDTH
from tkinter import font

class Register(Frame):
    def __init__(self, master):
        super().__init__(master=master)
        self.layout_components()
        # Setup Callbacks

    def layout_components(self):
        self.pack(fill = tk.BOTH, expand = False, padx = PADX, pady = PADY)
        error_font = font.Font(family = "Times New Roman", size = 8)

        # Variables
        self.username = tk.StringVar()
        self.username.set("")

        self.email = tk.StringVar()
        self.email.set("")

        self.password = tk.StringVar()
        self.password.set("")

        self.passcnfm = tk.StringVar()
        self.passcnfm.set("")

        # Email Row
        eFrame = Frame(self)
        eFrame.pack(fill = tk.X)
        eLabel = Label(eFrame, text = "Email:", width = LABEL_WIDTH)
        eLabel.pack(side = tk.LEFT, padx = PADX, pady = PADY)
        self.eEntry = Entry(eFrame, width = ENTRY_WIDTH, textvariable = self.email)
        self.eEntry.pack(fill = tk.X, padx = PADX, pady = PADY, expand = True)
        # Email Error Row
        e_eFrame = Frame(self)
        e_eFrame.pack(fill = tk.X)
        e_eLabel = Label(e_eFrame, text = "", foreground = "red", font = error_font)
        e_eLabel.pack(side = tk.LEFT, anchor = "center", expand = True, padx = PADX, pady = PADY)

        # Username Row
        uFrame = Frame(self)
        uFrame.pack(fill = tk.X)
        uLabel = Label(uFrame, text = "Username:", width = LABEL_WIDTH)
        uLabel.pack(side = tk.LEFT, padx = PADX, pady = PADY)
        self.uEntry = Entry(uFrame, width = ENTRY_WIDTH, textvariable = self.username)
        self.uEntry.pack(fill = tk.X, padx = PADX, pady = PADY, expand = True)
        # Username Error Row
        u_eFrame = Frame(self)
        u_eFrame.pack(fill = tk.X)
        u_eLabel = Label(u_eFrame, text = "", foreground = "red", font = error_font)
        u_eLabel.pack(side = tk.LEFT, anchor = "center", expand = True, padx = PADX, pady = PADY)

        # Original Password Row
        p_oFrame = Frame(self)
        p_oFrame.pack(fill = tk.X)
        p_oLabel = Label(p_oFrame, text = "Password:", width = LABEL_WIDTH)
        p_oLabel.pack(side = tk.LEFT, padx = PADX, pady = PADY)
        self.p_oEntry = Entry(p_oFrame, width = ENTRY_WIDTH, textvariable = self.password, show = "*")
        self.p_oEntry.pack(fill = tk.X, padx = PADX, pady = PADY, expand = True)
        # Confirming Password Row
        p_cFrame = Frame(self)
        p_cFrame.pack(fill = tk.X)
        p_cLabel = Label(p_cFrame, text = "Confirm:", width = LABEL_WIDTH)
        p_cLabel.pack(side = tk.LEFT, padx = PADX, pady = PADY)
        self.p_cEntry = Entry(p_cFrame, width = ENTRY_WIDTH, textvariable = self.passcnfm, show = "*")
        self.p_cEntry.pack(fill = tk.X, padx = PADX, pady = PADY, expand = True)
        # Password Error Row
        p_eFrame = Frame(self)
        p_eFrame.pack(fill = tk.X)
        p_eLabel = Label(p_eFrame, text = "", foreground = "red", font = error_font)
        p_eLabel.pack(side = tk.LEFT, anchor = "center", expand = True, padx = PADX, pady = PADY)

        # Sign in and Cancel Button Row
        bFrame = Frame(self)
        bFrame.pack(fill = tk.X)
        cButton = Button(bFrame, text = "Cancel", command = self.cancel)
        cButton.pack(side = tk.RIGHT, padx = PADX, pady = PADY, expand = False)
        sButton = Button(bFrame, text = "Sign in")
        sButton.pack(side = tk.RIGHT, padx = PADX, pady = PADY, expand = False)

    def cancel(self):
        self.email.set("")
        self.username.set("")
        self.password.set("")
        self.passcnfm.set("")
        self.eEntry.focus()
