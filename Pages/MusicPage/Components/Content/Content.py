import tkinter as tk
import tkinter.font as tkfont

from Pages.MusicPage.Components.Content.Components.MusicFrame import MusicFrame
from Pages.Resource.VerticalScrollableFrame import ScrollableFrame


class Content(tk.Frame):
    count = 0

    def __init__(self, master, data, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, *kwargs)
        self['background'] = '#181818'
        self.count = 0
        self.data = data

        self.support = tkfont.Font(family="Pragatic Narrow", size=12, weight="bold")

        self.scrollable = ScrollableFrame(self)
        self.scrollable.scrollable_frame.config(background='#181818')
        from Base.listOfPage import musicList
        musicList.append({self.master: []})

        if len(data) == 1 and data[0] == 'not found':
            self.label = tk.Label(self,
                                  text='Song not in the list',
                                  background='#181818',
                                  foreground='#999999',
                                  font=self.support
                                  )
            self.label.grid(row=0, column=0)
        elif len(data) == 0:
            self.label = tk.Label(self,
                                  text='Your liked song will appear here',
                                  background='#181818',
                                  foreground='#999999',
                                  font=self.support
                                  )
            self.label.grid(row=0, column=0)
        else:
            for j, i in enumerate(self.data):
                self.music = MusicFrame(self.scrollable.scrollable_frame,
                                        title=i['title'],
                                        album=i['genre'],
                                        artist=i['artist'],
                                        url=i['location'])
                self.line = tk.Frame(self.scrollable.scrollable_frame,
                                     bg='#333333')
                self.music.grid(row=self.count, column=0, sticky='nsew', padx=(30, 15))
                self.count += 1
                self.line.grid(row=self.count, column=0, sticky='nsew', padx=(30, 15))
                self.count += 1
                musicList[Content.count][self.master].append(self.music)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        Content.count += 1
