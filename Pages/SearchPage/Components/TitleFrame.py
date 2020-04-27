import tkinter as tk
import tkinter.font as tkfont

title_size = 0
icon_size = 0
album_size = 0
artist_size = 0
menu_size = 0


class TitleFrame(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self['background'] = '#181818'
        self['height'] = 40

        self.iconFrame = tk.Frame(self, bg='#181818')
        self.titleFrame = tk.Frame(self, bg='#000000')
        self.artistFrame = tk.Frame(self, bg='#000000')
        self.albumFrame = tk.Frame(self, bg='#000000')
        self.menuFrame = tk.Frame(self,bg='#181818')

        self.iconFrame.grid(row=0, column=0, sticky='nsew')
        self.titleFrame.grid(row=0, column=1, sticky='nsew')
        self.artistFrame.grid(row=0, column=2, sticky='nsew')
        self.albumFrame.grid(row=0, column=3, sticky='nsew')
        self.menuFrame.grid(row=0, column=4, sticky='nsew')

        self.titleLabel = TitleLabel(self.titleFrame, text='TITLE')
        self.titleLabel.grid(row=0, column=0, sticky='nsew')
        self.titleFrame.grid_columnconfigure(0, weight=1)
        self.titleFrame.grid_rowconfigure(0, weight=1)

        self.artistLabel = TitleLabel(self.artistFrame, text='GENRE')
        self.artistLabel.grid(row=0, column=0, sticky='nsew')
        self.artistFrame.grid_columnconfigure(0, weight=1)
        self.artistFrame.grid_rowconfigure(0, weight=1)

        self.albumLabel = TitleLabel(self.albumFrame, text='ARTIST')
        self.albumLabel.grid(row=0, column=0, sticky='nsew')
        self.albumFrame.grid_columnconfigure(0, weight=1)
        self.albumFrame.grid_rowconfigure(0, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=10)
        self.grid_columnconfigure(2, weight=6)
        self.grid_columnconfigure(3, weight=6)
        self.grid_columnconfigure(4, weight=1)
        self.grid_propagate(False)

        self.iconFrame.bind('<Configure>', self.icon_size)
        self.titleFrame.bind('<Configure>', self.title_size)
        self.albumFrame.bind('<Configure>', self.album_size)
        self.artistFrame.bind('<Configure>', self.artist_size)
        self.menuFrame.bind('<Configure>', self.menu_size)

    def title_size(self, event):
        global title_size
        title_size = event.width

    def icon_size(self, event):
        global icon_size
        icon_size = event.width

    def album_size(self, event):
        global album_size
        album_size = event.width

    def artist_size(self, event):
        global artist_size
        artist_size = event.width

    def menu_size(self, event):
        global menu_size
        menu_size = event.width


class TitleLabel(tk.Label):
    def __init__(self, master, *args, **kwargs):
        tk.Label.__init__(self, master, *args, **kwargs)

        self.font = tkfont.Font(family="Roboto", size=9)

        self['height'] = 40,
        self['bg'] = '#181818',
        self['foreground'] = '#888888',
        self['anchor'] = tk.W
        self['font'] = self.font

        self.bind('<Enter>', self.enter)
        self.bind('<Leave>', self.leave)

    def enter(self, event):
        self.config(foreground='white')

    def leave(self, event):
        self.config(foreground='#888888')
