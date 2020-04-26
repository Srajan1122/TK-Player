import tkinter as tk
import tkinter.font as tkfont


class ContentLabel(tk.Label):
    def __init__(self, master, *args, **kwargs):
        tk.Label.__init__(self, master, *args, **kwargs)

        self.font = tkfont.Font(family="Roboto", size=10, weight='bold')

        self['height'] = 40,
        self['bg'] = '#181818',
        self['foreground'] = '#888888',
        self['anchor'] = tk.W
        self['font'] = self.font

        # self.bind('<Button-1>', self.master.master.click)
        # self.bind('<Double-Button-1>', self.master.master.double_click)
