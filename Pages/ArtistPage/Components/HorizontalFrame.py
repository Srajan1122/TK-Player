import tkinter as tk
import pyglet
import tkinter.font as tkfont
from .HorizontalScrollableFrame import HorizontalScrollableFrame
from skimage import io
from PIL import ImageTk, Image


def wid():
    global w
    return w


def hei():
    global height
    return height

def num():
    global number
    return number


class HorizontalFrame(tk.Frame):
    def __init__(self, master, controller, data, text, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self['background'] = '#181818'
        self['padx'] = 20
        self['pady'] = 20

        self.upper = Upper(self, text, data)
        self.line = tk.Frame(self, background='#333333')
        self.lower = Lower(self, controller, data)

        self.upper.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.line.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.lower.grid(row=2, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2,  weight=1)

    def right(self):
        self.lower.scrollable.right()

    def left(self):
        self.lower.scrollable.left()


class Upper(tk.Frame):
    def __init__(self, master, text, data, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self['background'] = '#181818'
        self.master = master

        pyglet.font.add_file('fonts/Play/Play-Bold.ttf')
        play = tkfont.Font(family="Play", size=15, weight="bold")

        self.left = tk.PhotoImage(file=r'.\images\left_arrow.png')
        self.right = tk.PhotoImage(file=r'.\images\right_arrow.png')

        self.label = tk.Label(self,
                              text=text,
                              font=play,
                              anchor=tk.W,
                              background='#181818',
                              foreground='white')

        # if len(data) > 5:
        #     self.left_button = ArrowButton(self, image=self.left, command=master.left)
        #     self.right_button = ArrowButton(self, image=self.right, command=master.right)
        #
        #     self.left_button.grid(row=0, column=1, sticky=tk.N + tk.S + tk.E + tk.W)
        #     self.right_button.grid(row=0, column=2, sticky=tk.N + tk.S + tk.E + tk.W)

        self.label.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=100)
        self.grid_columnconfigure((1, 2), weight=1)


class Lower(tk.Frame):
    count = 0

    def __init__(self, master, controller, data, *args, **kwargs):
        from Base.listOfPage import musicPages2
        musicPages2.append([])
        tk.Frame.__init__(self, master, *args, **kwargs)
        self['background'] = '#181818'
        self['pady'] = 10
        self.bind('<Configure>', self.size)

        global number
        remainder = len(data)%5
        if remainder !=0:
            number = len(data)/5 + 1
        else:
            number = len(data) / 5

        self.scrollable = HorizontalScrollableFrame(self)
        self.frame = tk.Frame(self.scrollable.scrollable_frame, bg='#181818')

        self.images = []

        for i in data:
            self.image = io.imread(i['url'])
            self.image = Image.fromarray(self.image)
            self.images.append(self.image)

        row = 0
        column = 0
        for i, j in enumerate(data):
            if i%5 == 0:
                row += 1
                column=0
            musicPages2[Lower.count].append(0)
            self.button = CardButton(self.frame, text=j['text'],
                                     url=self.images[i],
                                     command=lambda d=j['tracks'],
                                                    img=self.images[i],
                                                    txt=j['text'],
                                                    r=Lower.count,
                                                    c=i:
                                     controller.show_frame_Main2(data=d,
                                                                image=img,
                                                                text=txt,
                                                                r=r,
                                                                c=c)
                                     )
            self.button.grid(row=row, column=column, padx=(0, 10))
            column+=1

        self.frame.grid(row=0, column=0, sticky='nsew')
        self.frame.grid_rowconfigure((0, 1), weight=1)
        self.frame.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)

        self.scrollable.grid(row=0, column=0, sticky=tk.W + tk.E)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        Lower.count += 1

    def size(self, event):
        global width
        global w
        global height
        width = event.width
        height = event.height
        w = event.width / 5 - 14


class ArrowButton(tk.Button):
    def __init__(self, master, *args, **kwargs):
        tk.Button.__init__(self, master, *args, **kwargs)
        self['relief'] = tk.FLAT
        self['background'] = '#181818'
        self['foreground'] = 'white'
        self['activebackground'] = '#181818'
        self['activeforeground'] = 'white'
        self['borderwidth'] = 0


class CardButton(tk.Button):
    def __init__(self, master, url, *args, **kwargs):
        tk.Button.__init__(self, master, *args, **kwargs)
        self.url = url

        self.bind('<Configure>', self.size)

        pyglet.font.add_file('fonts/Play/Play-Bold.ttf')
        play = tkfont.Font(family="Play", size=15, weight="bold")
        self['background'] = '#181818'
        self['height'] = 300
        self['border'] = 0
        self['font'] = play
        self['compound'] = tk.TOP
        self['activebackground'] = '#181818'
        self['foreground'] = 'white'
        self['activeforeground'] = 'white'

        self.bind('<Enter>', self.enter)
        self.bind('<Leave>', self.leave)

    def size(self, event):
        global width
        w = width / 5 - 14
        self.configure(width=int(round(w)), height=int(round(w)) + 50)
        self.image = self.url
        self.image = self.image.resize((int(round(w)), int(round(w))), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(self.image)
        self.config(image=self.image)

    def enter(self, event):
        global width
        w = width / 5 - 14
        self.configure(width=int(round(w)), height=int(round(w)) + 50)
        self.image = self.url
        self.image = self.image.resize((int(round(w))+3, int(round(w))+3), Image.ANTIALIAS)
        # self.greyscale = self.image.convert('LA')
        self.image = ImageTk.PhotoImage(self.image)
        self.config(image=self.image)

    def leave(self, event):
        global width
        w = width / 5 - 14
        self.configure(width=int(round(w)), height=int(round(w)) + 50)
        self.image = self.url
        self.image = self.image.resize((int(round(w)), int(round(w))), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(self.image)
        self.config(image=self.image)
