import tkinter as tk
from Pages.HomePage.Home import Home
from Pages.Browse.browse import Browse
from tkinter import font
from PIL import ImageTk, Image
from tkinter.ttk import *


class IconButton(tk.Button):
	def __init__(self, master, controller, text, image, page,  *args, **kwargs):
		tk.Button.__init__(self, master, *args, **kwargs)

		self.appHighlightFont = font.Font(family='lineto circular', size=11, weight='bold')

		self['foreground'] = '#a8a8a8'
		self['background'] = '#121212'
		self['border'] = 0
		self['activebackground'] = '#121212'
		self['activeforeground'] = 'white'
		self['padx'] = 0
		self['pady'] = 5
		self['image'] = image
		self['compound'] = tk.LEFT
		self['text'] = text
		self['anchor'] = tk.W
		self['font'] = self.appHighlightFont
		self['command'] = lambda: controller.show_frame(page)

class NormalButton(tk.Button):
	def __init__(self, master, controller, text, page, *args, **kwargs):
		tk.Button.__init__(self, master, *args, **kwargs)

		self.appHighlightFont = font.Font(family='lineto circular', size=11, weight='bold')

		self['foreground'] = '#a8a8a8'
		self['background'] = '#121212'
		self['border'] = 0
		self['activebackground'] = '#121212'
		self['activeforeground'] = 'white'
		self['padx'] = 10
		self['pady'] = 5
		self['text'] = text
		self['anchor'] = tk.W
		self['font'] = self.appHighlightFont
		self['command'] = lambda: controller.show_frame(page)

class TopLeft(tk.Frame):
	def __init__(self, master, *args, **kwargs):
		tk.Frame.__init__(self, master, *args, **kwargs)
		self['background'] = '#121212'
		self.master = master

		#font
		self.appHighlightFont = font.Font(family='lineto circular', size=12, weight='bold')

		#images
		self.home_icon = tk.PhotoImage(file=r".\Images\home.png")
		self.browse_icon = tk.PhotoImage(file=r".\Images\browse_outlined.png")

		self.frame1 = tk.Frame(self, bg='#121212', padx=0)
		self.frame2 = tk.Frame(self, bg='#121212', padx=30)
		self.frame3 = tk.Frame(self, bg='#121212', padx=10)
		self.frame4 = tk.Frame(self, bg='#121212', padx=10)
		self.frame5 = tk.Frame(self, bg='#121212', padx=10)

		self.menu = tk.Button(self.frame1,
							  background='#121212',
							  activebackground='#121212',
							  foreground='white',
							  activeforeground='white',
							  text=". . .",
							  font=self.appHighlightFont,
							  border=0,
							  pady=10)



		self.home = IconButton(self.frame2, master, text='Home', image=self.home_icon, page=Home)
		self.browse = IconButton(self.frame2, master, text='Browse', image=self.browse_icon, page=Browse)

		self.appHighlightFont = font.Font(family='lineto circular', size=9, weight='bold')
		self.label = tk.Label(self.frame3,
						 text='YOUR LIBRARY',
						 background='#121212',
						 foreground='#a8a8a8',
						 anchor= tk.W,
						 padx = 5,
						 font=self.appHighlightFont
						 )
		self.madeForYou = NormalButton(self.frame3, master, text='Made For You', page='')
		self.recentlyPlayed = NormalButton(self.frame3, master, text='Recently Played', page='')
		self.likedSongs = NormalButton(self.frame3, master, text='Liked Songs', page='')
		self.albums = NormalButton(self.frame3, master, text='Albums', page='')
		self.artists = NormalButton(self.frame3, master, text='Artists', page='')

		self.label2 = tk.Label(self.frame4,
							  text='PLAYLISTS',
							  background='#121212',
							  foreground='#a8a8a8',
							  anchor=tk.W,
							  padx=5,
							  font=self.appHighlightFont
							  )

		self.menu.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W + tk.E)
		self.home.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
		self.browse.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
		self.label.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
		self.madeForYou.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
		self.recentlyPlayed.grid(row=2, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
		self.likedSongs.grid(row=3, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
		self.albums.grid(row=4, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
		self.artists.grid(row=5, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
		self.label2.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)


		self.frame1.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
		self.frame2.grid(row=1, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
		self.frame3.grid(row=2, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
		self.frame4.grid(row=3, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
		self.frame5.grid(row=4, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

		self.grid_columnconfigure(0, weight=1)
		self.grid_rowconfigure(0, weight=1)
		self.grid_rowconfigure(1, weight=2)
		self.grid_rowconfigure(2, weight=2)
		self.grid_rowconfigure(3, weight=2)
		self.grid_rowconfigure(4, weight=10)


