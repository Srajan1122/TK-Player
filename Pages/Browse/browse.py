import tkinter as tk
from Pages.Resource.VerticalScrollableFrame import ScrollableFrame
from .Components.header import Header
import pyglet
import tkinter.font as tkfont
from Database import Database
from Database import HomePagedata


class Browse(tk.Frame):
	def __init__(self, master, controller, *args, **kwargs):
		tk.Frame.__init__(self, master, *args, **kwargs)
		self['background'] = 'black'
		self.bind('<Configure>', self.size)
		self.main = tk.Frame(self, bg='#181818')
		self.scrollable = ScrollableFrame(self.main)

		pyglet.font.add_file('fonts/Play/Play-Bold.ttf')
		play = tkfont.Font(family="Play", size=15, weight="bold")

		self.head = Header(self,text='Browse')

		self.head.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
		self.content = tk.Frame(self.scrollable.scrollable_frame, bg='red')
		self.frames = {}



		self.categoryFrame = tk.Frame(self,bg='#171717',height=20)
		self.categoryFrame.grid(row=1,column=0,sticky='nsew')
		

		# self.artist = tk.Button(self.categoryFrame, text='artist',
		# 						padx=10,bg='#171717',
		# 						foreground='white',
		# 						pady=10,font=play,
		# 						command=lambda: self.show_frame(Artist)).grid(row=0, column=0,pady=(35,0))
		# self.genre = tk.Button(self.categoryFrame, 
		# 						text='genre',
		# 						padx=10,bg='#171717', 
		# 						foreground='white', 
		# 						pady=10,font=play,
		# 						command=lambda: self.show_frame(Genre)).grid(row=0, column=1,pady=(35,0))


		# data = Database.all_songs
		# print('###################################################')
		# print(data)
		# print(len(data))
		# print('###################################################')

		# gData = HomePagedata.genre_data
		# print('###################################################')
		# # print(gData)
		# print(len(gData))
		# gTitle = ['All']
		# for i in gData:
		# 	gTitle.append(i['text'])
		# print(gTitle)
		# print('###################################################')

		# for j,i in enumerate(gTitle):
		# 	print(j,i)
		# 	self.button = tk.Button(self.categoryFrame,
		# 							text=i,
		# 							padx=5,bg='#171717', 
		# 							foreground='white', 
		# 							pady=10,font=play,
		# 							command=lambda: self.show_frame(All)).grid(row=0, column=j)
		
		for F in (All,Artist,Genre):
			frame = F(self.content, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky='nsew')

		print('hihihaha',self.frames)

		self.show_frame(Artist)

		self.content.grid_rowconfigure(0, weight=1)
		self.content.grid_columnconfigure(0, weight=1)

		self.content.grid(row=0, column=0, sticky='nsew')

		self.main.grid(row=2, column=0, sticky='nsew')
		self.main.grid_rowconfigure(0, weight=1)
		self.main.grid_columnconfigure(0, weight=1)


		self.grid_rowconfigure(0, weight=1)
		self.grid_rowconfigure(1, weight=1)
		self.grid_rowconfigure(2, weight=10)
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

class All(tk.Frame):
	def __init__(self, master, controller, *args, **kwargs):
		tk.Frame.__init__(self, master , *args ,**kwargs)
		self['background'] = 'white'



		