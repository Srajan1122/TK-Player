import tkinter as tk
from tkinter import ttk
from tkinter import font
import re

# data2 for login
global data2
data2 = {
	"email": "",
	"password": "",
}
global state
state = {
	'user_object': None
}
class UserEntry(tk.Entry):
	def __init__(self, master, placeholder, show, textvariable, id, *args, **kwargs):
		tk.Entry.__init__(self, master, *args, **kwargs)

		# self.placeholder = placeholder

		def default_placeholder(self):
			self.insert(0, placeholder)

		default_placeholder(self)

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

		# self['justify'] = tk.CENTER

		def foc_in(event):
			# self['foreground'] = 'white'
			if (show == 1):
				self['show'] = '*'
			if self['foreground'] == self.default_fg:
				if self.get() == placeholder:
					self['foreground'] = self.default_fg
					self.delete(0, 100)
			self['textvariable'] = textvariable
			self['foreground'] = 'white'

			print(data2)

		def foc_out(event):
			lambda e: enter_details(e)
			self['foreground'] = self.default_fg
			if (id == 'email'):
				data2["email"] = self.get()
			elif (id == 'password'):
				data2["password"] = self.get()
			print(data2)
			print(self.get())
			if not self.get():
				if (show == 1):
					self['show'] = ''
				default_placeholder(self)
			else:
				self.insert(0, self['textvariable'])

		def enter_details(event):
			if (id == 'password'):
				data2["password"] = self.get()
			elif (id == 'email'):
				data2["email"] = self.get()
			print(data2)

		#def key(events):


		self.bind("<FocusIn>", lambda e: foc_in(e))
		self.bind("<FocusOut>", lambda e: foc_out(e))
		self.bind("<Return>", lambda e: enter_details(e))
		#self.bind("<Key>",lambda : self.insert(0,self['textvariable']))


class Frame3(tk.Frame):
	def __init__(self, master, *args, **kwargs):
		tk.Frame.__init__(self, master, *args, **kwargs)

		self.container = tk.Frame(self, bg='#121212', padx=80, pady=80)

		self.logo = tk.PhotoImage(file=r'images\login_head2.png', height=150, width=360)
		self.labelLogo = tk.Label(self.container, image=self.logo, bd=0)
		self.labelLogo.grid(row=0, column=0, pady=25)

		from .Frame1 import Frame1
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
			command=lambda: self.master.show_frame(Frame1)
		)
		self.back.grid(
			row=5,
			column=0,
			sticky='news',
			padx=2,
			pady=5,
			ipadx=20,
			ipady=10
		)

		self.password = UserEntry(
			self.container,
			placeholder="  Password",
			show=1,
			textvariable=None,
			id="password"
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
			placeholder="  Email ID",
			show=0,
			textvariable=None,
			id="email"
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

		# def loginNow():
		# 	password_check = data2.get("password")
		# 	# email_check = data2.get("email")
		#
		# 	if password_check != "" and email_check != "":
		# 		pass
		#
				# def emailCheck(s):
				# 	Pattern = re.compile('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$')
				# 	return Pattern.match(s)
		#
				# def passwordCheck(s):
				# 	if len(s) in range(8, 20):
				# 		return True
				# 	else:
				# 		return False
		#
		# 		if emailCheck(email_check):
		# 			if passwordCheck(password_check):
		# 				self.result['text'] = ""
		# 				print('hiiiiii')
		# 				self.master.login
		# 			else:
		# 				self.result['text'] = "Password must be atleast 8 characters long"
		# 		else:
		# 			self.result['text'] = "Invalid Email"
		# 	else:
		# 		print("last block")
		# 		self.result['text'] = "Invalid Credentials"

		self.result = tk.Label(
			self.container,
			border=0,
			background='#121212',
			activebackground='#121212',
			foreground='white',
			activeforeground='white',
			# font=appHighlightFont,
		)
		self.result.grid(row=3, column=0)

		self.btnimg = tk.PhotoImage(file=r'images\login.png')

		self.login = tk.Button(
			self.container,
			border=0,
			background='#121212',
			activebackground='#121212',
			image=self.btnimg,
			# command=self.master.login
			command=self.loginNow
		)
		self.login.grid(row=4, column=0, pady=10)

		self.container.grid(row=0, column=0)

		self.grid_rowconfigure(0, weight=1)
		self.grid_columnconfigure(0, weight=1)

	def emailCheck(self, s):
		pattern = re.compile('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$')
		return pattern.match(s)

	def passwordCheck(self, s):
		if len(s) in range(8, 20):
			return True
		return False

	def loginNow(self):

		global data2
		password = data2.get("password")
		email = data2.get("email")

		if password.strip(' ') == '' or email.strip(' ') == '':
			self.result['text'] = "Invalid Credentials"
			return

		if not self.emailCheck(email):
			self.result['text'] = "Invalid Email"
			return

		if not self.passwordCheck(password):
			self.result['text'] = "Password must be atleast 8 characters long"
			return
		from Database.Database import sign_in_with_email_and_password
		print('i am in there')
		user_object = sign_in_with_email_and_password(email,password)
		if(user_object):
			# global state
			# print(user_object)
			# state['user_object'] = user_object
			self.master.login(user_object)
		else:
			self.result['text'] = "Login Failed"




