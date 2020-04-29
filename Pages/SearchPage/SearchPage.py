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

        # self.filterFrame = FilterFrame(self.contentFrame,data=self.data())
        # print("\nMai andar wala data hoon\n", data,"\nAndar Wala data Khatam")
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
        # from Database.Database import all_songs
        # info = [
        #     {
        #         'genre': 'Workout',
        #         'location': 'https://firebasestorage.googleapis.com/v0/b/one-more-tk.appspot.com/o/tracks%2FThe%20Mission.mp3?alt=media&token=e549651c-c737-41d8-8eb5-9fd2fb06cc7e',
        #         'title': 'The Mission',
        #         'artist': 'Dread Pitt'
        #     },
        #     {
        #         'genre': 'WorkIn',
        #         'location': 'https://firebasestorage.googleapis.com/v0/b/one-more-tk.appspot.com/o/tracks%2FThe%20Mission.mp3?alt=media&token=e549651c-c737-41d8-8eb5-9fd2fb06cc7e',
        #         'title': 'The Kotkar',
        #         'artist': 'Dead Pitt'
        #     }

        # ]
        all_songs= get_all_tracks()
        # print(all_songs)
        return all_songs
    
    def searchFunc(self, data):
        if data==None:
            # print("Mai yaha se None bhej raha hoon")
            return None
        else:
            matchingSongs.clear()
            # print("searchFunc started")
            # print(self.songs)
            user_input = data
            # print(user_input)

            # if not user_input:
            # 	return
            # print("first check done")
            # print(songs)
            song_list = self.listOfSongs()
            for i in range(len(song_list)):
                # print("\nuser input",data,"\ncurrent song\n",song_list[i]['title'])
                input_matcher = re.search(
                    user_input.upper(),
                    song_list[i]['title'].upper()
                )
                # print(input_matcher)
                if input_matcher:
                    matchingSongs.append(song_list[i])
            # print(matchingSongs)
            if not matchingSongs:
                data=['not found']
                return data
            else:
                return matchingSongs
