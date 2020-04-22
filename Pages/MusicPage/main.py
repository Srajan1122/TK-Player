import tkinter as tk
from .Components.Head import Head
from .Components.Content.Content import Content
from .Components.FilterFrame import FilterFrame
from .Components.TitleFrame import TitleFrame


class Main(tk.Frame):
    flag = 0

    def __init__(self, master, *args, **kwargs):
        self.data = kwargs.pop('data')
        self.image = kwargs.pop('image')
        self.text = kwargs.pop('text')
        tk.Frame.__init__(self, master, *args, **kwargs)
        self['background'] = '#000000'

        self.bind('<Configure>', self.size)

        self.head = Head(self, image=self.image, text=self.text, data=self.data)
        self.middle = tk.Frame(self, bg='#181818')
        self.filter_frame = FilterFrame(self.middle, data=self.data)
        self.title_frame = TitleFrame(self.middle)
        self.line_frame = tk.Frame(self.middle, bg='#333333')
        self.content = Content(self, data=self.data)

        self.head.grid(row=0, column=0, sticky='nsew')
        self.middle.grid(row=1, column=0, sticky='nsew')
        self.filter_frame.grid(row=0, column=0, sticky='nsew', padx=30, pady=(10, 0))
        self.title_frame.grid(row=1, column=0, sticky='nsew', padx=30)
        self.line_frame.grid(row=2, column=0, sticky='nsew', padx=30)
        self.content.grid(row=3, column=0, sticky='nsew')

        self.middle.grid_columnconfigure(0, weight=1)
        self.middle.grid_rowconfigure((0, 1), weight=1)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1000)
        self.grid_propagate(False)

    def size(self, event):
        if Main.flag == 0:
            self.config(width=event.width)
            Main.flag = 1
