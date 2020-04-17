import tkinter as tk
from tkinter import font

class UserEntry(tk.Entry):
    def __init__(self, master, placeholder, *args, **kwargs):
        tk.Entry.__init__(self, master, *args, **kwargs)

        self.placeholder = placeholder
        def default_placeholder(self):
            self.insert(0,self.placeholder)

        self.appHighlightFont = font.Font(
                                family='lineto circular', 
                                size=12, 
                                )

        self.default_fg = '#d3d3d3'
        self.input_fg = 'white'
        
        self['background'] = '#525252'
        self['foreground'] = self.default_fg
        self['insertbackground'] = 'white'

        def foc_in(event):
            if self['foreground'] == self.default_fg:
                if self.get() == placeholder:
                   self.delete(0,100)
            self['foreground'] = 'red'
                               
        def foc_out(event):
            if not self.get():
                default_placeholder(self)
            else:
                insert(0,self.placeholder)

        self.bind("<FocusIn>", lambda e: foc_in(e))
        self.bind("<FocusOut>", lambda e: foc_out(e))

        default_placeholder(self)

        





root = tk.Tk()

entry1 = UserEntry(root, placeholder='aditya')
entry1.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            ipadx=40,
            ipady=10,
            sticky=tk.N + tk.S + tk.E + tk.W
            )
entry1.grid_columnconfigure(0, weight=1)
entry1 = UserEntry(root, placeholder='kotkar')
entry1.grid(
            row=1,
            column=0,
            padx=10,
            pady=10,
            ipadx=40,
            ipady=10,
            sticky=tk.N + tk.S + tk.E + tk.W
            )
entry1.grid_columnconfigure(1, weight=1)
root.mainloop()
