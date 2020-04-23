import tkinter as tk


class Bottom(tk.Frame):
	def __init__(self, master, *args, **kwargs):
		tk.Frame.__init__(self, master, *args, **kwargs)
		self['bg'] = '#2c2c2c'

		self.grid_rowconfigure(0, weight=1)
		self.grid_columnconfigure(0, weight=1)

	def show_frame(self, title):
		from Base.listOfPage import bottomPage
		frame = bottomPage[0]
		frame.grid(row=0, column=0, sticky='nsew')
		frame.tkraise()
