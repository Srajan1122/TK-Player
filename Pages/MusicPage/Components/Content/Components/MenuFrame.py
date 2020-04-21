import tkinter as tk


class MenuFrame(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self['background'] = '#181818'

        self.menu_image = tk.PhotoImage(file=r'images/menu_icon.png')

        self.menuButton = tk.Button(self,
                                    image=self.menu_image,
                                    relief=tk.FLAT,
                                    bd=0,
                                    background='#181818',
                                    activebackground='#333333')
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.menuButton.bind('<Button-1>', self.master.click)

        self.bind('<Button-1>', self.master.click)
