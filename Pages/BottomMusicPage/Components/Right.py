import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
from PIL import Image, ImageTk


class Right(tk.Frame):
    count = 0
    flag = 0

    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self['bg'] = '#000000'
        self['width'] = 300

        style = ThemedStyle(self)

        custom_name = 'custom' + str(Right.count) + '.Horizontal.Scale'

        self.trough = Image.open('images/green_trough.png')
        self.trough = self.trough.resize((8, 4), Image.ANTIALIAS)
        self.trough = ImageTk.PhotoImage(self.trough)

        self.circle = Image.open('images/circle.png')
        self.circle = self.circle.resize((20, 20), Image.ANTIALIAS)
        self.circle = ImageTk.PhotoImage(self.circle)

        style.element_create(custom_name+'.trough', 'image', self.trough)
        style.element_create(custom_name + '.slider', 'image', self.circle)

        style.layout('custom.Horizontal.TScale',
                     [(custom_name+'.trough', {'sticky': 'ew'}),
                      (custom_name+'.slider',
                       {'side': 'left', 'sticky': '',
                        'children': [('Horizontal.Scale.label', {'sticky': ''})]
                        })])

        style.theme_settings("vista", {
            "custom.Horizontal.TScale": {
                'map':
                    {'background': [("active", "#000000"),
                                    ("!disabled", "#000000")],
                     }
            }})

        self.volume_icon = self.prepare_image('volume_icon2.png', 20)
        self.mute_icon = self.prepare_image('mute_icon.png', 20)

        self.volume_button = tk.Button(self,
                                       image=self.volume_icon,
                                       background='#000000',
                                       activebackground='#000000',
                                       bd=0,
                                       relief=tk.FLAT,
                                       width=20,
                                       height=20,
                                       padx=0,
                                       pady=0,
                                       command=self.click
                                       )
        self.volume_button.grid(row=0, column=1, padx=(0, 2))

        self.volume = tk.DoubleVar()
        self.volume.set(70)
        self.volumeSlider = ttk.Scale(self,
                                      to=100,
                                      orient=tk.HORIZONTAL,
                                      length=1,
                                      variable=self.volume,
                                      command=self.UpdateVolume,
                                      style='custom.Horizontal.TScale')

        self.volumeSlider.grid(row=0, column=2, sticky='nsew', padx=(0, 15))

        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_propagate(False)

        Right.count += 1

    def UpdateVolume(self, value):
        from Base.listOfPage import currentTrack
        percentValue = float(value) / 100
        currentTrack[0]['instance'].player.music.set_volume(percentValue)

    @staticmethod
    def prepare_image(filename, size):
        icon = Image.open('images/' + filename)
        icon = icon.resize((size, size), Image.ANTIALIAS)
        icon = ImageTk.PhotoImage(icon)
        return icon

    def click(self):
        if self.flag == 0:
            self.volume_button.config(image=self.mute_icon)
            self.flag = 1
        else:
            self.volume_button.config(image=self.volume_icon)
            self.flag = 0
