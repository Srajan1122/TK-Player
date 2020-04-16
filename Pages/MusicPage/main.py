import tkinter as tk


class Main(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        self.data = kwargs.pop('data')
        print(self.data)
        tk.Frame.__init__(self, master, *args, **kwargs)
        self['background'] = 'red'

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
