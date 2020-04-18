import tkinter as tk


class Content(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, *kwargs)
        self['background'] = '#181818'
