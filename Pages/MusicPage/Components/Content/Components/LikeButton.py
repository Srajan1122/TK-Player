import tkinter as tk
from PIL import Image, ImageTk


class LikeButton(tk.Button):
    def __init__(self, master, *args, **kwargs):
        tk.Button.__init__(self, master, *args, **kwargs)

        self.liked = True

        self.empty_heart = self.prepare_image('empty_heart.png', 16)
        self.filled_heart = self.prepare_image('filled_heart.png', 16)

        self['background'] = '#181818'
        self['activebackground'] = '#333333'
        self['bd'] = 0
        self['image'] = self.empty_heart
        self['command'] = self.clicked

        self.bind('<Button-1>', self.master.master.click)

    def clicked(self):
        if not self.liked:
            # if unliked
            self['image'] = self.empty_heart
            self.liked = True
            return
        # if liked
        self['image'] = self.filled_heart
        self.liked = False

    @staticmethod
    def prepare_image(filename, size):
        icon = Image.open('images/'+filename)
        icon = icon.resize((size, size), Image.ANTIALIAS)
        icon = ImageTk.PhotoImage(icon)
        return icon
