import tkinter as tk
from .Frame1 import Frame1
from .Frame2 import Frame2
from .Frame3 import Frame3


class AuthBase(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Login')
        self.state('zoomed')

        self.frame = AuthFrame(self)
        self.frame.grid(row=0, column=0, sticky='nsew')

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


class AuthFrame(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        canvas = tk.Canvas(self, width=1920, height=1280, bd=0)
        self.bg = tk.PhotoImage(file=r"images\bg4.png")
        canvas.create_image(0, 0, anchor=tk.NW, image=self.bg)
        canvas.grid(row=0, column=0)

        self.frames = {}

        for F in (Frame1, Frame2, Frame3):
            frame = F(self)
            self.frames[F] = frame
            frame.grid(row=0, column=0)

        # self.logo = tk.PhotoImage(file=r'2.PNG',height=36,width=55)
        self.button = tk.Button(
            self,
            bd=0,
            text='X',
            background='#121212',
            foreground='white',
            command=self.master.destroy)
        self.button.grid(row=0, column=0, sticky='ne')

        self.show_frame(Frame1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def show_frame(self, context):
        framee = self.frames[context]
        framee.tkraise()

    def login(self):
        from main import Root
        print('help')
        """
            Check different condition for authentication
        """
        if False:
            return

        self.user = {
            'name': 'srajan',
            'age': 18
        }

        self.master.destroy()
        main = Root(data=self.user)
        main.mainloop()
