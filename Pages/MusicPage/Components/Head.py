import tkinter as tk
from PIL import ImageTk, Image
from Pages.MusicPage.Components.TextFrame import TextFrame


class Head(tk.Frame):
    def __init__(self, master, image, text, data, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, *kwargs)
        self['background'] = 'black'
        self.photo = image
        self.count = 0

        self.image_frame = tk.Frame(self, bg='#000000')
        self.image_frame.bind('<Configure>', self.frame_size)

        self.text_frame = TextFrame(self, text, data)

        self.image_label = tk.Canvas(self.image_frame,
                                     bd=0,
                                     highlightthickness=0)
        self.image_label.grid(row=0,
                              column=0,
                              sticky='nsew', )
        self.image_label.bind('<Configure>', self.label_size)
        self.image_frame.grid_columnconfigure(0, weight=1)
        self.image_frame.grid_rowconfigure(0, weight=1)

        self.image_frame.grid(row=0, column=0, sticky='nsew', padx=(30, 0), pady=30)
        self.text_frame.grid(row=0, column=1, sticky='nsew', padx=(10, 0), pady=(30, 30))

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=10000)

    def frame_size(self, event):
        pass

    def label_size(self, event):
        if self.count == 0:
            width = int(round(event.width / 1.5))
            height = int(round(event.height / 2))

            self.photo = self.photo.resize((height, height),
                                           Image.ANTIALIAS)
            self.photo = ImageTk.PhotoImage(self.photo)
            self.image_label.config(width=width, height=height)

            self.image_label.create_image(0, 0,
                                          image=self.photo,
                                          anchor=tk.NW,
                                          tags="IMG")
            self.image_label.configure(width=height)
            self.count = 1
