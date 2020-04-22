import tkinter as tk
from PIL import Image, ImageTk
from .listOfPage import pages, rightPage, incrementCount, getCount, resetCount
from Pages.UserPage.UserPage import UserPage


class TopRightTop(tk.Frame):
	def __init__(self, master, *args, **kwargs):
		tk.Frame.__init__(self, master, *args, **kwargs)
		self['background'] = '#000000'

		self.back = Back(self)
		self.search = tk.Frame(self, bg='yellow')
		self.name = tk.Frame(self, bg='blue')
		self.dropdown = tk.Frame(self, bg='pink')
		self.button = tk.Frame(self, bg='green')

		self.userButton = tk.Button(self.name, text='Username', command=lambda: self.master.master.show_frame(UserPage))
		self.userButton.grid(row=0, column=0, sticky='nsew')
		self.back.grid(row=0, column=0, sticky='nsew')
		self.search.grid(row=0, column=1, sticky='nsew')
		self.name.grid(row=0, column=2, sticky='nsew')
		self.dropdown.grid(row=0, column=3, sticky='nsew')
		self.button.grid(row=0, column=4, sticky='nsew')

		self.rowconfigure(0, weight=1)
		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=20)
		self.grid_columnconfigure(2, weight=10)
		self.grid_columnconfigure(3, weight=1)
		self.grid_columnconfigure(4, weight=4)


class Back(tk.Frame):
	def __init__(self, master, *args, **kwargs):
		tk.Frame.__init__(self, master, *args, **kwargs)
		self['background'] = '#000000'

		self.leftImage = tk.PhotoImage(file=r'.\images\left_arrow.png')
		self.rightImage = tk.PhotoImage(file=r'.\images\right_arrow.png')

		self.left = ArrowButton(self, image=self.leftImage, command=self.left)
		self.right = ArrowButton(self, image=self.rightImage, command=self.right)

		self.left.grid(row=0, column=0, sticky='ew')
		self.right.grid(row=0, column=1, sticky='ew')

		self.grid_rowconfigure(0, weight=1)
		self.grid_columnconfigure((0, 1), weight=1)

	def left(self):
		if len(pages) > 0:
			if len(pages) == 1:
				return
			else:
				r = pages.pop(len(pages)-1)
				rightPage.append(r)
				frame = pages[len(pages) - 1]

				self.master.master.master.show_frame_directly(frame)

	def right(self):
		if len(rightPage) < 1:
			return

		c = getCount()
		if c > len(rightPage):
			return
		frame = rightPage[len(rightPage)-c]
		pages.append(frame)
		incrementCount()
		self.master.master.master.show_frame_directly(frame)


class ArrowButton(tk.Button):
	def __init__(self, master, *args, **kwargs):
		tk.Button.__init__(self, master, *args, **kwargs)
		self['relief'] = tk.FLAT
		self['background'] = '#000000'
		self['foreground'] = 'white'
		self['activebackground'] = '#000000'
		self['activeforeground'] = 'white'
		self['borderwidth'] = 0

