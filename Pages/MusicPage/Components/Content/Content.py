import tkinter as tk

from Pages.MusicPage.Components.Content.Components.MusicFrame import MusicFrame
from Pages.Resource.VerticalScrollableFrame import ScrollableFrame


class Content(tk.Frame):
    count = 0

    def __init__(self, master, data, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, *kwargs)
        self['background'] = 'red'
        self.count = 0
        self.data = data
        print(self.data)

        self.scrollable = ScrollableFrame(self)
        from Base.listOfPage import musicList
        musicList.append({self.master: []})

        for k in range(20):
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
