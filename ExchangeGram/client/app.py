import tkinter as tk
from tkinter.ttk import Frame
from .view.sign_in import SignInView

class Application(Frame):
    def __init__(self, master) -> None:
        super().__init__(master=master)
        self.master = master
        self.pack()
        self.initialize_view()

    def initialize_view(self):
        self.winfo_toplevel().title("ExchangeGram")
        self.sign_ing_view = SignInView(self)

def start_client():
    root = tk.Tk()
    root.geometry("600x480")
    app = Application( master = root )
    app.mainloop()
