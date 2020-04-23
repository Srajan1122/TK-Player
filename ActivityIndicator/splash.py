import tkinter as tk
import time
from Activity_Indicator import ImageLabel

class Splash(tk.Toplevel):
	def __init__(self,parent):
		tk.Toplevel.__init__(self,parent)
		self.title("Splash")
		lbl = ImageLabel(self)
		lbl.pack()
		lbl.load('Activity.gif')
		## required to make window show before the program gets to the mainloop
		
class App(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		self.withdraw()
		def myfun():
			print('befire')
			splash.destroy()
			print('aim teher')
			self.title("Main Window")
			# time.sleep(7)
			print('i ma deiconify')
			self.deiconify()
			print('deiconified')

		splash = Splash(self)
		splash.after(6000,myfun)
		
		## simulate a delay while loading
		
		splash.mainloop()

		## setup stuff goes here
		

		## finished loading so destroy splash
		# splash.destroy()

		## show window again
		

if __name__ == "__main__":
	app = App()
	
	app.mainloop()