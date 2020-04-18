import tkinter as tk
from Pages.Resource.VerticalScrollableFrame import ScrollableFrame
from .Components.header import Header
from .Components.HorizontalFrame import HorizontalFrame


class Home(tk.Frame):
    def __init__(self, master, controller, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self['background'] = '#181818'
        self.bind('<Configure>', self.size)
        self.main = tk.Frame(self, bg='#181818')
        self.scrollable = ScrollableFrame(self.main)

        self.head = Header(self, text='Home')

        for i, j in enumerate(self.data()):
            self.item = HorizontalFrame(self.scrollable.scrollable_frame,
                                        controller,
                                        text=j['title'], data=j['data'])
            self.item.grid(row=i, column=0, sticky=tk.N + tk.W + tk.E)

        self.head.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.main.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

        self.main.grid_rowconfigure(0, weight=1)
        self.main.grid_columnconfigure(0, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=10)
        self.grid_columnconfigure(0, weight=1)

    def data(self):
        from Database import HomePagedata
        title = ['Listen to your favourite Artist', 'Get your mood on']
        data = [
            HomePagedata.artist_data, HomePagedata.genre_data
        ]
        info = [
            {'title': title[0], 'data': data[0]},
            {'title': title[1], 'data': data[1]}
        ]

        return info

    def size(self, event):
        pass
