import tkinter as tk


class MenuFrame(tk.Frame):
    def __init__(self, master, title, album, artist, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self['background'] = '#181818'

        self.menu_image = tk.PhotoImage(file=r'images/menu_icon.png')

        # self.menuButton = tk.Button(self,
        #                             image=self.menu_image,
        #                             relief=tk.FLAT,
        #                             bd=0,
        #                             background='#181818',
        #                             activebackground='#333333')

        self.title = "Title: {}".format(title)
        self.artist = "Artist: {}".format(artist)
        self.album = "Album: {}".format(album)
        self.menuButton = tk.Menubutton(
                                self,
                                image=self.menu_image,
                                bd=0,
                                background="#181818",
                                activebackground="#181818",
                                direction=tk.LEFT
                            )
        self.menuButton.menu = tk.Menu(
                                    self.menuButton,
                                    tearoff=0,
                                    background="#404040",
                                    activebackground="#404040",
                                    foreground="white",
                                    activeforeground="white",
                                    bd=0
                                )
        self.menuButton['menu'] = self.menuButton.menu
        self.menuButton.menu.add_command(label=self.title, command=None)
        self.menuButton.menu.add_command(label=self.artist, command=None)
        self.menuButton.menu.add_command(label=self.album, command=None)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.menuButton.bind('<Button-1>', self.master.click)

        self.bind('<Button-1>', self.master.click)
