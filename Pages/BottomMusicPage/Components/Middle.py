import tkinter as tk
from ttkthemes import ThemedStyle
from tkinter import ttk
from PIL import ImageTk, Image


class Middle(tk.Frame):
    count = 100

    def __init__(self, master, controller, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self['bg'] = '#2c2c2c'

        self.upper = tk.Frame(self, bg='#2c2c2c')
        self.lower = tk.Frame(self, bg='#2c2c2c')

        self.pause_icon2 = self.prepare_image('pause_icon2.png', 30)
        self.play_icon2 = self.prepare_image('play_icon2.png', 30)
        self.repeat_icon = self.prepare_image('repeat_icon.png', 15)
        self.previous_icon = self.prepare_image('previous.png', 18)
        self.next_icon = self.prepare_image('next.png', 18)
        self.shuffle_icon = self.prepare_image('shuffle.png', 15)
        self.pause_icon3 = self.prepare_image('pause_icon2.png', 32)
        self.play_icon3 = self.prepare_image('play_icon2.png', 32)

        # ------------------------------------------------------
        style = ThemedStyle(self)

        custom_name = 'custom' + str(Middle.count) + '.Horizontal.Scale'

        self.trough = Image.open('images/green_trough.png')
        self.trough = self.trough.resize((8, 4), Image.ANTIALIAS)
        self.trough = ImageTk.PhotoImage(self.trough)

        self.circle = Image.open('images/circle.png')
        self.circle = self.circle.resize((20, 20), Image.ANTIALIAS)
        self.circle = ImageTk.PhotoImage(self.circle)

        style.element_create(custom_name + '.trough', 'image', self.trough)
        style.element_create(custom_name + '.slider', 'image', self.circle)

        style.layout('custom.Horizontal.TScale',
                     [(custom_name + '.trough', {'sticky': 'ew'}),
                      (custom_name + '.slider',
                       {'side': 'left', 'sticky': '',
                        'children': [('Horizontal.Scale.label', {'sticky': ''})]
                        })])

        style.theme_settings("vista", {
            "custom.Horizontal.TScale": {
                'map':
                    {'background': [("active", "#2c2c2c"),
                                    ("!disabled", "#2c2c2c")],
                     }
            }})
        # ------------------------------------------------------

        self.controller = controller
        self.playing = True

        self.button = tk.Button(self.upper,
                                image=self.play_icon2,
                                background='#2c2c2c',
                                activebackground='#2c2c2c',
                                bd=0,
                                relief=tk.FLAT,
                                command=self.click,
                                width=33,
                                height=33)
        self.repeat = tk.Button(self.upper,
                                image=self.repeat_icon,
                                background='#2c2c2c',
                                activebackground='#2c2c2c',
                                bd=0,
                                relief=tk.FLAT,
                                width=15,
                                height=15)
        self.shuffle = tk.Button(self.upper,
                                 image=self.shuffle_icon,
                                 background='#2c2c2c',
                                 activebackground='#2c2c2c',
                                 bd=0,
                                 relief=tk.FLAT,
                                 width=15,
                                 height=15)
        self.next = tk.Button(self.upper,
                              image=self.next_icon,
                              background='#2c2c2c',
                              activebackground='#2c2c2c',
                              bd=0,
                              relief=tk.FLAT,
                              width=18,
                              height=18)
        self.previous = tk.Button(self.upper,
                                  image=self.previous_icon,
                                  background='#2c2c2c',
                                  activebackground='#2c2c2c',
                                  bd=0,
                                  relief=tk.FLAT,
                                  width=18,
                                  height=18)

        from Base.listOfPage import currentTrack
        self.sliderValue = tk.DoubleVar()
        self.slider = ttk.Scale(self.lower,
                                to=currentTrack[0]['instance'].songDuration,
                                orient=tk.HORIZONTAL,
                                length=700,
                                variable=self.sliderValue,
                                command=self.UpdateSlider,
                                style='custom.Horizontal.TScale')

        self.currentTime = tk.Label(self.lower,
                                    text="--/--",
                                    foreground='#999999',
                                    background='#2c2c2c')

        endTime = self.convertTime(currentTrack[0]['instance'].songDuration)
        self.endTime = tk.Label(self.lower,
                                text=endTime,
                                foreground='#999999',
                                background='#2c2c2c')

        self.shuffle.grid(row=0, column=1, padx=12)
        self.previous.grid(row=0, column=2, padx=12)
        self.button.grid(row=0, column=3, padx=12)
        self.next.grid(row=0, column=4, padx=12)
        self.repeat.grid(row=0, column=5, padx=12)

        self.currentTime.grid(row=0, column=0, sticky='nsew')
        self.slider.grid(row=0, column=1, sticky='nsew')
        self.endTime.grid(row=0, column=2, sticky='nsew')

        self.upper.grid(row=0, column=0, pady=(5, 0))
        self.lower.grid(row=1, column=0, sticky='nsew', pady=(0, 10))

        # self.upper.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.upper.grid_rowconfigure(0, weight=1)
        # self.upper.grid_propagate(False)

        self.lower.grid_columnconfigure((0, 2), weight=1)
        self.lower.grid_columnconfigure(1, weight=10)
        self.lower.grid_rowconfigure(0, weight=1)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1), weight=1)

        self.button.bind('<Enter>', self.enter)
        self.button.bind('<Leave>', self.leave)

        Middle.count += 1

    def UpdateSlider(self, value):
        from Base.listOfPage import currentTrack
        if currentTrack[0]['instance'].player.music.get_busy():
            self.after_cancel(self.loopID)
            self.sliderValue.set(value)
            currentTrack[0]['instance'].Play()
        else:
            # print("Track Not Playing")
            self.sliderValue.set(value)

    def convertTime(self, currentTime):
        mins, sec = divmod(currentTime, 60)
        time = str(int(mins)).zfill(2) + ":" + str(int(sec)).zfill(2)
        return time

    def TrackPlay(self, currentTime):
        from Base.listOfPage import currentTrack
        if currentTrack[0]['instance'].player.music.get_busy():
            self.sliderValue.set(currentTime)
            time = self.convertTime(currentTime)
            self.currentTime.config(text=time)
            currentTime += 1
            self.loopID = self.after(1000, lambda: self.TrackPlay(currentTime))
        else:
            pass
            # print('Track has ended')

    def click(self):
        self.controller.play_button.click()

    def changeButton(self):
        if self.playing:
            self.button.config(image=self.play_icon2)
            self.playing = False
        else:
            self.button.config(image=self.pause_icon2)
            self.playing = True

    @staticmethod
    def prepare_image(filename, size):
        icon = Image.open('images/' + filename)
        icon = icon.resize((size, size), Image.ANTIALIAS)
        icon = ImageTk.PhotoImage(icon)
        return icon

    def enter(self, event):
        if self.playing:
            self.button.config(image=self.play_icon3)
        else:
            self.button.config(image=self.pause_icon3)

    def leave(self, event):
        if self.playing:
            self.button.config(image=self.play_icon2)
        else:
            self.button.config(image=self.pause_icon2)
