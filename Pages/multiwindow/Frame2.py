import tkinter as tk
from tkinter import ttk
from tkinter import font
import re

#data for registration
global data 
data = {
	"username" : "",
	"password" : "",
	"phone" : "",
	"email" : ""
}

#Class for input field: contact number
class NumberEntry(tk.Entry):
	def __init__(self, master, placeholder, *args, **kwargs):
		tk.Entry.__init__(self, master, *args, **kwargs)

		self.placeholder = placeholder
		
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
			print( "placeholder:",self.get())
			#self.delete(0,100)
			self.insert(0,self.placeholder)
		
		def only_numbers(char):
			return char.isdigit()
		
		def foc_in(event):
			#self['foreground'] = 'white'
			if self['foreground'] == self.default_fg:
				if self.get() == placeholder:
					self['foreground'] = self.default_fg
					self.delete(0,100)
			validation = master.register(only_numbers)
			self['validate'] = 'key'
			self['validatecommand'] = (validation,'%S')
			self['foreground'] = 'white'
					
		def foc_out(event):
			print(self.get())
			self['foreground'] = self.default_fg
			if not self.get():
				default_placeholder(self)
			else:
				self.insert(0,self.placeholder)

		self.bind("<FocusIn>", lambda e: foc_in(e))
		self.bind("<FocusOut>", lambda e: foc_out(e))

		default_placeholder(self)

#Class for input fields: username, password, email
class UserEntry(tk.Entry):
	def __init__(self, master, placeholder, show, textvariable, id, *args, **kwargs):
		tk.Entry.__init__(self, master, *args, **kwargs)

		#self.placeholder = placeholder
		self['textvariable'] = placeholder
		def default_placeholder(self):
			self.insert(0,placeholder)

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
		
		def foc_in(event):
			#self['foreground'] = 'white'
			if(show==1):
				self['show']='*'
			if self['foreground'] == self.default_fg:
				if self.get() == placeholder:
					self['foreground'] = self.default_fg
					self.delete(0,100)
			self['foreground'] = 'white'
			self['textvariable'] = textvariable
		
		def foc_out(event):
			self['foreground'] = self.default_fg
			if(id=='username'):
				data["username"] = self.get()
			elif(id=='password'):
				data["password"] = self.get()
			elif(id=='email'):
				data["email"] = self.get()
			print(data)

			print(self.get())
			if not self.get():
				if(show==1):
					self['show']= ''
				default_placeholder(self)
			else:
				insert(0,self['textvariable'])
		
		def enter_details(event):
			if(id=='username'):
				data["username"] = self.get()
			elif(id=='password'):
				data["password"] = self.get()
			elif(id=='email'):
				data["email"] = self.get()
			print(data)

		self.bind("<FocusIn>", lambda e: foc_in(e))
		self.bind("<FocusOut>", lambda e: foc_out(e))
		self.bind("<Return>", lambda e: enter_details(e))

#Frame Class
class Frame2(tk.Frame):
	def __init__(self, master, *args, **kwargs):
		tk.Frame.__init__(self, master, *args, **kwargs)

		#frame size
		self.container = tk.Frame(self, bg='#121212', padx=80, pady=30)

		#signup_logo
		self.logo = tk.PhotoImage(file=r'./images/signup_head.PNG',height=225,width=360)
		self.labelLogo = tk.Label(self.container, image=self.logo,bd=0)
		self.labelLogo.grid(row=0, column=0)

		#fields : username, password, contact number, email
		from Frame1 import Frame1

		#font
		self.appHighlightFont = font.Font(
								family='lineto circular', 
								size=14, 
								)

		#back button
		self.back = tk.Button(
							self.container,
							border=0,
							text='Back',
							background='#121212',
							activebackground='#121212',
							activeforeground='white',
							font = self.appHighlightFont,
							foreground='white',
							command=lambda:self.master.show_frame(Frame1)
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

		#username				
		self.username_input = tk.StringVar()
		self.username = UserEntry(
							self.container, 
							placeholder="  Username",
							show=0,
							textvariable=self.username_input,
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

		#password
		self.password = UserEntry(
							self.container, 
							placeholder="  Password",
							show=1,
							textvariable=None,
							id = "password"
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
		
		#contact number
		self.phone = NumberEntry(
							self.container, 
							placeholder="  Contact Number"
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

		#email
		self.email = UserEntry(
							self.container, 
							placeholder="  Email ID",
							show=0,
							textvariable=None,
							id = "email"
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

		def change():
			return self.master.show_frame(Frame1)

		def register():
			#print(data)
			username_check = data.get("username")
			#print("user: ",username_check)
			password_check = data.get("password")
			#print("pass: ",password_check)
			email_check = data.get("email")
			#print()

			count=0
			
		
			print("user: ",username_check)
			print("pass: ",password_check)
			print("email: ",email_check)
			if(username_check!="" and password_check!="" and email_check!=""):
				print("first block")
				change()
			else:
				print("last block")
				self.result['text'] = "Invalid Credentials"	
				

			# if(username_check=="" or password_check!="" or email_check!=""):
			# 	print("0 done")
			# 	self.result['text'] = "Invalid Credentials"
			# elif(username_check!=""):
			# 	result_text = username_check
			# 	print("1 done")
			# 	print(data)
			# 	print(password_check)
			# 	#print(result_text)
			# 	#self.result['text'] = result_text
			# 	count += 1
			# elif(password_check!=""):
			# 	print("2 done")
			# 	result_text = password_check
			# 	#print(result_text)
			# 	#self.result['text'] = result_text
			# 	count += 1
			# elif(email_check!=""):
			# 	print("3 done")
			# 	result_text = email_check
			# 	#print(result_text)
			# 	#self.result['text'] = result_text
			# 	count += 1
			# elif(username_check!="" and password_check!="" and email_check!=""):
			# 	print("last block")
			# 	print(count)
			# 	lambda: self.master.show_frame(Frame1)
				
				
				
			#if(count==3):
					
		


			# if(username_check!=""):
			# 	result_text = username_check
			# 	print(result_text)
			# 	self.result['text'] = result_text
			# else:
			# 	print("else block")
			# 	self.result['text'] = "Invalid Username"
			# if(len(username_check)==0):
			# 	result_text = "Invalid Username"
			# 	print(result_text)
			# 	self.result['text'] = result_text
			# else:
			# 	print(result_text)
			# 	print("reached")
			# 	result_text = data.get("username")
			# 	self.result['text'] = result_text



			#lambda:self.master.show_frame(Frame1)

			
		self.result = tk.Label(
								self.container,
								border=0,
								background='#121212',
								activebackground='#121212',
								foreground='white',
								activeforeground='white',
								#font=appHighlightFont,
							) 
		self.result.grid(row=5, column=0)

		self.btnimg = tk.PhotoImage(file=r'./images/register.PNG')
		self.register = tk.Button(
						self.container,
						border=0,
						background='#121212',
						activebackground='#121212',
						image=self.btnimg,
						command=register
						)
		self.register.grid(row=6, column=0, pady=10)

		self.container.grid(row=0, column=0)

		self.grid_rowconfigure(0, weight=1)
		self.grid_columnconfigure(0, weight=1)


		
