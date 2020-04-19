import tkinter as tk
import pyglet
from PIL import ImageTk, Image
import tkinter.font as tkfont


class TextFrame(tk.Frame):
    def __init__(self, master, text, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self['background'] = '#000000'

        pyglet.font.add_file('fonts/Play/Play-Bold.ttf')
        self.head = tkfont.Font(family="Pragatic Narrow", size=28, weight="bold")
        self.support = tkfont.Font(family="Play", size=10, weight="bold")
        #
        self.button_heart_raw = Image.open('images/button_heart.png')
        self.button_heart = self.button_heart_raw.resize((35, 35), Image.ANTIALIAS)
        self.button_heart_active = self.button_heart_raw.resize((37, 37), Image.ANTIALIAS)
        self.button_heart = ImageTk.PhotoImage(self.button_heart)
        self.button_heart_active = ImageTk.PhotoImage(self.button_heart_active)

        self.button_liked_raw = Image.open('images/love_filled.png')
        self.button_liked = self.button_liked_raw.resize((35, 35), Image.ANTIALIAS)
        self.button_liked_active = self.button_liked_raw.resize((37, 37), Image.ANTIALIAS)
        self.button_liked = ImageTk.PhotoImage(self.button_liked)
        self.button_liked_active = ImageTk.PhotoImage(self.button_liked_active)

        self.music_menu_button_raw = Image.open('images/music_menu_button.png')
        self.music_menu_button = self.music_menu_button_raw.resize((33, 33), Image.ANTIALIAS)
        self.music_menu_button_active = self.music_menu_button_raw.resize((35, 35), Image.ANTIALIAS)
        self.music_menu_button = ImageTk.PhotoImage(self.music_menu_button)
        self.music_menu_button_active = ImageTk.PhotoImage(self.music_menu_button_active)

        self.play_raw = Image.open('images/play.png')
        self.play = self.play_raw.resize((100, 35), Image.ANTIALIAS)
        self.play_active = self.play_raw.resize((103, 38), Image.ANTIALIAS)
        self.play = ImageTk.PhotoImage(self.play)
        self.play_active = ImageTk.PhotoImage(self.play_active)

        # self.menu_button_image = tk.PhotoImage(file=r'images/button_heart.png')

        self.text_heading = tk.Label(self,
                                     background='#000000',
                                     foreground='white',
                                     text=text,
                                     font=self.head,
                                     anchor=tk.SW,
                                     padx=0,
                                     pady=0)
        self.text_support = tk.Label(self,
                                     bg='#000000',
                                     foreground='white',
                                     text='By Amplify.',
                                     font=self.support,
                                     anchor=tk.NW
                                     )
        self.button_region = tk.Frame(self, bg='#000000', height=38)

        self.play_button = HeadIcon(self.button_region,
                                    image=self.play,
                                    active_image=self.play_active,
                                    width=105, )

        self.like_button = HeadIcon(self.button_region,
                                    image=self.button_heart,
                                    active_image=self.button_heart_active,
                                    width=39,
                                    command=self.liked)
        self.liked_button = HeadIcon(self.button_region,
                                     image=self.button_liked,
                                     active_image=self.button_liked_active,
                                     width=39,
                                     command=self.unliked)
        self.menu_button = HeadIcon(self.button_region,
                                    image=self.music_menu_button,
                                    active_image=self.music_menu_button_active,
                                    width=37)

        self.play_button.grid(row=0, column=0, sticky='nsew')
        self.like_button.grid(row=0, column=1, sticky='nsew', padx=(0, 5))
        self.liked_button.grid(row=0, column=1, sticky='nsew', padx=(0, 5))
        self.menu_button.grid(row=0, column=2, sticky='nsew')

        self.like_button.tkraise()

        self.button_region.grid_rowconfigure(0, weight=1)
        self.button_region.grid_propagate(False)

        self.text_heading.grid(row=0, column=0, sticky='nsew')
        self.text_support.grid(row=1, column=0, sticky='nsew')
        self.button_region.grid(row=2, column=0, sticky='nsew')

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_propagate(False)

    def liked(self):
        self.liked_button.tkraise()

    def unliked(self):
        self.like_button.tkraise()


class HeadIcon(tk.Button):
    def __init__(self, master, image, active_image, *args, **kwargs):
        tk.Button.__init__(self, master, *args, **kwargs)
        self['background'] = '#000000'
        self['activebackground'] = '#000000'
        self['bd'] = 0
        self['image'] = image

        self.active_image = active_image
        self.image = image

        self.bind('<Enter>', self.enter)
        self.bind('<Leave>', self.leave)

        self.grid_propagate(False)

    def enter(self, event):
        self.config(image=self.active_image)

    def leave(self, event):
        self.config(image=self.image)
