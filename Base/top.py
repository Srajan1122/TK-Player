import tkinter as tk
from .topLeft import TopLeft
from .topRight import TopRight
from Pages.HomePage.Home import Home
from Pages.Browse.browse import Browse


class Top(tk.Frame):

    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self['background'] = 'yellow'

        self.topleft = TopLeft(self)
        self.topRight = TopRight(self)

        # --------------------------------------------------------------------------
        # Loading all the frames

        self.frames = {}
        for F in (Home, Browse):
            frame = F(self.topRight.topRightBottom, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W + tk.E)

        # Displaying the frame
        self.show_frame(Home)
        # --------------------------------------------------------------------------

        self.topleft.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W + tk.E)
        self.topRight.grid(row=0, column=1, sticky=tk.N + tk.S + tk.W + tk.E)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=40)

    def show_frame(self, context):
        frame = self.frames[context]
        frame.tkraise()
