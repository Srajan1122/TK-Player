#-----Signup/Register Page
import traceback
import tkinter as tk
from tkinter import ttk
from tkinter import font
import re
from tkinter import messagebox  

from .Frame4 import Frame4
from .Frame4 import data3


# data for registration and passing them
global data
data = {
	"username": "",
	"password": "",
	"phone": "",
	"email": ""
}


# Class for input field: contact number
class NumberEntry(tk.Entry):
	def __init__(self, master, placeholder, id, *args, **kwargs):
		tk.Entry.__init__(self, master, *args, **kwargs)

		# self.placeholder = placeholder
		self['textvariable'] = placeholder
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

		def default_placeholder(self):
			print("placeholder:", self.get())
			# self.delete(0,100)
			self.insert(0, placeholder)

		def only_numbers(char):
			return char.isdigit()

		def foc_in(event):
			# self['foreground'] = 'white'
			if self['foreground'] == self.default_fg:
				if self.get() == placeholder:
					self['foreground'] = self.default_fg
					self.delete(0, 100)
			validation = master.register(only_numbers)
			self['validate'] = 'key'
			self['validatecommand'] = (validation, '%S')
			self['foreground'] = 'white'
			self['textvariable'] = textvariable

		def foc_out(event):
			# print(self.get())
			lambda e: enter_details(e)
			self['foreground'] = self.default_fg
			if (id == 'phone'):
				data["phone"] = self.get()
			print(data)

			if not self.get():
				default_placeholder(self)
			else:
				self.insert(0, self['textvariable'])

		def enter_details(event):
			if (id == 'phone'):
				data["phone"] = self.get()
			print(data)

		self.bind("<FocusIn>", lambda e: foc_in(e))
		self.bind("<FocusOut>", lambda e: foc_out(e))
		self.bind("<Return>", lambda e: enter_details(e))

		default_placeholder(self)


# Class for input fields: username, password, email
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

		#def key(events)	
		self.bind("<FocusIn>", lambda e: foc_in(e))
		self.bind("<FocusOut>", lambda e: foc_out(e))

# Frame of Signup/Register Page
class Frame2(tk.Frame):
	def __init__(self, master, *args, **kwargs):
		tk.Frame.__init__(self, master, *args, **kwargs)

		#Frame
		self.container = tk.Frame(self, bg='#121212', padx=80, pady=30)

		#Signup/Register head
		self.logo = tk.PhotoImage(file=r'images\signup_head.png', height=225, width=360)
		self.labelLogo = tk.Label(self.container, image=self.logo, bd=0)
		self.labelLogo.grid(row=0, column=0)

		#For Back button
		from .Frame1 import Frame1

		#Font style, size
		self.appHighlightFont = font.Font(
			family='lineto circular',
			size=14,
		)

		#Bck button
		self.back = tk.Button(
			self.container,
			border=0,
			text='Back',
			background='#121212',
			activebackground='#121212',
			activeforeground='white',
			font=self.appHighlightFont,
			foreground='white',
			command=lambda: self.master.show_frame(Frame1)
		)
		self.back.grid(
			row=7,
			column=0,
			sticky='news',
			padx=2,
			pady=5,
			ipadx=20,
			ipady=10
		)

		#Username Entry
		self.username_input = tk.StringVar()
		self.username = UserEntry(
			self.container,
			placeholder="  Username",
			show=0,
			textvariable=None,
			id="username"
		)
		self.username.grid(
			row=1,
			column=0,
			sticky=tk.N + tk.S + tk.E + tk.W,
			padx=2,
			pady=5,
			ipadx=20,
			ipady=10
		)

		#Password Entry
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

		#Contact Number Entry
		self.phone = UserEntry(
			self.container,
			placeholder="  Contact Number",
			show=0,
			textvariable=None,
			id="phone",
		)
		self.phone.grid(
			row=3,
			column=0,
			sticky=tk.N + tk.S + tk.E + tk.W,
			padx=2,
			pady=5,
			ipadx=20,
			ipady=10
		)

		#Email Entry
		self.email = UserEntry(
			self.container,
			placeholder="  Email ID",
			show=0,
			textvariable=None,
			id="email"
		)
		self.email.grid(
			row=4,
			column=0,
			sticky=tk.N + tk.S + tk.E + tk.W,
			padx=2,
			pady=4,
			ipadx=20,
			ipady=10
		)

		#Result/Stataus Display
		self.result = tk.Label(
			self.container,
			border=0,
			background='#121212',
			activebackground='#121212',
			foreground='white',
			activeforeground='white',
			# font=appHighlightFont,
		)
		self.result.grid(row=5, column=0)

		#Signup/Register Button
		self.btnimg = tk.PhotoImage(file=r'images\register.png')
		
		self.register = tk.Button(
			self.container,
			border=0,
			background='#121212',
			activebackground='#121212',
			image=self.btnimg,
			command=self.registerNow
		)
		self.register.grid(row=6, column=0, pady=10)

		#Frame grid and configurations
		self.container.grid(row=0, column=0)

		self.grid_rowconfigure(0, weight=1)
		self.grid_columnconfigure(0, weight=1)

	#Validaiton funtion for contact number
	def phoneCheck(self,s):
		Pattern = re.compile("(0/91)?[7-9][0-9]{9}")
		return Pattern.match(s)

	#Validation function for email
	def emailCheck(self,s):
		Pattern = re.compile('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$')
		return Pattern.match(s)

	#Validation function for password
	def passwordCheck(self,s):
		if (len(s) in range(8, 20)):
			return True
		else:
			return False

	#Validation for signup/register
	def registerNow(self):
		
		global data
		username = self.username.get()
		password = self.password.get()
		phone = self.phone.get()
		email = self.email.get()

		data["username"] = username
		data["password"] = password
		data["phone"] = phone
		data["email"] = email
		print(data)

		#placeholders
		username_placeholder = "  Username"
		password_placeholder = "  Password"
		phone_placeholder = "  Contact Number"
		email_placeholder = "  Email ID"
	
		if username==username_placeholder or password==password_placeholder or phone==phone_placeholder or email==email_placeholder:
			self.result['text'] = "Please enter all fields"
			return

		if username.strip(' ')=='' or password.strip(' ')=='' or phone.strip(' ')=='' or email.strip(' ')=='' :
			self.result['text'] = "Invalid Credentials" 
			return

		if not self.passwordCheck(password):
			self.result['text'] = "Password must be atleast 8 characters long"
			return

		if not self.phoneCheck(phone):
			self.result['text'] = "Invalid Contact Number"
			return

		if not self.emailCheck(email):
			self.result['text'] = "Invalid Email ID"
			return
		data3['email'] = email
		try:
			self.result['text'] = "Account created successfully"
			from Database.Database import register_user
			register_user(username,email,phone,password)
			
			from Database.Database import send_email_verification_otp
			send_email_verification_otp(data3['email'])
		except Exception as ex:
			print('Exception Occured which is of type :', ex.__class__.__name__)
			messagebox.showerror('Error',ex.__class__.__name__)  
			self.result['text'] = ex.__class__.__name__
			return
		
		return self.master.show_frame(Frame4)























'''
	def change():
		return self.master.show_frame(Frame1)
		def register():
			# print(data)
			username_check = data.get("username")
			# print("user: ",username_check)
			password_check = data.get("password")
			# print("pass: ",password_check)
			email_check = data.get("email")
			# print()
			phone_check = data.get("phone")

			print("user: ", username_check)
			print("pass: ", password_check)
			print("email: ", email_check)
			print("phone: ", phone_check)
			if (username_check != "" and password_check != "" and email_check != "" and phone_check != ""):
				print("first block")

				def phoneCheck(s):
					Pattern = re.compile("(0/91)?[7-9][0-9]{9}")
					return Pattern.match(s)

				def emailCheck(s):
					Pattern = re.compile('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$')
					return Pattern.match(s)

				def passwordCheck(s):
					if (len(s) in range(8, 20)):
						return True
					else:
						return False

				if (passwordCheck(password_check)):
					if (phoneCheck(phone_check)):
						if (emailCheck(email_check)):
							from Database.Database import register_user
							register_user(username_check,email_check,phone_check,password_check)

							change()
							self.result['text'] = "Account was succesfully created"
						else:
							self.result['text'] = "Invalid Email ID"
					else:
						self.result['text'] = "Invalid Contact Number"
				else:
					self.result['text'] = "Password must be atleast 8 characters long"
				# change()
			# else:
			# 	self.result['text'] = "Invalid Phone number"
			else:
				print("last block")
				self.result['text'] = "Invalid Credentials"
'''
		

