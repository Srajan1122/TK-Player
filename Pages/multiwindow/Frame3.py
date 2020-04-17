import tkinter as tk
from tkinter import ttk
from tkinter import font

class UserEntry(tk.Entry):
	def __init__(self, master, placeholder, *args, **kwargs):
		tk.Entry.__init__(self, master, *args, **kwargs)

		self.placeholder = placeholder
		def default_placeholder(self):
			self.insert(0,self.placeholder)
		
		self.appHighlightFont = font.Font(
								family='lineto circular', 
								size=12, 
								)

		self.default_fg = '#867f7a'
		self.input_fg = 'white'
		
		
		self['background'] = '#404040'
		self['foreground'] = self.default_fg
		self['insertbackground'] = 'white'
		self['font'] = self.appHighlightFont
		self['border'] = 0
		#self['justify'] = tk.CENTER
		

		def foc_in(event):
			#self['foreground'] = 'white'
			if self['foreground'] == self.default_fg:
				if self.get() == placeholder:
					self['foreground'] = self.default_fg
					self.delete(0,100)
			self['foreground'] = 'white'
			
					
		def foc_out(event):
			self['foreground'] = self.default_fg
			if not self.get():
				default_placeholder(self)
			else:
				insert(0,self.placeholder)

		self.bind("<FocusIn>", lambda e: foc_in(e))
		self.bind("<FocusOut>", lambda e: foc_out(e))

		default_placeholder(self)

class Frame3(tk.Frame):
	def __init__(self, master, *args, **kwargs):
		tk.Frame.__init__(self, master, *args, **kwargs)

		self.container = tk.Frame(self, bg='#121212', padx=80, pady=80)

		self.logo = tk.PhotoImage(file=r'./images/login_head2.PNG',height=150,width=360)
		self.labelLogo = tk.Label(self.container, image=self.logo,bd=0)
		self.labelLogo.grid(row=0, column=0, pady=25)

		from Frame1 import Frame1
		self.appHighlightFont = font.Font(
									family='lineto circular',
									size=14
								)
		self.back = tk.Button(
							self.container,
							border=0,
							text='Back',
							background='#121212',
							activebackground='#121212',
							foreground='white',
							activeforeground='white',
							font=self.appHighlightFont,
							command=lambda:self.master.show_frame(Frame1)
						)
		self.back.grid(
						row=4,
						column=0,
						sticky='news',
						padx=2,
						pady=5,
						ipadx=20,
						ipady=10
					)
		

		self.password = UserEntry(
							self.container, 
							placeholder="  Password"
						)
		self.password.grid(
						row=2,
						column=0,
						sticky=tk.N + tk.S + tk.E + tk.W,
						padx=2,
						pady=5,
						ipadx=20,
						ipady=10
						)


		self.email = UserEntry(
							self.container, 
							placeholder="  Email ID"
						)
		self.email.grid(
						row=1,
						column=0,
						sticky=tk.N + tk.S + tk.E + tk.W,
						padx=2,
						pady=4,
						ipadx=20,
						ipady=10
						)

		self.btnimg = tk.PhotoImage(file=r'./images/login.PNG')

		self.login = tk.Button(
						self.container,
						border=0,
						background='#121212',
						activebackground='#121212',
						image=self.btnimg,
						command=self.master.login
						)
		self.login.grid(row=3, column=0, pady=10)

		self.container.grid(row=0, column=0)

		self.grid_rowconfigure(0, weight=1)
		self.grid_columnconfigure(0, weight=1)


		
