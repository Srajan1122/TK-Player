import tkinter as tk


class Bottom(tk.Frame):
	def __init__(self, master, *args, **kwargs):
		tk.Frame.__init__(self, master, *args, **kwargs)
		self['bg'] = 'red'
