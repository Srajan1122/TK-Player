import tkinter as tk
from Pages.HomePage.Home import Home
from Pages.Browse.browse import Browse


class TopLeft(tk.Frame):
	def __init__(self, master, *args, **kwargs):
		tk.Frame.__init__(self, master, *args, **kwargs)
		self['background'] = 'blue'
		self.master = master

		home = tk.Button(self, text='Home', command=lambda:master.show_frame(Home)).pack()
		other = tk.Button(self, text='Other', command=lambda:master.show_frame(Browse)).pack()
