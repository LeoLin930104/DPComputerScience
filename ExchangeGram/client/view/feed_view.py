import tkinter as tk
from client.view.scrollable_frame import ScrollableFrame
from tkinter.ttk import Frame, Label, Button, Style
from typing import Callable
from client.view.theme import PADX, PADY


class FeedView(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.layout_components()

    def layout_components(self):
        self.pack(fill=tk.BOTH, expand=True, padx=PADX, pady=PADY)

        topFrame = Frame(self)
        topFrame.grid(columnspan=2, row=1, sticky=tk.N + tk.W + tk.E)

        home_Button = Button(topFrame, text="Home")
        home_Button.grid(padx=PADX, pady=PADY, column=1, row=1, sticky=tk.N + tk.W)

        feed_Button = Button(topFrame, text="Feed")
        feed_Button.grid(padx=PADX, pady=PADY, column=2, row=1, sticky=tk.W)

        # Testing
        style = Style()
        style.configure("a.TFrame", background="red", foreground="white")

        leftFrame = Frame(self)
        leftFrame.grid(column=1, sticky=tk.N + tk.W + tk.S)

        rightFrame = ScrollableFrame(self, style="a.TFrame")
        rightFrame.grid(column=2, sticky=tk.NSEW)
