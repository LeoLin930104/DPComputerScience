import tkinter as tk
from tkinter.ttk import Frame
from client.view.sign_in import SignInView
from client.view.register import Register

class Application(Frame):
    def __init__(self, master) -> None:
        super().__init__(master=master)
        self.master = master
        self.pack()
        self.initialize_view()

    def initialize_view(self):
        self.winfo_toplevel().title("ExchangeGram")
        self.register = Register(self)
        self.register.pack_forget()
        self.sign_in_view = SignInView(self)
        self.sign_in_view.show_register = self.show_register

    def show_register(self):
        self.sign_in_view.pack_forget()
        self.register.pack()

def start_client():
    root = tk.Tk()
    # root.geometry("600x480")
    # Geometry() sets the size of the window
    # Without this function, Tkinter automatically sets the size to optimal.
    app = Application( master = root )
    app.mainloop()
