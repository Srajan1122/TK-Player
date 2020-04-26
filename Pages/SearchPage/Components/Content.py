import tkinter as tk
from Pages.Resource.VerticalScrollableFrame import ScrollableFrame
from .MusicFrame import MusicFrame

class Content(tk.Frame):
    def __init__(self,master,data,*args,**kwargs):
        tk.Frame.__init__(self,master,*args,**kwargs)

        self.scrollableFrame = ScrollableFrame(self)

        for j,i in enumerate(data):
            self.music = MusicFrame(self.scrollableFrame.scrollable_frame,
                                        title=i['title'],
                                        album=i['genre'],
                                        artist=i['artist'],
                                        url=i['location'])
            self.line = tk.Frame(self.scrollableFrame.scrollable_frame,
                                    bg='#333333')
            self.music.grid(row=j*2, column=0, sticky='nsew', padx=(30, 15))
            self.line.grid(row=j*2 + 1 ,column =0 ,sticky='nsew')
        
        self.scrollableFrame.grid(row=0,column=0,sticky='nsew')
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)