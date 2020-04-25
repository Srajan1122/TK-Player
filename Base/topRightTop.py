import tkinter as tk
from PIL import Image, ImageTk
from tkinter import font
from .listOfPage import pages, rightPage, incrementCount, getCount, resetCount
from Pages.UserPage.UserPage import UserPage


class IconButton(tk.Button):
	def __init__(self, master, controller, text, image, command, *args, **kwargs):
		tk.Button.__init__(self, master, *args, **kwargs)

		self.appHighlightFont = font.Font(family='lineto circular', size=11, weight='bold')
		self['foreground'] = 'white'
		self['background'] = '#121212'
		self['border'] = 0
		self['activebackground'] = '#121212'
		# self['activeforeground'] = 'white'
		self['padx'] = 10
		self['pady'] = 5
		self['image'] = image
		self['compound'] = tk.LEFT
		self['text'] = text
		self['anchor'] = tk.W
		self['font'] = self.appHighlightFont
		self['command'] = command

class TopRightTop(tk.Frame):
	def __init__(self, master, *args, **kwargs):
		tk.Frame.__init__(self, master, *args, **kwargs)
		self['background'] = '#000000'

		self.back = Back(self)
		self.search = tk.Frame(self, bg='yellow')
		self.name = tk.Frame(self, bg='#121212')
		self.dropdown = tk.Frame(self, bg='pink')
		self.button = tk.Frame(self, bg='green')


		#Dynamic content
		f = open('user')
		x = f.readlines()[0]
		from Database.Database import get_user
		myobject = get_user(x)

		#User_button
		# self.name = self.user_data
		# print(self.name)
		self.appHighlightFont = font.Font(family='lineto circular', size=11, weight='bold')
		self.appHighlightFont2 = font.Font(family='lineto circular',underline=1, size=11, weight='bold')
		self.user_icon = tk.PhotoImage(file=r".\Images\user2.png",height=25,width=25)
		self.userButton = IconButton(self.name,
								master, text= myobject['display_name'],
								image=self.user_icon,
								command=lambda:self.master.master.show_frame(UserPage)
							)
		self.userButton.bind("<Enter>",lambda e : self.userButtonHighlight(e))
		self.userButton.bind("<Leave>",lambda e : self.userButtonLeave(e))

		#user_dropdown
		self.down = tk.PhotoImage(file=r".\Images\down_arrow.png",width=25,height=25)
		self.user_menu = tk.Menubutton(
								self.name,
								image=self.down,
								background="#121212",
								activebackground="#121212",
								bd=0, padx=2, pady=0
							)
		self.user_menu.menu = tk.Menu(
									self.user_menu,
									tearoff=0,
									background='#35363a', activebackground='#404040',
									foreground='#a8a8a8', activeforeground='white',
									bd=0,
									font=self.appHighlightFont
								)
		self.user_menu['menu'] = self.user_menu.menu
		self.user_menu.menu.add_command(label='Logout',command=self.logout)
		self.user_menu.menu.add_command(label="Settings")

		self.user_menu.grid(row=0,column=1,sticky='nsew', padx=10, pady=0)
		self.userButton.grid(row=0, column=0, sticky='nsew',ipady=0)
		self.back.grid(row=0, column=0, sticky='nsew')
		self.search.grid(row=0, column=1, sticky='nsew')
		self.name.grid(row=0, column=2, sticky='nsew')
		self.dropdown.grid(row=0, column=3, sticky='nsew')
		self.button.grid(row=0, column=4, sticky='nsew')

		self.rowconfigure(0)
		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=20)
		self.grid_columnconfigure(2, weight=10)
		self.grid_columnconfigure(3, weight=1)
		self.grid_columnconfigure(4, weight=4)

	def userButtonHighlight(self,event):
		self.userButton['bg']="#404040"
		self.userButton['font'] = self.appHighlightFont2

	def userButtonLeave(self,event):
		self.userButton['bg'] = "#121212"
		self.userButton['font'] = self.appHighlightFont

	def logout(self):
		import os
		from Database.Database import sign_out
		from Pages.UserAuthentication.AuthBase import AuthBase
		sign_out()
		print(os.getcwd())
		self.master.master.master.master.destroy()
		login = AuthBase()
		login.mainloop()


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

