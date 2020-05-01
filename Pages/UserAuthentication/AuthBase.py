#-----Base for Authentication-----

import tkinter as tk
from .Frame1 import Frame1
from .Frame2 import Frame2
from .Frame3 import Frame3
from .Frame4 import Frame4
from main import Root

#Layout of Base
class AuthBase(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Login')
        self.state('zoomed')

        self.frame = AuthFrame(self)
        self.frame.grid(row=0, column=0, sticky='nsew')

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
      

#Frame of Base
class AuthFrame(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        #Canvas for Background Image
        canvas = tk.Canvas(self, width=1920, height=1280, bd=0)
        self.bg = tk.PhotoImage(file=r"images\bg4.png")
        canvas.create_image(0, 0, anchor=tk.NW, image=self.bg)
        canvas.grid(row=0, column=0)

        #Frames
        self.frames = {}

        for F in (Frame1, Frame2, Frame3, Frame4):
            frame = F(self)
            self.frames[F] = frame
            frame.grid(row=0, column=0)

        #Close Button
        self.close = tk.PhotoImage(file=r"images\close3.png")
        self.button = tk.Button(
            self,
            bd=0,
            image=self.close,
            background='#121212',
            foreground='white',
            command=self.master.destroy)
        self.button.grid(row=0, column=0, pady=3, padx=3, sticky='ne')

        #Frame grid and configurations
        self.show_frame(Frame1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    #Function for displaying frames
    def show_frame(self, context):
        frame  = context(self)
        frame.grid(row=0, column=0)
        # framee = self.frames[context]
        frame.tkraise()

    #Function for entering Homepage
    def login(self,user_object):
      
        """
            Check different condition for authentication
        """
        if False:
            return

      

        self.master.destroy()
        main = Root(data=user_object)
        main.mainloop()

    def openFrame4(self):
        framee = self.frames[Frame4]
        framee.tkraise()
    def openFrame3(self):
        framee = self.frames[Frame3]
        framee.tkraise()


