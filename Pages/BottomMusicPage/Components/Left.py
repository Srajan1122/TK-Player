import tkinter as tk
from PIL import ImageTk, Image
import tkinter.font as tkfont


class Left(tk.Frame):
    def __init__(self, master, title, artist, image, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self['bg'] = '#2c2c2c'

        self.titleFont = tkfont.Font(family="Pragatic Narrow", size=10, weight="bold")
        self.artistFont = tkfont.Font(family="Pragatic Narrow", size=8, weight="bold")

        self.imageFrame = tk.Frame(self)
        self.textFrame = tk.Frame(self, width=250)

        self.image = image.resize((50, 50), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(self.image)
        self.imageLabel = tk.Label(self.imageFrame,
                                   image=self.image,
                                   background='#2c2c2c')

        self.imageLabel.grid(row=0, column=0, sticky='nsew')

        self.label = tk.Label(self.textFrame,
                              text=title,
                              font=self.titleFont,
                              foreground='#ffffff',
                              bg='#2c2c2c',
                              anchor=tk.SW
                              )
        self.artistLabel = tk.Label(self.textFrame,
                                    text=artist,
                                    font=self.artistFont,
                                    foreground='#dddddd',
                                    bg='#2c2c2c',
                                    anchor=tk.NW
                                    )

        self.label.grid(row=0, column=0, sticky='nsew')
        self.artistLabel.grid(row=1, column=0, sticky='nsew')

        self.imageFrame.grid(row=0, column=0, sticky='nsew', padx=(5, 0), pady=5)
        self.textFrame.grid(row=0, column=1, sticky='nsew', pady=5)
        self.textFrame.grid_propagate(False)

        self.imageFrame.grid_rowconfigure(0, weight=1)
        self.imageFrame.grid_columnconfigure(0, weight=1)

        self.textFrame.grid_rowconfigure((0, 1), weight=1)
        self.textFrame.grid_columnconfigure(0, weight=1)

        self.grid_rowconfigure(0, weight=1)
