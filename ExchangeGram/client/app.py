import tkinter as tk
from tkinter.ttk import Frame
from client.view.sign_in import SignInView
from client.view.register import Register
from client.view.feed_view import FeedView


class Application(Frame):
    def __init__(self, master) -> None:
        super().__init__(master=master)
        self.master = master
        self.pack()
        self.initialize_view()

    def initialize_view(self):
        # Initialize Register Page
        self.register = Register(self)
        self.register.show_sign_in = self.show_sign_in
        # Initialize Sign in Page
        self.sign_in_view = SignInView(self)
        self.sign_in_view.show_register = self.show_register
        # Initialize Feed Page
        self.feed_view = FeedView(self)
        # Show First Page: Sign in Page
        self.show_feed_view()

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


def start_client():
    root = tk.Tk()
    # root.geometry("600x480")
    # Geometry() sets the size of the window
    # Without this function, Tkinter automatically sets the size to optimal.
    app = Application(master=root)
    app.mainloop()
