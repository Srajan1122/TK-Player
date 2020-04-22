import tkinter as tk


class FilterFrame(tk.Frame):
    def __init__(self, master, *args, data, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self['background'] = 'black'
        self['height'] = 40

        self.button = tk.Button(self, text='clear', command=self.clear)
        self.button.grid(row=0, column=0, sticky='nsew')

        self.button2 = tk.Button(self, text='fill', command=self.fill)
        self.button2.grid(row=0, column=1, sticky='nsew')

        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

    def clear(self):
        from .Content.Content import Content
        self.content = Content(self.master.master, data=[])
        self.content.grid(row=3, column=0, sticky='nsew')
        self.content.tkraise()

    def fill(self):
        self.master.master.content.tkraise()
