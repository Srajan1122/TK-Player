import tkinter as tk
from Pages.Resource.VerticalScrollableFrame import ScrollableFrame
from .Components.header import Header

class Browse(tk.Frame):
	def __init__(self, master, controller, *args, **kwargs):
		tk.Frame.__init__(self, master, *args, **kwargs)
		self['background'] = 'black'
		self.bind('<Configure>', self.size)
		self.main = tk.Frame(self, bg='#181818')
		self.scrollable = ScrollableFrame(self.main)

		self.head = Header(self,text='Browse')

		self.head.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

		self.grid_rowconfigure(0, weight=1)
		self.grid_rowconfigure(1, weight=10)
		self.grid_columnconfigure(0, weight=1)


