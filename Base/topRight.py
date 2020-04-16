import tkinter as tk
from .topRightTop import TopRightTop
from .topRightBottom import TopRightBottom


class TopRight(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self['background'] = 'purple'

        self.topRightTop = TopRightTop(self)
        self.topRightBottom = TopRightBottom(self)

        self.topRightTop.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W + tk.E)
        self.topRightBottom.grid(row=1, column=0, sticky=tk.N + tk.S + tk.W + tk.E)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=13)
        self.grid_columnconfigure(0, weight=1)
