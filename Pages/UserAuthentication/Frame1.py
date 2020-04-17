import tkinter as tk


class Frame1(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self.container = tk.Frame(self, bg='#121212', padx=80, pady=100)

        self.logo = tk.PhotoImage(file=r'C:\Users\adity\PycharmProjects\TK-Player\Pages\UserAuthentication\images\head5.png', height=225, width=360)
        self.labelLogo = tk.Label(self.container, image=self.logo, bd=0)
        self.labelLogo.grid(row=0, column=0)

        self.btnimg = tk.PhotoImage(file=r'C:\Users\adity\PycharmProjects\TK-Player\Pages\UserAuthentication\images\signup6.png')
        self.btnimg2 = tk.PhotoImage(file=r'C:\Users\adity\PycharmProjects\TK-Player\Pages\UserAuthentication\images\login.png')

        from .Frame3 import Frame3
        self.login = tk.Button(
            self.container,
            border=0,
            background='#121212',
            activebackground='#121212',
            image=self.btnimg2,
            command=lambda: self.master.show_frame(Frame3)
        )
        self.login.grid(row=2, column=0, pady=10)

        from .Frame2 import Frame2
        self.login = tk.Button(
            self.container,
            border=0,
            background='#121212',
            activebackground='#121212',
            image=self.btnimg,
            command=lambda: self.master.show_frame(Frame2)
        )
        self.login.grid(row=1, column=0)

        self.container.grid(row=0, column=0, sticky='nsew')

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
