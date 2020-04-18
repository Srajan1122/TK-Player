import tkinter as tk

import pyglet
from PIL import ImageTk, Image
import tkinter.font as tkfont


class Head(tk.Frame):
    def __init__(self, master, image, text, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, *kwargs)
        self['background'] = 'black'
        self.photo = image
        self.count = 0

        self.image_frame = tk.Frame(self, bg='#000000')
        self.image_frame.bind('<Configure>', self.frame_size)

        self.text_frame = TextFrame(self, text)

        self.image_label = tk.Canvas(self.image_frame,
                                     bd=0,
                                     highlightthickness=0)
        self.image_label.grid(row=0,
                              column=0,
                              sticky='nsew',)
        self.image_label.bind('<Configure>', self.label_size)
        self.image_frame.grid_columnconfigure(0, weight=1)
        self.image_frame.grid_rowconfigure(0, weight=1)

        self.image_frame.grid(row=0, column=0, sticky='nsew', padx=(50, 0), pady=30)
        self.text_frame.grid(row=0, column=1, sticky='nsew', padx=(10, 0), pady=30)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1000)

    def frame_size(self, event):
        pass

    def label_size(self, event):
        if self.count == 0:
            width = int(round(event.width/1.5))
            height = int(round(event.height/2))

            self.photo = self.photo.resize((width, height),
                                           Image.ANTIALIAS)
            self.photo = ImageTk.PhotoImage(self.photo)
            self.image_label.config(width=width, height=height)

            self.image_label.create_image(0, 0,
                                          image=self.photo,
                                          anchor=tk.NW,
                                          tags="IMG")
            self.count = 1


class TextFrame(tk.Frame):
    def __init__(self, master, text, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self['background'] = '#000000'

        pyglet.font.add_file('fonts/Play/Play-Bold.ttf')
        self.head = tkfont.Font(family="Pragatic Narrow", size=28, weight="bold")
        self.support = tkfont.Font(family="Play", size=10, weight="bold")

        self.text_heading = tk.Label(self,
                                     background='#000000',
                                     foreground='white',
                                     text=text,
                                     font=self.head,
                                     anchor=tk.W)
        self.text_support = tk.Label(self,
                                     bg='#000000',
                                     foreground='white',
                                     text='By Amplify.',
                                     font=self.support,
                                     anchor=tk.NW
                                     )
        self.button_region = tk.Frame(self, bg='#000000')

        self.play = tk.Button(self.button_region)
        self.play.grid(row=0, column=0, sticky='nsew')

        self.text_heading.grid(row=0, column=0, sticky='nsew')
        self.text_support.grid(row=1, column=0, sticky='nsew')
        # self.button_region.grid(row=2, column=0, sticky='nsew', padx=30)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

