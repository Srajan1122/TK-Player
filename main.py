import tkinter as tk
from Base import top
from Base.bottom import Bottom
from threading import Thread
from ActivityIndicator.Activity_Indicator import ImageLabel
import time


class Splash(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Splash")
        self['bg'] = 'black'

        lbl = ImageLabel(self)
        lbl['bd'] = 0
        lbl['bg'] = 'black'
        lbl.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W + tk.E)

        self.logo = tk.PhotoImage(file=r'images\loading.png', height=150, width=360)
        self.labelLogo = tk.Label(self, image=self.logo, bd=0, bg='black')
        self.labelLogo.grid(row=1, column=0, sticky=tk.N + tk.S + tk.W + tk.E)
        self.grid_columnconfigure(0, weight=1)
        self.state('zoomed')
        self.overrideredirect(True)

        lbl.load('ActivityIndicator/Activity.gif')


class Container(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, bg='white', *args, **kwargs)

        self.top = top.Top(self)
        self.bottom = Bottom(self)

        from Base.listOfPage import bottomInstance
        bottomInstance.append(self.bottom)

        self.top.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W + tk.E)
        self.bottom.grid(row=1, column=0, sticky=tk.N + tk.S + tk.W + tk.E)

        self.grid_rowconfigure(0, weight=8)
        self.grid_rowconfigure(1, weight=2)
        self.grid_columnconfigure(0, weight=1)


class Root(tk.Tk):
    def __init__(self, data, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        def TK_player():
            self.withdraw()
            print('befire')

            print('aim teher')
            self.title('TK-Player')
            app_icon = tk.PhotoImage(file=r"images\app_64.png")
            self.iconphoto(False, app_icon)

            container = Container(self)
            container.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W + tk.E)

            self.grid_columnconfigure(0, weight=1)
            self.grid_rowconfigure(0, weight=1)
            self.state('zoomed')

        def Splash_Screen():
            splash = Splash(self)

            def myfun():
                splash.destroy()
                self.deiconify()

            splash.after(15000, myfun)
            time.sleep(15000)

        Thread(target=TK_player).start()
        Thread(target=Splash_Screen).start()

        print(data)


if __name__ == '__main__':
    from Database.Database import get_user
    # from ActivityIndicator.Activity_Indicator import ImageLabel

    from os import path

    if path.exists('user'):
        f = open('user', 'r')
        doc = get_user(f.readline())
        f.close()

        root = Root(data=doc)

        root.mainloop()
    else:
        from Pages.UserAuthentication.AuthBase import AuthBase

        login = AuthBase()
        login.mainloop()
