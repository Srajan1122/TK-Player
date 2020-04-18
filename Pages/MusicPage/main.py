import tkinter as tk
from .Components.Head import Head
from .Components.Content import Content


class Main(tk.Frame):
    flag = 0

    def __init__(self, master, *args, **kwargs):
        self.data = kwargs.pop('data')
        self.image = kwargs.pop('image')
        self.text = kwargs.pop('text')
        tk.Frame.__init__(self, master, *args, **kwargs)
        self['background'] = 'red'

        self.bind('<Configure>', self.size)

        self.head = Head(self, image=self.image, text=self.text)
        self.content = Content(self)

        self.head.grid(row=0, column=0, sticky='nsew')
        self.content.grid(row=1, column=0, sticky='nsew')

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1000)
        self.grid_propagate(False)

    def size(self, event):
        if Main.flag == 0:
            self.config(width=event.width)
            Main.flag = 1
