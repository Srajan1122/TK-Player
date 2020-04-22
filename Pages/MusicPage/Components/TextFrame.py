import tkinter as tk
import pyglet
from PIL import ImageTk, Image
import tkinter.font as tkfont


class TextFrame(tk.Frame):
    def __init__(self, master, text, data, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self['background'] = '#000000'

        pyglet.font.add_file('fonts/Play/Play-Bold.ttf')
        self.head = tkfont.Font(family="Pragatic Narrow", size=28, weight="bold")
        self.support = tkfont.Font(family="Play", size=10, weight="bold")

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

        self.play_button = PlayHeadIcon(self.button_region, data=data,)

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


class PlayHeadIcon(tk.Button):
    def __init__(self, master, data, *args, **kwargs):
        tk.Button.__init__(self, master, *args, **kwargs)

        self.isPlaying = False
        self.data = data

        self.play_raw = Image.open('images/play.png')
        self.play = self.play_raw.resize((100, 35), Image.ANTIALIAS)
        self.play_active = self.play_raw.resize((103, 38), Image.ANTIALIAS)
        self.play = ImageTk.PhotoImage(self.play)
        self.play_active = ImageTk.PhotoImage(self.play_active)

        self.pause_raw = Image.open('images/pause.png')
        self.pause = self.pause_raw.resize((100, 35), Image.ANTIALIAS)
        self.pause_active = self.pause_raw.resize((103, 38), Image.ANTIALIAS)
        self.pause = ImageTk.PhotoImage(self.pause)
        self.pause_active = ImageTk.PhotoImage(self.pause_active)

        self['background'] = '#000000'
        self['activebackground'] = '#000000'
        self['bd'] = 0
        self['width'] = 105
        self['image'] = self.play

        self.bind('<Enter>', self.enter)
        self.bind('<Leave>', self.leave)
        self.bind('<Button-1>', self.click)

        self.grid_propagate(False)
        # self.after(100, self.ifPlaying)

    def ifPlaying(self):
        if self.isPlaying:
            self.config(image=self.pause)
        else:
            self.config(image=self.play)

    def enter(self, event):
        if self.isPlaying:
            self.config(image=self.pause_active)
            return

        self.config(image=self.play_active)

    def leave(self, event):
        if self.isPlaying:
            self.config(image=self.pause)
            return
        self.config(image=self.play)

    def click(self, event):
        from Base.listOfPage import current_playing
        from Base.listOfPage import musicList
        # print(self.master.master.master.master)
        if self.isPlaying:
            self.config(image=self.play)
            if len(current_playing) != 0:
                from Base.listOfPage import currentTrack
                url = currentTrack[0]['url']
                title = currentTrack[0]['title']
                current_playing[0].play_button.click(title=title, url=url)
        else:
            from Base.listOfPage import focusCard
            if len(focusCard) != 0:
                previous_focus = focusCard.pop()
                previous_focus.isPlaying = False
                previous_focus.ifPlaying()
            focusCard.append(self)
            self.config(image=self.pause)
            if len(current_playing) != 0:
                if current_playing[0].master.master.master.master.master == self.master.master.master.master:
                    from Base.listOfPage import currentTrack
                    url = currentTrack[0]['url']
                    title = currentTrack[0]['title']
                    current_playing[0].play_button.click(title=title, url=url)
                else:
                    for i in musicList:
                        for k, v in i.items():
                            if k == self.master.master.master.master:
                                v[0].play_button.click(self.data[0]['title'], self.data[0]['location'])
            elif len(current_playing) == 0:
                for i in musicList:
                    for k, v in i.items():
                        if k == self.master.master.master.master:
                            v[0].play_button.click(self.data[0]['title'], self.data[0]['location'])
