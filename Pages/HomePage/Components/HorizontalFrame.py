import tkinter as tk
import pyglet
import tkinter.font as tkfont
from Pages.Resource.HorizontalScrollableFrame import HorizontalScrollableFrame


class HorizontalFrame(tk.Frame):
    def __init__(self, master, text, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self['background'] = '#181818'
        self['padx'] = 20
        self['pady'] = 20

        self.upper = Upper(self, text)
        self.line = tk.Frame(self, background='#ffffff')
        self.lower = Lower(self)

        self.upper.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
        self.line.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.lower.grid(row=2, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

    def right(self):
        self.lower.scrollable.right()

    def left(self):
        self.lower.scrollable.left()


class Upper(tk.Frame):
    def __init__(self, master, text, *args, **kwargs):
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

        self.left_button = ArrowButton(self, image=self.left, command=master.left)
        self.right_button = ArrowButton(self, image=self.right, command=master.right)

        self.left_button.grid(row=0, column=1, sticky=tk.N+tk.S+tk.E+tk.W)
        self.right_button.grid(row=0, column=2, sticky=tk.N + tk.S + tk.E + tk.W)

        self.label.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=100)
        self.grid_columnconfigure((1, 2), weight=1)


class Lower(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self['background'] = '#181818'
        self['pady'] = 10
        self.bind('<Configure>', self.size)
        self.Ed_sheeran = tk.PhotoImage(file='images/Ed_sheeran.png')

        self.scrollable = HorizontalScrollableFrame(self)
        self.frame = tk.Frame(self.scrollable.scrollable_frame, bg='#181818')

        for i in range(9):
            self.button1 = CardButton(self.frame, text='{} \n hello'.format(i),
                                      image=self.Ed_sheeran
                                      )
            self.button1.grid(row=0, column=i, padx=(0, 10))

        self.frame.grid(row=0, column=0, sticky='nsew')

        self.scrollable.grid(row=0, column=0, sticky=tk.W + tk.E)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def size(self, event):
        global width
        width = event.width
        print(width)


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
    def __init__(self, master, *args, **kwargs):
        tk.Button.__init__(self, master, *args, **kwargs)

        self.bind('<Configure>', self.size)

        pyglet.font.add_file('fonts/Play/Play-Bold.ttf')
        play = tkfont.Font(family="Play", size=15, weight="bold")
        # print(width)
        self['background'] = '#181818'
        self['height'] = 350
        self['border'] = 0
        self['font'] = play
        self['compound'] = tk.TOP
        self['activebackground'] = '#181818'
        self['foreground'] = 'white'
        self['activeforeground'] = 'white'

    def size(self, event):
        global width
        self.configure(width=width/4 -14)
