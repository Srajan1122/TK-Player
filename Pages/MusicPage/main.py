import tkinter as tk


class Main(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        self.data = kwargs.pop('data')
        tk.Frame.__init__(self, master, *args, **kwargs)
        self['background'] = 'red'

        # self.label = tk.Label(self, text=self.data).pack()

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
