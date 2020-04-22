import tkinter as tk


class UserPage(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self['background'] = 'red'

        
