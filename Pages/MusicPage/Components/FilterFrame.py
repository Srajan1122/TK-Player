import tkinter as tk
from tkinter import font
import re

global matchingSongs
matchingSongs = []

class UserEntry(tk.Entry):
	def __init__(self, master, placeholder, textvariable, songDict, *args, **kwargs):
		tk.Entry.__init__(self, master, *args, **kwargs)

		#placeholder function
		def default_placeholder(self):
			self.insert(0, placeholder)

		default_placeholder(self)		

		#font size, style
		self.appHighlightFont = font.Font(
			family='lineto circular',
			size=11,
		)

		#font color
		self.default_fg = '#867f7a'
		self.input_fg = 'white'

		#properties of Entry widget
		self['background'] = '#121212'
		self['foreground'] = self.default_fg
		self['insertbackground'] = 'white'
		self['font'] = self.appHighlightFont
		self['border'] = 0

		#function called on focusing
		def foc_in(event):
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
				default_placeholder(self)
			else:
				self.insert(0, self['textvariable'])

		#def key(events)	
		self.bind("<FocusIn>", lambda e: foc_in(e))
		self.bind("<FocusOut>", lambda e: foc_out(e))

class FilterFrame(tk.Frame):
	def __init__(self, master, *args, data, **kwargs):
		tk.Frame.__init__(self, master, *args, **kwargs)
		self['background'] = '#121212'
		self['height'] = 40

		self.search = tk.PhotoImage(file=r'images\search2.png', height=18, width=18)
		self.search_highlight = tk.PhotoImage(file=r'images\search_highlight.png', height=18, width=18)
		self.search_icon = tk.Label(self, image=self.search, bd=0, bg="#121212")
		self.search_icon.grid(row=0, column=0, ipadx=10, ipady=3, sticky='nsew')

		self.filter = UserEntry(
			self, placeholder="  Filter",
			textvariable=None,
			songDict = data
		)
		self.filter.grid(
			row=0, column=1, sticky='nsew',padx=2,
			pady=4,
			ipadx=20,
			ipady=5
		)

		self.close = tk.PhotoImage(file=r'images/close3.png',height=20, width=20)
		self.close_icon = tk.Button(
								self, 
								image=self.close, 
								bd=0, 
								bg="#121212", 
								command=self.leaveHighlight,
								activebackground="#121212",
								width=30
							)
		self.close_icon.grid(row=0,column=3, sticky='nsew')

		#songs = data
		print(data)
		self.filter.bind("<Key>", lambda e : self.searchFunc(e,data))
		self.bind("<Enter>",lambda e: self.highlight(e))
		self.bind("<FocusIn>",lambda e : self.focusHighlight(e))
		self.bind("<Leave>",lambda e : self.leaveHighlight(e))
		
		# self.button = tk.Button(self, text='clear', command=self.clear)
		# self.button.grid(row=0, column=0, sticky='nsew')

		# self.button2 = tk.Button(self, text='fill', command=self.fill)
		# self.button2.grid(row=0, column=1, sticky='nsew')

		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=25)
		self.grid_columnconfigure(2, weight=2)

	def foc_out(self, event):
		self.filter['foreground'] = "#867f7a"
		print(self.filter.get())
		if not self.filter.get():
			self.filter.insert(0, "  Filter")
		else:
			self.filter.insert(0, self['textvariable'])

	def searchFunc(self,event,data):

		matchingSongs.clear()
		self.songs = data
		
		print("searchFunc started")
		#print(self.songs)
		user_input = self.filter.get().upper()
		print(user_input)
		
		if not user_input:
			return
		#print("first check done")
		#print(songs)
		for i in range(len(self.songs)):
			print(self.songs[i]['title'])
			input_matcher = re.search(
								user_input,
								self.songs[i]['title'].upper()
							)
			print(input_matcher)
			if input_matcher:
				matchingSongs.append(self.songs[i])
				#print("result: ",matchingSongs)
		
		if not matchingSongs:
			self.clear2()
		else:
			self.clear()


	def highlight(self,event):
		self['bg'] = "#121212"
		self.search_icon['image'] = self.search_highlight
		self.filter['foreground'] = 'white'
		
	
	def leaveHighlight(self):
		self['bg'] = "#121212"
		self.search_icon['image'] = self.search
		self.close_icon['bg'] = "#121212"
		self.filter['bg'] = "#121212"
		self.filter['foreground'] = "#867f7a"
		self.close_icon['bg'] = "#12121212"
		

	def focusHighlight(self,event):
		self['bg'] = "#404040"
		self.search_icon['bg'] = "#404040"
		self.filter['bg'] = "#404040"
		self.close_icon['bg'] = "#404040"
		self.unbind("<Key>")

	# def focusoutHighlight(self,event):
	# 	leaveHighlight(self)


	def clear(self):
		print("clear started")
		print("matchingDict: ",matchingSongs)
		from .Content.Content import Content
		self.content = Content(self.master.master, data=matchingSongs)
		self.content.grid(row=3, column=0, sticky='nsew')
		self.content.tkraise()

	def clear2(self):
		print("clear2 started")
		#print("matchingDict: ",matchingSongs)
		from .Content.Content import Content
		self.content = Content(self.master.master, data=[])
		self.content.grid(row=3, column=0, sticky='nsew')
		self.content.tkraise()

	def fill(self):
		self.master.master.content.tkraise()
