import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from PIL import ImageTk, Image

class UserPage(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self['background'] = '#000000'
       
        f = open('user')
        x = f.readlines()[0]
        from Database.Database import get_user
        myobject  = get_user(x)
        fontStyle = tkFont.Font(family="Lucida Grande", size=18, weight='bold' )
        Dynamic_Font = tkFont.Font(family="Lucida Grande", size=20 , weight = 'bold' )

        #Frames
        self.frame1 = tk.Frame(self, bg="#000000")
        self.frame1.grid(row=0,column=0,padx=5,pady=5)

        self.frame2 = tk.Frame(self, bg="#000000")
        self.frame2.grid(row=0,column=1,padx=5,pady=5)


        #Logo
        self.logo = self.prepare_image('radio2.png', 256, 256)
        self.my_logo = tk.Label(self.frame2 , image = self.logo, bg = 'black')
        self.my_logo.grid(row = 0 , column  = 2, padx=30,pady=30)
        
        #Profile
        self.profile_icon = self.prepare_image('profile.png',50,360)
        self.your_profile = tk.Label(
                                self.frame1, image=self.profile_icon,
                                bg="#000000"
                            )
        self.your_profile.grid(row=0, column=1,padx=20,pady=20)
        
        #Name
        self.name_icon = self.prepare_image('name.png',45,135)
        self.nameLabel = tk.Label(
                                self.frame1, image=self.name_icon,
                                bg="#000000"
                            )
        self.nameLabel.grid(row=1, column=0, padx=20, pady=20)
        self.name = tk.Label(
                        self.frame1, text=myobject['display_name'],
                        bg="#000000", fg="#FFFFFF", font=fontStyle
                    )
        self.name.grid(row=1, column=1, padx=20, pady=20)

        #Email
        self.email_icon = self.prepare_image('email.png',45,135)
        self.emailLabel = tk.Label(
                                self.frame1, image=self.email_icon,
                                bg="#000000"
                            )
        self.emailLabel.grid(row=2, column=0, padx=20, pady=20)
        self.email = tk.Label(
                        self.frame1, text=myobject['email'],
                        bg="#000000", fg="#FFFFFF", font=fontStyle
                    )
        self.email.grid(row=2, column=1, padx=20, pady=20)

        #Contact No.
        self.contact_icon = self.prepare_image('contact.png',45,135)
        self.contactLabel = tk.Label(
                                self.frame1, image=self.contact_icon,
                                bg="#000000"
                            )
        self.contactLabel.grid(row=3, column=0, padx=20, pady=20)
        self.contact = tk.Label(
                        self.frame1, text=myobject['phone_number'],
                        bg="#000000", fg="#FFFFFF", font=fontStyle
                    )
        self.contact.grid(row=3, column=1, padx=20, pady=20)

        #Password
        self.password_icon = self.prepare_image('password.png',45,135)
        self.passwordLabel = tk.Label(
                                self.frame1, image=self.password_icon,
                                bg="#000000"
                            )
        self.passwordLabel.grid(row=4, column=0, padx=20, pady=20)
        self.password = tk.Label(
                        self.frame1, text=myobject['password'],
                        bg="#000000", fg="#FFFFFF", font=fontStyle
                    )
        self.password.grid(row=4, column=1, padx=20, pady=20)

        #configure
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0,1), weight=1)

    @staticmethod
    def prepare_image(filename, height, width):
        icon = Image.open('images/'+filename)
        icon = icon.resize((width, height), Image.ANTIALIAS)
        icon = ImageTk.PhotoImage(icon)
        return icon



        # Your_Profile = tk.Label(self, text = myobject['display_name']+"'s Profile" ,  bg = 'black', fg = 'white' ) 
        # Your_Profile.grid(row = 0 , column = 2 )
        # Your_Profile.config(font=('Comic Sans MS', 30, 'bold'))
        # l1 = tk.Label(self, text = "Name :-" ,  bg = 'black', fg = 'white', font = fontStyle , padx = 20 ) 
        # l2 = tk.Label(self, text = "Email : -" ,  bg = 'black', fg = 'white', font = fontStyle ) 
        # l3 = tk.Label(self, text = "Contact No. :-" ,  bg = 'black', fg = 'white', font = fontStyle ) 
        # l4 = tk.Label(self, text = "Password : -" ,  bg = 'black', fg = 'white', font = fontStyle ) 
        # # l1.config(font=( 20, 'bold'))
        # # l2.config(font=( 20, 'bold'))
        # # l3.config(font=(20))
        # # l4.config(font=(20))
        # name = tk.Label(self, text = myobject['display_name'] ,  bg = 'black', fg = 'white' , padx = 20, font = Dynamic_Font)
        # email = tk.Label(self, text = myobject['email'] ,  bg = 'black', fg = 'white' , padx = 20, font = Dynamic_Font )
        # PhoneNo = tk.Label(self, text = myobject['phone_number'][3:] ,  bg = 'black', fg = 'white' , padx = 20, font = Dynamic_Font ) 
        # Password = tk.Label(self, text = myobject['password'] ,  bg = 'black', fg = 'white' , padx = 20, font = Dynamic_Font ) 

        
        # # grid method to arrange labels in respective 
        # # rows and columns as specified 
        
        # l1.grid(row = 1, column = 1,padx=10, pady=10) 
        # l2.grid(row = 2, column = 1, padx=10, pady=10) 
        # l3.grid(row = 3, column = 1, padx=10, pady=10) 
        # l4.grid(row = 4, column = 1,padx=10, pady=10) 
        # name.grid(row = 1, column = 2,padx=10, pady=10) 
        # email.grid(row = 2, column = 2,padx=10, pady=10) 
        # PhoneNo.grid(row = 3, column =2,padx=10, pady=10) 
        # Password.grid(row = 4, column = 2,padx=10, pady=10) 

        # entry widgets, used to take entry from user 
        # e1 = tk.Entry(self) 
        # e2 = tk.Entry(self) 
        
        # # this will arrange entry widgets 
        # e1.grid(row = 0, column = 1, pady = 2) 
        # e2.grid(row = 1, column = 1, pady = 2) 
  
       