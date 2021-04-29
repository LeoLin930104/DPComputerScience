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
        self.user_Entry.focus()

    def layout_components(self):
        self.pack(fill=tk.BOTH, expand=False, padx=PADX, pady=PADY)
        error_font = font.Font(family="Ariel", size=8)

        # Variables
        self.username = tk.StringVar()
        self.username.set("")

        self.password = tk.StringVar()
        self.password.set("")

        # Username Row
        user_Frame = Frame(self)
        user_Frame.pack(fill=tk.X)
        user_Label = Label(user_Frame, text="Username:", width=LABEL_WIDTH)
        user_Label.pack(side=tk.LEFT, padx=PADX, pady=PADY)
        self.user_Entry = Entry(
            user_Frame, width=ENTRY_WIDTH, textvariable=self.username
        )
        self.user_Entry.bind("<FocusOut>", self.enable_sign_in)
        self.user_Entry.pack(fill=tk.X, padx=PADX, pady=PADY, expand=True)

        # Password Row
        pass_Frame = Frame(self)
        pass_Frame.pack(fill=tk.X)
        pass_Label = Label(pass_Frame, text="Password:", width=LABEL_WIDTH)
        pass_Label.pack(side=tk.LEFT, padx=PADX, pady=PADY)
        self.pass_Entry = Entry(
            pass_Frame, width=ENTRY_WIDTH, textvariable=self.password, show="*"
        )
        self.pass_Entry.bind("<FocusOut>", self.enable_sign_in)
        self.pass_Entry.pack(fill=tk.X, padx=PADX, pady=PADY, expand=True)

        # Error Row
        err_Frame = Frame(self)
        err_Frame.pack(fill=tk.X)
        self.err_Label = Label(err_Frame, text="", foreground="red", font=error_font)
        self.err_Label.pack(
            side=tk.LEFT, anchor="center", expand=True, padx=PADX, pady=PADY
        )

        # Button Row
        button_Frame = Frame(self)
        button_Frame.pack(fill=tk.X)
        # Cancel Button
        cncl_Button = Button(button_Frame, text="Cancel", command=self.cancel)
        cncl_Button.pack(side=tk.RIGHT, padx=PADX, pady=PADY, expand=False)
        # Sign in Button
        self.sgnn_Button = Button(
            button_Frame, text="Sign in", state="disabled", command=self._sign_in
        )
        self.sgnn_Button.pack(side=tk.RIGHT, padx=PADX, pady=PADY, expand=False)

        # Register Row
        register_Frame = Frame(self)
        register_Frame.pack(fill=tk.X)
        register_Button = Button(
            register_Frame, text="Register", command=self._show_register
        )
        register_Button.pack(side=tk.RIGHT, padx=PADX, pady=PADY, expand=False)
        register_Label = Label(register_Frame, text="Not a Member of ExchangeGram?")
        register_Label.pack(side=tk.RIGHT, padx=PADX, pady=PADY)

    def _sign_in(self):
        if self.sign_in is not None:
            self.sign_in()

    def enable_sign_in(self, event):
        if self.username.get() != "" and self.password.get() != "":
            self.sgnn_Button.configure(state="normal")
        else:
            self.sgnn_Button.configure(state="disabled")

    def failed_sign_in(self):
        self.err_Label.configure(text="Username/Password Incorrect")

    def cancel(self):
        self.username.set("")
        self.password.set("")
        self.user_Entry.focus()

    def _show_register(self):
        if self.show_register is not None:
            self.cancel()
            self.show_register()
        else:
            pass
