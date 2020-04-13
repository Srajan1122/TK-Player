import tkinter as tk
from Pages.Resource.ScrollableFrame import ScrollableFrame
from Pages.HomePage.Components.HorizontalFrame import HorizontalFrame
import pyglet
import tkinter.font as tkfont


class Home(tk.Frame):
    def __init__(self, master, controller, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self['background'] = '#181818'
        pyglet.font.add_file('fonts/Play/Play-Bold.ttf')
        play = tkfont.Font(family="Play", size=16, weight="bold")
        self.Ed_sheeran = tk.PhotoImage(file='images/edsheeran.png')
        self.taylor_swift = tk.PhotoImage(file='images/taylor.png')
        self.playlist = tk.PhotoImage(file='images/playlist.png')

        self.head = tk.Frame(self, bg='#181818')
        self.label = tk.Label(self.head, text='Home', background='#181818', fg='white',font=play)
        self.label.grid(row=0, column=0, stick=tk.N+tk.W)
        self.main = tk.Frame(self, bg='#181818')

        self.scrollable = ScrollableFrame(self.main)
        self.recentlyPlayedFrame = HorizontalFrame(self.scrollable.scrollable_frame,
                                                   text='Recently played',
                                                   content=self.recentlyPLayedContent(),
                                                   row=0)

        self.head.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
        self.main.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

        self.main.grid_rowconfigure(0, weight=1)
        self.main.grid_columnconfigure(0, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=10)
        self.grid_columnconfigure(0, weight=1)

    def recentlyPLayedContent(self):

        recently_played_dict = [
            {'text': 'Ed Sheeran', 'image': self.Ed_sheeran},
            {'text': 'Taylor Swift', 'image': self.taylor_swift},
            {'text': 'Your Playlist 1', 'image': self.playlist},
        ]
        return recently_played_dict
