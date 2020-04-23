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
		self.content = tk.Frame(self.scrollable.scrollable_frame, bg='red')
		self.frames = {}

		for F in (Artist, Genre):
			frame = F(self.content, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky='nsew')

		self.show_frame(Artist)

		self.artist = tk.Button(self, text='artist', command=lambda: self.show_frame(Artist)).grid(row=0, column=0)
		self.genre = tk.Button(self, text='genre', command=lambda: self.show_frame(Genre)).grid(row=0, column=1)


		self.content.grid_rowconfigure(0, weight=1)
		self.content.grid_columnconfigure(0, weight=1)

		self.content.grid(row=0, column=0, sticky='nsew')

		self.main.grid(row=1, column=0, sticky='nsew')
		self.main.grid_rowconfigure(0, weight=1)
		self.main.grid_columnconfigure(0, weight=1)


		self.grid_rowconfigure(0, weight=1)
		self.grid_rowconfigure(1, weight=10)
		self.grid_columnconfigure(0, weight=1)

	def show_frame(self, context):
		frame = self.frames[context]
		frame.tkraise()


class Artist(tk.Frame):
	def __init__(self, master, controller, *args, **kwargs):
		tk.Frame.__init__(self, master, *args, **kwargs)

		self['background'] = 'yellow'

class Genre(tk.Frame):
	def __init__(self, master, controller, *args, **kwargs):
		tk.Frame.__init__(self, master, *args, **kwargs)

		self['background'] = 'blue'