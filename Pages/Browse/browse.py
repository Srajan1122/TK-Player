import tkinter as tk
from PIL import ImageTk, Image


class Browse(tk.Frame):
	def __init__(self, master, controller, *args, **kwargs):
		tk.Frame.__init__(self, master, *args, **kwargs)
		self['background'] = '#212121'

		self.logo = self.prepare_image('about_us3.png',513,1100)
		self.my_logo = tk.Label(self , image = self.logo, bg = '#212121', anchor=tk.W)
		self.my_logo.grid(row = 0 , column  = 0, padx=30,pady=30)

		self.grid_rowconfigure(1, weight=1)
		self.grid_columnconfigure(0, weight=1)

	@staticmethod
	def prepare_image(filename, height, width):
		icon = Image.open('images/'+filename)
		icon = icon.resize((width, height), Image.ANTIALIAS)
		icon = ImageTk.PhotoImage(icon)
		return icon


