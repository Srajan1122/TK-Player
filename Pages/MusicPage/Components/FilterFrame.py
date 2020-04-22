import tkinter as tk
from tkinter import font
import re

global titles
titles = []

global matches
matches = []

class UserEntry(tk.Entry):
	def __init__(self, master, placeholder, show, textvariable, id, *args, **kwargs):
		tk.Entry.__init__(self, master, *args, **kwargs)

		#placeholder function
		def default_placeholder(self):
			self.insert(0, placeholder)

		default_placeholder(self)		

		#font size, style
		self.appHighlightFont = font.Font(
			family='lineto circular',
			size=12,
		)

		#font color
		self.default_fg = '#867f7a'
		self.input_fg = 'white'

		#properties of Entry widget
		self['background'] = '#404040'
		self['foreground'] = self.default_fg
		self['insertbackground'] = 'white'
		self['font'] = self.appHighlightFont
		self['border'] = 0

		#function called on focusing
		def foc_in(event):
			if (show == 1):
				self['show'] = '*'
			if self['foreground'] == self.default_fg:
				if self.get() == placeholder:
					self['foreground'] = self.default_fg
					self.delete(0, 100)
			self['foreground'] = 'white'
			self['textvariable'] = textvariable

		#function called when not focusing
		def foc_out(event):
			self['foreground'] = self.default_fg
			print(self.get())
			if not self.get():
				if (show == 1):
					self['show'] = ''
				default_placeholder(self)
			else:
				self.insert(0, self['textvariable'])

		
		def searchFunc(event):
			user_input = self.get().upper()
			
			for i in range(len(titles)):
				print(titles[i])
				if not user_input:
					return
				input_matcher = re.search(
									re.search(
										"{}".format(user_input),
										"{}".format(titles[i].upper)
									)
								)
				if input_matcher:
					matches.append(titles[i])

		print(matches)
				


		#def key(events)	
		self.bind("<FocusIn>", lambda e: foc_in(e))
		self.bind("<Button>", lambda e: foc_out(e))
		self.bind("<Key>", lambda e : searchFunc(e))


class FilterFrame(tk.Frame):
	def __init__(self, master, *args, data, **kwargs):
		tk.Frame.__init__(self, master, *args, **kwargs)
		self['background'] = 'black'
		self['height'] = 40

		self.filter = UserEntry(
			self, placeholder="  Filter",
			show=0, textvariable=None, id=None
		)
		self.filter.grid(
			row=0, column=0, sticky='nsew'
		)
		print(data)
		
		for song in data:
			#print(song['title'])
			titles.append(song['title'])

		print(titles)
		# self.button = tk.Button(self, text='clear', command=self.clear)
		# self.button.grid(row=0, column=0, sticky='nsew')

		# self.button2 = tk.Button(self, text='fill', command=self.fill)
		# self.button2.grid(row=0, column=1, sticky='nsew')

		# self.grid_columnconfigure((0, 1), weight=1)
		# self.grid_rowconfigure(0, weight=1)

	def clear(self):
		from .Content.Content import Content
		self.content = Content(self.master.master, data=[])
		self.content.grid(row=3, column=0, sticky='nsew')
		self.content.tkraise()

	def fill(self):
		self.master.master.content.tkraise()
