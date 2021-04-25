import tkinter as tk
from common.util import validate_email
from tkinter.ttk import Frame, Label, Entry, Button
from .theme import PADX, PADY, ENTRY_WIDTH, LABEL_WIDTH
from tkinter import font
import client


class Register(Frame):
    def __init__(self, master):
        super().__init__(master=master)
        self.layout_components()
        # Setup Callbacks
        self.show_sign_in: Callable = None
        self.sign_in: Callable = None
        self.search_email: Callable = None
        self.search_username: Callable = None
        self.search_password: Callable = None
        self.register: Callable = None

        self.username_valid: bool = False
        self.email_valid: bool = False
        self.password_valid: bool = False
        self.passcnfm_valid: bool = False
        # Refocus to Email Entry
        self.email_Entry.focus()

    def layout_components(self):
        self.pack(fill=tk.BOTH, expand=False, padx=PADX, pady=PADY)
        error_font = font.Font(family="Ariel", size=8)

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
        email_Frame = Frame(self)
        email_Frame.pack(fill=tk.X)
        email_Label = Label(email_Frame, text="Email:", width=LABEL_WIDTH)
        email_Label.pack(side=tk.LEFT, padx=PADX, pady=PADY)
        self.email_Entry = Entry(
            email_Frame, width=ENTRY_WIDTH, textvariable=self.email
        )
        self.email_Entry.pack(fill=tk.X, padx=PADX, pady=PADY, expand=True)
        self.email_Entry.bind("<FocusOut>", self._validate_email)
        # Email Error Row
        email_errFrame = Frame(self)
        email_errFrame.pack(fill=tk.X)
        self.email_errLabel = Label(
            email_errFrame, text="", foreground="red", font=error_font
        )
        self.email_errLabel.pack(
            side=tk.LEFT, anchor="center", expand=True, padx=PADX, pady=PADY
        )

        # Username Row
        user_Frame = Frame(self)
        user_Frame.pack(fill=tk.X)
        user_Label = Label(user_Frame, text="Username:", width=LABEL_WIDTH)
        user_Label.pack(side=tk.LEFT, padx=PADX, pady=PADY)
        self.user_Entry = Entry(
            user_Frame, width=ENTRY_WIDTH, textvariable=self.username
        )
        self.user_Entry.pack(fill=tk.X, padx=PADX, pady=PADY, expand=True)
        self.user_Entry.bind("<FocusOut>", self._validate_username)

        # Username Error Row
        user_errFrame = Frame(self)
        user_errFrame.pack(fill=tk.X)
        self.user_errLabel = Label(
            user_errFrame, text="", foreground="red", font=error_font
        )
        self.user_errLabel.pack(
            side=tk.LEFT, anchor="center", expand=True, padx=PADX, pady=PADY
        )

        # Original Password Row
        pass_Frame = Frame(self)
        pass_Frame.pack(fill=tk.X)
        pass_Label = Label(pass_Frame, text="Password:", width=LABEL_WIDTH)
        pass_Label.pack(side=tk.LEFT, padx=PADX, pady=PADY)
        self.pass_Entry = Entry(
            pass_Frame, width=ENTRY_WIDTH, textvariable=self.password, show="*"
        )
        self.pass_Entry.pack(fill=tk.X, padx=PADX, pady=PADY, expand=True)
        self.pass_Entry.bind("<FocusOut>", self._validate_password)
        # Confirming Password Row
        pass_cnfmFrame = Frame(self)
        pass_cnfmFrame.pack(fill=tk.X)
        pass_cnfmLabel = Label(pass_cnfmFrame, text="Confirm:", width=LABEL_WIDTH)
        pass_cnfmLabel.pack(side=tk.LEFT, padx=PADX, pady=PADY)
        self.pass_cnfmEntry = Entry(
            pass_cnfmFrame, width=ENTRY_WIDTH, textvariable=self.passcnfm, show="*"
        )
        self.pass_cnfmEntry.pack(fill=tk.X, padx=PADX, pady=PADY, expand=True)
        self.pass_cnfmEntry.bind("<FocusOut>", self._validate_password)
        # Password Error Row
        pass_errFrame = Frame(self)
        pass_errFrame.pack(fill=tk.X)
        self.pass_errLabel = Label(
            pass_errFrame, text="", foreground="red", font=error_font
        )
        self.pass_errLabel.pack(
            side=tk.LEFT, anchor="center", expand=True, padx=PADX, pady=PADY
        )

        # Button Row
        button_Frame = Frame(self)
        button_Frame.pack(fill=tk.X)
        # Cancel Button
        cncl_Button = Button(button_Frame, text="Cancel", command=self.cancel)
        cncl_Button.pack(side=tk.RIGHT, padx=PADX, pady=PADY, expand=False)
        # Register Button
        self.register_Button = Button(
            button_Frame, text="Register", state="disabled", command=self._register
        )
        self.register_Button.pack(side=tk.RIGHT, padx=PADX, pady=PADY, expand=False)
        # View Password Button
        self.view_pass_Button = Button(
            button_Frame, text="View Password", command=self.view_password
        )
        self.view_pass_Button.pack(side=tk.LEFT, padx=PADX, pady=PADY)

        # Go Back Button Row
        gbck_Frame = Frame(self)
        gbck_Frame.pack(fill=tk.X)
        gbck_Label = Label(gbck_Frame, text="Have an Account? Go Ahead and ")
        gbck_Label.pack(side=tk.LEFT, padx=PADX, pady=PADY, expand=False)
        gbck_Button = Button(gbck_Frame, text="Sign In", command=self._show_sign_in)
        gbck_Button.pack(side=tk.RIGHT, padx=PADX, pady=PADY, expand=False)

    def cancel(self):
        self.email.set("")
        self.username.set("")
        self.password.set("")
        self.passcnfm.set("")
        self.email_Entry.focus()
        self.email_errLabel.configure(text="")
        self.user_errLabel.configure(text="")
        self.pass_errLabel.configure(text="")

    def view_password(self):
        self.pass_Entry.configure(show="")
        self.pass_cnfmEntry.configure(show="")
        self.view_pass_Button.configure(
            text="Hide Password", command=self.hide_password
        )

    def hide_password(self):
        self.pass_Entry.configure(show="*")
        self.pass_cnfmEntry.configure(show="*")
        self.view_pass_Button.configure(
            text="View Passwrod", command=self.view_password
        )

    def _show_sign_in(self):
        if self.show_sign_in is not None:
            self.show_sign_in()
            self.cancel()

    def _register(self):
        if self.register is not None:
            self.register()
            self.cancel()

    def _validate_email(self, event):
        email = self.email.get()
        if len(email) == 0:
            self.email_errLabel.configure(text="Email Must not be Empty...")
            self.email_valid = False
        elif not validate_email(email):
            self.email_errLabel.configure(text="Email Format Invalide...")
            self.email_valid = False
        elif self.search_email is not None and not self.search_email(email):
            self.email_errLabel.configure(text="Email Already Registered...")
            self.email_valid = False
        else:
            self.email_errLabel.configure(text="")
            self.email_valid = True
        self.enable_register()

    def _validate_username(self, event):
        username = self.username.get()
        if len(username) == 0:
            self.user_errLabel.configure(text="Username Must not be Empty...")
            self.username_valid = False
        elif self.search_username is not None and not self.search_username(username):
            self.username_valid = False
        else:
            self.user_errLabel.configure(text="")
            self.username_valid = True
        self.enable_register()

    def _validate_password(self, event):
        password = self.password.get()
        passcnfm = self.passcnfm.get()
        if len(password) == 0:
            self.pass_errLabel.configure(text="Password Must Not be Empty...")
            self.password_valid = False
        elif len(password) < 8:
            self.pass_errLabel.configure(
                text="Password Must be Longer than 8 Characters..."
            )
            self.password_valid = False
        elif password != passcnfm:
            self.pass_errLabel.configure(text="Password Must Match...   ")
            self.passcnfm_valid = False
        elif self.search_password is not None and not self.search_password(password):
            self.pass_errLabel.configure(text="")
            self.password_valid = False
        else:
            self.pass_errLabel.configure(text="")
            self.passcnfm_valid = True
            self.password_valid = True
        self.enable_register()

    def enable_register(self):
        if (
            self.email_valid
            and self.username_valid
            and self.password_valid
            and self.passcnfm_valid
        ):
            self.register_Button.configure(state="normal")