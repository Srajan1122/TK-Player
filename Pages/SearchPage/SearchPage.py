import tkinter as tk
# from .Components.FilterFrame import FilterFrame
from .Components.TitleFrame import TitleFrame
from .Components.MusicFrame import MusicFrame
from .Components.Content import Content
import pyglet
import tkinter.font as tkfont
import re
from Database.Database import get_all_tracks

global matchingSongs
matchingSongs = []

class SearchPage(tk.Frame):
    def __init__(self, master, controller, data=None, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self['background'] = "#000000"

        self.titleFrame = tk.Frame(self,background="#999999")
        self.contentFrame = tk.Frame(self,background="#181818")

        pyglet.font.add_file('fonts/Play/Play-Bold.ttf')
        play = tkfont.Font(family="Play", size=35, weight="bold")
        
        self.heading = tk.Label(self.titleFrame,text="Search",bg="#000000",foreground='white',font=play,padx=20)

       
      
        self.labelTitleFrame = TitleFrame(self.contentFrame)

        data = self.searchFunc(data)
        self.content = Content(self.contentFrame,controller,data=data)


        self.titleFrame.grid(row=0, column=0 , sticky='nsw')
        self.heading.grid(row=0, column=0 , sticky='nsew')
        self.contentFrame.grid(row=1,column=0,sticky='nsew')
        # self.filterFrame.grid(row=0,column=0,sticky='nsew')
        self.labelTitleFrame.grid(row=0,column=0,sticky='nsew')
        self.content.grid(row=1,column=0,sticky='nsew')

        self.titleFrame.grid_rowconfigure(0,weight=1)
        self.titleFrame.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=10)
        self.grid_columnconfigure(0,weight=1)
        # self.contentFrame.grid_rowconfigure(0,weight=2)
        self.contentFrame.grid_rowconfigure(0,weight=1)
        self.contentFrame.grid_rowconfigure(1,weight=55)
        self.contentFrame.grid_columnconfigure(0,weight=1)
        # self.contentFrame.grid_columnconfigure(0,weight=1)

    def listOfSongs(self):
       
        all_songs= get_all_tracks()
       
        return all_songs
    
    def searchFunc(self, data):
        if data==None:
           
            return None
        else:
            matchingSongs.clear()
           
            user_input = data
           
            song_list = self.listOfSongs()
            for i in range(len(song_list)):
              
                input_matcher = re.search(
                    user_input.upper(),
                    song_list[i]['title'].upper()
                )
               
                if input_matcher:
                    matchingSongs.append(song_list[i])
            
            if not matchingSongs:
                data=['not found']
                return data
            else:
                return matchingSongs
