import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
class UserPage(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self['background'] = '#000000'
       
        f = open('user')
        x = f.readlines()[0]
        from Database.Database import get_user
        myobject  = get_user(x)
        fontStyle = tkFont.Font(family="Lucida Grande", size=20 )
        Dynamic_Font = tkFont.Font(family="Lucida Grande", size=20 , weight = 'bold' )
        Your_Profile = tk.Label(self, text = myobject['display_name']+"'s Profile" ,  bg = 'black', fg = 'white' ) 
        Your_Profile.grid(row = 0 , column = 2 )
        Your_Profile.config(font=('Comic Sans MS', 30, 'bold'))
        l1 = tk.Label(self, text = "Name :-" ,  bg = 'black', fg = 'white', font = fontStyle , padx = 20 ) 
        l2 = tk.Label(self, text = "Email : -" ,  bg = 'black', fg = 'white', font = fontStyle ) 
        l3 = tk.Label(self, text = "Contact No. :-" ,  bg = 'black', fg = 'white', font = fontStyle ) 
        l4 = tk.Label(self, text = "Password : -" ,  bg = 'black', fg = 'white', font = fontStyle ) 
        # l1.config(font=( 20, 'bold'))
        # l2.config(font=( 20, 'bold'))
        # l3.config(font=(20))
        # l4.config(font=(20))
        name = tk.Label(self, text = myobject['display_name'] ,  bg = 'black', fg = 'white' , padx = 20, font = Dynamic_Font)
        email = tk.Label(self, text = myobject['email'] ,  bg = 'black', fg = 'white' , padx = 20, font = Dynamic_Font )
        PhoneNo = tk.Label(self, text = myobject['phone_number'][3:] ,  bg = 'black', fg = 'white' , padx = 20, font = Dynamic_Font ) 
        Password = tk.Label(self, text = myobject['password'] ,  bg = 'black', fg = 'white' , padx = 20, font = Dynamic_Font ) 

        
        # grid method to arrange labels in respective 
        # rows and columns as specified 
        
        l1.grid(row = 1, column = 1,padx=10, pady=10) 
        l2.grid(row = 2, column = 1, padx=10, pady=10) 
        l3.grid(row = 3, column = 1, padx=10, pady=10) 
        l4.grid(row = 4, column = 1,padx=10, pady=10) 
        name.grid(row = 1, column = 2,padx=10, pady=10) 
        email.grid(row = 2, column = 2,padx=10, pady=10) 
        PhoneNo.grid(row = 3, column =2,padx=10, pady=10) 
        Password.grid(row = 4, column = 2,padx=10, pady=10) 

        # entry widgets, used to take entry from user 
        # e1 = tk.Entry(self) 
        # e2 = tk.Entry(self) 
        
        # # this will arrange entry widgets 
        # e1.grid(row = 0, column = 1, pady = 2) 
        # e2.grid(row = 1, column = 1, pady = 2) 
  
       