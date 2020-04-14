import tkinter as tk
from Pages.Resource.VerticalScrollableFrame import ScrollableFrame
from .Components.header import Header
from .Components.HorizontalFrame import HorizontalFrame


class Home(tk.Frame):
    def __init__(self, master, controller, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self['background'] = '#181818'

        self.head = Header(self, text='Home')

        self.main = tk.Frame(self, bg='#181818')

        self.scrollable = ScrollableFrame(self.main)

        self.popular = HorizontalFrame(self.scrollable.scrollable_frame,
                                       text='Popular Playlist')

        self.popular2 = HorizontalFrame(self.scrollable.scrollable_frame,
                                       text='Popular Playlist')

        self.popular.grid(row=0, column=0, sticky=tk.N+tk.W+tk.E)
        self.popular2.grid(row=1, column=0, sticky=tk.N + tk.W + tk.E)

        self.head.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
        self.main.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

        self.main.grid_rowconfigure(0, weight=1)
        self.main.grid_columnconfigure(0, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=10)
        self.grid_columnconfigure(0, weight=1)

