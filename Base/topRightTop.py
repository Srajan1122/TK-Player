import tkinter as tk
from PIL import Image, ImageTk
from tkinter import font
from .listOfPage import pages, rightPage, incrementCount, getCount, resetCount
from Pages.UserPage.UserPage import UserPage
import sys


class UserEntry(tk.Entry):
    def __init__(self, master, placeholder, textvariable, songDict, *args, **kwargs):
        tk.Entry.__init__(self, master, *args, **kwargs)

        # placeholder function
        def default_placeholder(self):
            self.insert(0, placeholder)

        default_placeholder(self)

        # font size, style
        self.appHighlightFont = font.Font(
            family='lineto circular',
            size=11,
        )

        # font color
        self.default_fg = 'black'
        self.input_fg = 'white'

        # properties of Entry widget
        self['background'] = 'white'
        self['foreground'] = self.default_fg
        self['insertbackground'] = 'black'
        self['font'] = self.appHighlightFont
        self['border'] = 0

        # function called on focusing
        def foc_in(event):
            if self.get() == placeholder:
                self['foreground'] = self.default_fg
                self.delete(0, 100)
            self['foreground'] = 'black'
            self['textvariable'] = textvariable

        # function called when not focusing
        def foc_out(event):
            self['foreground'] = self.default_fg
            # print(self.get())
            if not self.get():
                default_placeholder(self)
            else:
                self.insert(0, self['textvariable'])

        # def key(events)
        self.bind("<FocusIn>", lambda e: foc_in(e))
        self.bind("<FocusOut>", lambda e: foc_out(e))


class IconButton(tk.Button):
    def __init__(self, master, controller, text, image, command, *args, **kwargs):
        tk.Button.__init__(self, master, *args, **kwargs)

        self.appHighlightFont = font.Font(family='lineto circular', size=11, weight='bold')
        self['foreground'] = 'white'
        self['background'] = '#000000'
        self['border'] = 0
        self['activebackground'] = '#000000'
        # self['activeforeground'] = 'white'
        self['padx'] = 10
        self['pady'] = 5
        self['image'] = image
        self['compound'] = tk.LEFT
        self['text'] = text
        self['anchor'] = tk.W
        self['font'] = self.appHighlightFont
        self['command'] = command
        # self['width']=100


class TopRightTop(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self['background'] = '#000000'

        f = open('user')
        x = f.readlines()[0]
        from Database.Database import get_user
        myobject  = get_user(x)

        self.back = Back(self)
        self.search = tk.Frame(self, bg='#000000')
        self.name = tk.Frame(self, bg='#000000')
        # self.dropdown = tk.Frame(self, bg='pink')
        self.min_max_cross = MinMaxCross(self)

        self.filter = UserEntry(
            self.search, placeholder="  Search",
            textvariable=None,
            songDict=None
        )
        self.filter.grid(
            row=0, column=0, sticky='nsew', padx=10,
            pady=4,
            ipadx=20,
            ipady=5
        )
        self.filter.bind("<Return>",lambda e: self.sendSearchData(e))

        # User_button
        # self.name = self.user_data
        # print(self.name)
        self.appHighlightFont = font.Font(family='lineto circular', size=11, weight='bold')
        self.appHighlightFont2 = font.Font(family='lineto circular', underline=1, size=11, weight='bold')
        self.user_icon = tk.PhotoImage(file=r".\Images\user2.png", height=25, width=25)
        self.userButton = IconButton(self.name,
                                     master, text=myobject['display_name'],
                                     image=self.user_icon,
                                     command=lambda: self.master.master.show_frame(UserPage)
                                     )
        self.userButton.bind("<Enter>", lambda e: self.userButtonHighlight(e))
        self.userButton.bind("<Leave>", lambda e: self.userButtonLeave(e))

        # user_dropdown
        self.down = tk.PhotoImage(file=r".\Images\down_arrow.png", width=25, height=25)
        self.user_menu = tk.Menubutton(
            self.name,
            image=self.down,
            background="#000000",
            activebackground="#000000",
            bd=0, padx=2, pady=0
        )
        self.user_menu.menu = tk.Menu(
            self.user_menu,
            tearoff=0,
            background='#35363a', activebackground='#404040',
            foreground='#a8a8a8', activeforeground='white',
            bd=0,
            font=self.appHighlightFont
        )
        self.user_menu['menu'] = self.user_menu.menu
        self.user_menu.menu.add_command(label='Logout', command=self.logout)
        self.user_menu.menu.add_command(label="Settings")

        self.user_menu.grid(row=0, column=2, sticky='nsew', padx=10, pady=0)
        self.userButton.grid(row=0, column=1, sticky='nsew', ipady=0)
        self.back.grid(row=0, column=0, sticky='nsew')
        self.search.grid(row=0, column=1, sticky='nsew')
        self.name.grid(row=0, column=2, sticky='nsew')
        # self.dropdown.grid(row=0, column=3, sticky='nsew')
        self.min_max_cross.grid(row=0, column=3, sticky='nsew')

        self.name.grid_rowconfigure(0, weight=1)
        self.name.grid_columnconfigure(0, weight=1)

        self.rowconfigure(0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=10)
        self.grid_columnconfigure(2, weight=5)
        # self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(3, weight=4)
    
    def sendSearchData(self, event):
        print(self.filter.get())

    def userButtonHighlight(self, event):
        self.userButton['bg'] = "#000000"
        self.userButton['font'] = self.appHighlightFont2

    def userButtonLeave(self, event):
        self.userButton['bg'] = "#000000"
        self.userButton['font'] = self.appHighlightFont

    def logout(self):
        import os
        from Database.Database import sign_out
        sign_out()
        from Base.listOfPage import current_playing
        current_playing[0].play_button.click()
        self.master.master.master.master.destroy()
        from Pages.UserAuthentication.AuthBase import AuthBase
        login = AuthBase()
        login.mainloop()


class Back(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self['background'] = '#000000'

        self.leftImage = tk.PhotoImage(file=r'.\images\left_arrow.png')
        self.rightImage = tk.PhotoImage(file=r'.\images\right_arrow.png')

        self.left = ArrowButton(self, image=self.leftImage, command=self.left)
        self.right = ArrowButton(self, image=self.rightImage, command=self.right)

        self.left.grid(row=0, column=0, sticky='ew')
        self.right.grid(row=0, column=1, sticky='ew')

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

    def left(self):
        if len(pages) > 0:
            if len(pages) == 1:
                return
            else:
                r = pages.pop(len(pages) - 1)
                rightPage.append(r)
                frame = pages[len(pages) - 1]

                self.master.master.master.show_frame_directly(frame)

    def right(self):
        if len(rightPage) < 1:
            return

        c = getCount()
        if c > len(rightPage):
            return
        frame = rightPage[len(rightPage) - c]
        pages.append(frame)
        incrementCount()
        self.master.master.master.show_frame_directly(frame)


class ArrowButton(tk.Button):
    def __init__(self, master, *args, **kwargs):
        tk.Button.__init__(self, master, *args, **kwargs)
        self['relief'] = tk.FLAT
        self['background'] = '#000000'
        self['foreground'] = 'white'
        self['activebackground'] = '#000000'
        self['activeforeground'] = 'white'
        self['borderwidth'] = 0


class MinMaxCross(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self['background'] = '#000000'

        self.min_icon = self.prepare_icon('min.png', 13)
        self.max_icon = self.prepare_icon('max.png', 14)
        self.cross_icon = self.prepare_icon('cross.png', 25)
        self.min = tk.Button(self,
                             bg='#000000',
                             activebackground='#867f7a',
                             height=25,
                             width=35,
                             image=self.min_icon,
                             relief=tk.FLAT,
                             bd=0,
                             command=lambda: self.master.master.master.master.master.wm_state("iconic"))
        self.max = tk.Button(self,
                             image=self.max_icon,
                             bg='#000000',
                             relief=tk.FLAT,
                             height=25,
                             width=35,
                             bd=0,
                             activebackground='#867f7a',
                             command=lambda: self.master.master.master.master.master.state('zoomed'))
        self.cross = tk.Button(self,
                               bg='#000000',
                               activebackground='red',
                               image=self.cross_icon,
                               relief=tk.FLAT,
                               width=35,
                               bd=0,
                               command=lambda: sys.exit())
        self.min.grid(row=0, column=1)
        self.max.grid(row=0, column=2)
        self.cross.grid(row=0, column=3)

        self.min.bind('<Enter>', self.enter)
        self.min.bind('<Leave>', self.leave)
        self.max.bind('<Enter>', self.max_enter)
        self.max.bind('<Leave>', self.max_leave)
        self.cross.bind('<Enter>', self.cross_enter)
        self.cross.bind('<Leave>', self.cross_leave)

        # self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def enter(self, event):
        self.min.config(bg='#867f7a')

    def leave(self, event):
        self.min.config(bg='#000000')

    def max_enter(self, event):
        self.max.config(bg='#867f7a')

    def max_leave(self, event):
        self.max.config(bg='#000000')

    def cross_enter(self, event):
        self.cross.config(bg='red')

    def cross_leave(self, event):
        self.cross.config(bg='#000000')

    @staticmethod
    def prepare_icon(filename, size):
        icon = Image.open('images/' + filename)
        icon = icon.resize((size, size), Image.ANTIALIAS)
        icon = ImageTk.PhotoImage(icon)
        return icon
