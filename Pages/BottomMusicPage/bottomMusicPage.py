import tkinter as tk
from .Components.Left import Left
from .Components.Middle import Middle
from .Components.Right import Right


class BottomMusicPage(tk.Frame):
    def __init__(self, master, controller, title, artist, image, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self['background'] = '#2c2c2c'
        self['height'] = 1

        self.left = Left(self, title, artist, image)
        self.right = Right(self)
        self.middle = Middle(self, controller)

        self.left.grid(row=0, column=0, sticky='nsew')
        self.middle.grid(row=0, column=1, sticky='nsew')
        self.right.grid(row=0, column=2, sticky='nsew')

        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=8)
        self.grid_columnconfigure(2, weight=3)
        self.grid_rowconfigure(0, weight=1)
        self.grid_propagate(False)

