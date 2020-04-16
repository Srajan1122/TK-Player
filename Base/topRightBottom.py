import tkinter as tk


class TopRightBottom(tk.Frame):
	def __init__(self, master, *args, **kwargs):
		tk.Frame.__init__(self, master, *args, **kwargs)
		self['background'] = 'purple'

		self.grid_rowconfigure(0, weight=1)
		self.grid_columnconfigure(0, weight=1)

