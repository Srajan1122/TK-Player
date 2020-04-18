class Playlist(tk.Frame):
    def __init__(self , master , *args , **kwargs):
        super().__init__(master)
        self.pack()
        self['background'] = '#000000'
        self['padx'] = 25
        self['pady'] = 25


    def playfromPlaylist(self,playlist):
        pass