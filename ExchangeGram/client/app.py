import tkinter as tk
from tkinter.ttk import Frame
from client.view.sign_in import SignInView
from client.view.register import Register
from client.view.feed_view import FeedView
from common.database.database_abstraction_layer import Dbal


class Application(Frame):
    def __init__(self, master, dbal: Dbal) -> None:
        super().__init__(master=master)
        self.master = master
        self.dbal = dbal
        self.pack()
        self.user = None
        self.initialize_view()

    def initialize_view(self):
        # Initialize Register Page
        self.register = Register(self)
        self.register.register = self._register
        self.register.show_sign_in = self.show_sign_in
        # Initialize Sign in Page
        self.sign_in_view = SignInView(self)
        self.sign_in_view.sign_in = self._sign_in
        self.sign_in_view.show_register = self.show_register
        # Initialize Feed Page
        self.feed_view = FeedView(self)
        self.feed_view.sign_out = self._sign_out
        # Show First Page: Sign in Page
        self.show_sign_in()

    def pack_forget_all(self):
        # Pack Forgetting all Pages Initialized
        self.sign_in_view.pack_forget()
        self.register.pack_forget()
        self.feed_view.pack_forget()

    def show_sign_in(self):
        self.winfo_toplevel().title("Sign In")
        self.pack_forget_all()
        self.sign_in_view.pack()

    def show_register(self):
        self.winfo_toplevel().title("Register")
        self.pack_forget_all()
        self.register.pack()

    def show_feed_view(self):
        self.winfo_toplevel().title("Feed Page")
        self.pack_forget_all()
        self.feed_view.pack()

    def _register(self):
        self.user = self.dbal.register(
            username=self.register.username.get(),
            email=self.register.email.get(),
            password=self.register.password.get(),
        )
        if self.user is not None:
            self.show_feed_view()
            self.register.cancel()
        else:
            self.register.failed_register()

    def _sign_in(self):
        self.user = self.dbal.authenticate(
            username=self.sign_in_view.username.get(),
            password=self.sign_in_view.password.get(),
        )
        if self.user is not None:
            self.show_feed_view()
            self.sign_in_view.cancel()
        else:
            self.sign_in_view.failed_sign_in()

    def _sign_out(self):
        self.user = None
        self.show_sign_in()


def start_client(dbal: Dbal):
    root = tk.Tk()
    # root.geometry("600x480")
    # Geometry() sets the size of the window
    # Without this function, Tkinter automatically sets the size to optimal.
    app = Application(master=root, dbal=dbal)
    app.mainloop()
