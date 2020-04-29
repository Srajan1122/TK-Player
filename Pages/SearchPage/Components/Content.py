import tkinter as tk
from Pages.Resource.VerticalScrollableFrame import ScrollableFrame
from .MusicFrame import MusicFrame
import pyglet
import tkinter.font as tkfont

class Content(tk.Frame):
    def __init__(self,master,controller,data,*args,**kwargs):
        tk.Frame.__init__(self,master,*args,**kwargs)
        pyglet.font.add_file('fonts/Play/Play-Bold.ttf')
        play = tkfont.Font(family="Play", size=15, weight="bold")
        self.scrollableFrame = ScrollableFrame(self)
        self.scrollableFrame.scrollable_frame.config(background='#181818')
        # print("\nMai content",data,"\nMai content khatam\n")
        if data==None:
            pass
        else:
            if len(data) == 1 and data[0] == 'not found':
                self.label = tk.Label(self,
                                    text='No Results Found\nTry Something Else',
                                    background='#181818',
                                    foreground='white',
                                    font=play
                                    )
                self.label.grid(row=0, column=0)
            elif len(data) == 0:
                self.label = tk.Label(self,
                                    text='Search Results Will appear here',
                                    background='#181818',
                                    foreground='#999999',
                                    font=self.support
                                    )
                self.label.grid(row=0, column=0)
            else:
                for j,i in enumerate(data):
                    self.music = MusicFrame(self.scrollableFrame.scrollable_frame,
                                                controller,
                                                title=i['title'],
                                                album=i['genre'],
                                                artist=i['artist'],
                                                url=i['location'])
                    self.line = tk.Frame(self.scrollableFrame.scrollable_frame,
                                            bg='#333333')
                    self.music.grid(row=j*2, column=0, sticky='nsew', padx=(30, 15))
                    self.line.grid(row=j*2 + 1 ,column =0 ,sticky='nsew',  padx=(30, 15))
        
        # self.scrollableFrame.grid(row=0,column=0,sticky='nsew')
        # self.scrollableFrame.grid_rowconfigure(0,weight=1)
        # self.scrollableFrame.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)