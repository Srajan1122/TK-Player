import tkinter as tk
from PIL import Image, ImageTk


class LikeButton(tk.Button):
    def __init__(self, master, *args, **kwargs):
        self.title = kwargs.pop('title')
        self.album = kwargs.pop('album')
        self.url = kwargs.pop('url')
        self.artist = kwargs.pop('artist')
        tk.Button.__init__(self, master, *args, **kwargs)

        self.liked = True

        self.empty_heart = self.prepare_image('empty_heart.png', 16)
        self.filled_heart = self.prepare_image('filled_heart.png', 16)

        self['background'] = '#181818'
        self['activebackground'] = '#333333'
        self['bd'] = 0
        self['image'] = self.empty_heart
        self['command'] = self.clicked

        from Base.listOfPage import likedSong
        for index, song in enumerate(likedSong):
            for key, value in song.items():
                if key == 'title' and value == self.title:
                    self['image'] = self.filled_heart

        self.bind('<Button-1>', self.master.master.click)

    def clicked(self):
        from Base.listOfPage import likedSong
        if not self.liked:
            # if unliked
            self['image'] = self.empty_heart
            self.liked = True
            for index, song in enumerate(likedSong):
                for key, value in song.items():
                    if key == 'title' and value == self.title:
                        likedSong.pop(index)
            return
        # if liked
        self['image'] = self.filled_heart
        self.liked = False
        likedSong.append({
            'title': self.title,
            'genre': self.album,
            'artist': self.artist,
            'location': self.url
        })


    @staticmethod
    def prepare_image(filename, size):
        icon = Image.open('images/'+filename)
        icon = icon.resize((size, size), Image.ANTIALIAS)
        icon = ImageTk.PhotoImage(icon)
        return icon
