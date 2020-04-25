import tkinter as tk
from Pages.MusicPage.Components.Content.Components.ContentLabel import ContentLabel
from Pages.MusicPage.Components.Content.Components.LikeButton import LikeButton
from Pages.MusicPage.Components.Content.Components.MenuFrame import MenuFrame
from Pages.MusicPage.Components.Content.Components.PlayButton import PlayButton
from PIL import Image, ImageTk
from Music.track import Track


class MusicFrame(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        self.title = kwargs.pop('title')
        self.album = kwargs.pop('album')
        self.url = kwargs.pop('url')
        self.artist = kwargs.pop('artist')
        tk.Frame.__init__(self, master, *args, **kwargs)
        self['background'] = '#181818'
        self['height'] = 40

        self.play_music = None

        self.pause_icon = self.prepare_icon('pause_icon.png', size=25)
        self.music_icon = self.prepare_icon('music_icon.png', size=16)
        self.volume_icon = self.prepare_icon('volume_icon.png', size=25)

        self.iconFrame = tk.Frame(self, bg='#181818')
        self.titleFrame = tk.Frame(self, bg='#181818')
        self.artistFrame = tk.Frame(self, bg='#181818')
        self.albumFrame = tk.Frame(self, bg='#181818')
        self.menuFrame = MenuFrame(self, bg='#181818')

        self.iconFrame.grid(row=0, column=0, sticky='nsew')
        self.titleFrame.grid(row=0, column=1, sticky='nsew')
        self.artistFrame.grid(row=0, column=2, sticky='nsew')
        self.albumFrame.grid(row=0, column=3, sticky='nsew')
        self.menuFrame.grid(row=0, column=4, sticky='nsew')

        self.play_button = PlayButton(self.iconFrame,
                                      title=self.title,
                                      url=self.url)
        self.like_button = LikeButton(self.iconFrame,
                                      title=self.title,
                                      album=self.album,
                                      artist=self.artist,
                                      url=self.url)

        self.play_button.grid(row=0, column=0, sticky='nsew')
        self.like_button.grid(row=0, column=1, sticky='nsew')

        self.iconFrame.grid_columnconfigure((0, 1), weight=1)
        self.iconFrame.grid_rowconfigure(0, weight=1)
        self.iconFrame.grid_propagate(False)

        self.titleLabel = ContentLabel(self.titleFrame, text=self.title)
        self.titleLabel.grid(row=0, column=0, sticky='nsew')
        self.titleFrame.grid_columnconfigure(0, weight=1)
        self.titleFrame.grid_rowconfigure(0, weight=1)

        self.artistLabel = ContentLabel(self.artistFrame, text=self.album)
        self.artistLabel.grid(row=0, column=0, sticky='nsew')
        self.artistFrame.grid_columnconfigure(0, weight=1)
        self.artistFrame.grid_rowconfigure(0, weight=1)

        self.albumLabel = ContentLabel(self.albumFrame, text=self.artist)
        self.albumLabel.grid(row=0, column=0, sticky='nsew')
        self.albumFrame.grid_columnconfigure(0, weight=1)
        self.albumFrame.grid_rowconfigure(0, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=10)
        self.grid_columnconfigure(2, weight=6)
        self.grid_columnconfigure(3, weight=6)
        self.grid_columnconfigure(4, weight=1)
        self.grid_propagate(False)

        self.iconFrame.bind('<Configure>', self.icon_size)
        self.titleFrame.bind('<Configure>', self.title_size)
        self.albumFrame.bind('<Configure>', self.album_size)
        self.artistFrame.bind('<Configure>', self.artist_size)
        self.menuFrame.bind('<Configure>', self.menu_size)

        self.bind('<Button-1>', self.click)
        self.bind('<Enter>', self.enter)
        self.bind('<Leave>', self.leave)

    @staticmethod
    def prepare_icon(filename, size):
        icon = Image.open('images/' + filename)
        icon = icon.resize((size, size), Image.ANTIALIAS)
        icon = ImageTk.PhotoImage(icon)
        return icon

    @staticmethod
    def bg_config(frame, bg):
        frame.iconFrame.config(bg=bg)
        frame.titleLabel.config(bg=bg)
        frame.albumLabel.config(bg=bg)
        frame.artistLabel.config(bg=bg)
        frame.menuFrame.config(bg=bg)
        frame.menuFrame.menuButton.config(bg=bg)
        frame.like_button.config(bg=bg)
        frame.play_button.config(bg=bg)

    @staticmethod
    def fg_config(frame, fg):
        frame.titleLabel.config(foreground=fg)
        frame.albumLabel.config(foreground=fg)
        frame.artistLabel.config(foreground=fg)

    def enter(self, event):
        from Base.listOfPage import current_playing
        if self.focus_get() != self:
            self.bg_config(self, '#222222')
            self.menuFrame.menuButton.grid(row=0, column=0, sticky='nsew')
        if self not in current_playing:
            self.play_button.config(image=self.pause_icon)
        return

    def leave(self, event):
        from Base.listOfPage import current_playing
        if self.focus_get() != self:
            self.bg_config(self, '#181818')
            self.menuFrame.menuButton.grid_forget()
        if self not in current_playing:
            self.play_button.config(image=self.music_icon)

        return

    def click(self, event):
        if str(self.focus_get()) != '.':
            self.bg_config(self.focus_get(), '#181818')
            self.focus_get().menuFrame.menuButton.grid_forget()
        self.focus_set()
        self.menuFrame.menuButton.grid(row=0, column=0, sticky='nsew')
        self.bg_config(self, '#333333')

    def double_click(self, event):
        from Base.listOfPage import current_playing
        if len(current_playing) != 0:
            frame = current_playing.pop()
            self.fg_config(frame, fg='#888888')
            frame.play_button.config(image=self.music_icon)
            frame.play_button.playing = False
            frame.master.master.master.master.master.head.text_frame.play_button.isPlaying = False
            frame.master.master.master.master.master.head.text_frame.play_button.ifPlaying()
            frame.play_music.Stop()

        if len(current_playing) == 0:
            current_playing.append(self)

        self.fg_config(self, fg='#1DB954')
        self.play_button.config(image=self.volume_icon)
        self.play_button.playing = True
        self.master.master.master.master.master.head.text_frame.play_button.isPlaying = True
        self.master.master.master.master.master.head.text_frame.play_button.ifPlaying()

        from Base.listOfPage import currentTrack
        if len(currentTrack) == 0:
            currentTrack.append({})
            currentTrack[0]['title'] = self.title
            currentTrack[0]['url'] = self.url
            self.play_music = Track(self, trackName=self.title,
                                    trackUrl=self.url,
                                    artist=self.artist,
                                    image=self.master.master.master.master.master.image)

            currentTrack[0]['instance'] = self.play_music
        else:
            # if currentTrack[0]['title'] == self.title:
            #     self.play_music = currentTrack[0]['instance']
            if currentTrack[0]['instance'] == self.play_music:
                self.play_music = currentTrack[0]['instance']
            else:
                from Base.listOfPage import bottomPage
                _ = bottomPage.pop()
                currentTrack[0]['title'] = self.title
                currentTrack[0]['url'] = self.url
                self.play_music = Track(self,
                                        trackName=self.title,
                                        trackUrl=self.url,
                                        artist=self.artist,
                                        image=self.master.master.master.master.master.image)
                currentTrack[0]['instance'] = self.play_music

        self.play_music.Play()

    def title_size(self, event):
        from ...TitleFrame import title_size
        self.titleFrame.config(width=title_size)
        self.titleFrame.grid_propagate(False)

    def icon_size(self, event):
        from ...TitleFrame import icon_size
        self.iconFrame.config(width=icon_size)
        self.iconFrame.grid_propagate(False)

    def album_size(self, event):
        from ...TitleFrame import album_size
        self.albumFrame.config(width=album_size)
        self.albumFrame.grid_propagate(False)

    def artist_size(self, event):
        from ...TitleFrame import artist_size
        self.artistFrame.config(width=artist_size)
        self.artistFrame.grid_propagate(False)

    def menu_size(self, event):
        from ...TitleFrame import menu_size
        self.menuFrame.config(width=menu_size)
        self.menuFrame.grid_propagate(False)
