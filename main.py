import tkinter as tk
from Base.top import Top
from Base.bottom import Bottom
from Pages.UserAuthentication.AuthBase import AuthBase


class Container(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, bg='white', *args, **kwargs)

        self.top = Top(self)
        self.bottom = Bottom(self)

        self.top.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W + tk.E)
        self.bottom.grid(row=1, column=0, sticky=tk.N + tk.S + tk.W + tk.E)

        self.grid_rowconfigure(0, weight=8)
        self.grid_rowconfigure(1, weight=2)
        self.grid_columnconfigure(0, weight=1)


class Root(tk.Tk):
    def __init__(self, data, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        print(data)
        self.title('TK-Player')
        app_icon = tk.PhotoImage(file=r"images\app_64.png")
        self.iconphoto(False, app_icon)

        container = Container(self)
        container.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W + tk.E)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.state('zoomed')


if __name__ == '__main__':
    if True:
        root = Root(data='')
        root.mainloop()
    else:
        login = AuthBase()
        login.mainloop()


