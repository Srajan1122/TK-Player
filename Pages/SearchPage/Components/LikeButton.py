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
        f = open('user')
        x = f.readlines()[0]
        from Database.Database import get_all_liked_songs
        for index, song in enumerate(get_all_liked_songs(x)):
            for key, value in song.items():
                if key == 'title' and value == self.title:
                    self.liked = False
                    self['image'] = self.filled_heart

        # self.bind('<Button-1>', self.master.master.click)

    def clicked(self):
        f = open('user')
        x = f.readlines()[0]
        from Base.listOfPage import likedSong
        if not self.liked:
            # if unliked
            self['image'] = self.empty_heart
            self.liked = True
            # for index, song in enumerate(likedSong):
            #     for key, value in song.items():
            #         if key == 'title' and value == self.title:
            #             likedSong.pop(index)
            from Database.Database import delete_liked_song
            delete_liked_song(x , self.title)
                
            
            return
        # if liked
        self['image'] = self.filled_heart
        self.liked = False
        from Database.Database import add_liked_songs
        track_object = {
            'title': self.title,
            'genre': self.album,
            'artist': self.artist,
            'location': self.url
        }
        
        add_liked_songs(track_object,x)
        likedSong.append(track_object)


    @staticmethod
    def prepare_image(filename, size):
        icon = Image.open('images/'+filename)
        icon = icon.resize((size, size), Image.ANTIALIAS)
        icon = ImageTk.PhotoImage(icon)
        return icon
