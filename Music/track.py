from pygame import mixer
import tkinter as tk
import urllib.request
from io import BytesIO
from mutagen.mp3 import MP3


class Track:
    def __init__(self, master, trackName, trackUrl, artist, image):

        self.title = trackName
        self.master = master
        self.artist = artist
        self.image = image

        self.track = None
        self.byteAudio = None
        # self.trackUrl = trackUrl
        self.TrackName = trackName
        self.songDuration = None
        self.player = None
        self.playButton = None
        self.stopButton = None
        self.slider = None
        self.sliderValue = tk.DoubleVar()
        self.volumeSlider = None
        self.volume = None
        self.currentTime = None
        self.endTime = None
        self.repeatButton = None

        self.byteAudio = self.get_audio_from_url(trackUrl)
        self.byteAudio2 = self.get_audio_from_url(trackUrl)
        self.track = self.byteAudio
        self.load_music()
        self.get_duration(self.byteAudio2)

    def get_audio_from_url(self, trackUrl):
        req = urllib.request.Request(trackUrl)
        resp = urllib.request.urlopen(req)
        byteAudio = BytesIO(resp.read())
        return byteAudio

    def get_duration(self, byteAudio):
        song = MP3(byteAudio)
        duration = song.info.length
        self.songDuration = duration

    def load_music(self):
        player = mixer
        player.init()
        player.music.load(self.track)
        player.music.set_volume(.70)

        self.player = player

    def Play(self):
        from Pages.BottomMusicPage.bottomMusicPage import BottomMusicPage
        from Base.listOfPage import bottomPage
        from Base.listOfPage import bottomInstance

        if len(bottomPage) == 0:
            bottom = BottomMusicPage(bottomInstance[0],
                                     self.master,
                                     title=self.title,
                                     artist=self.artist,
                                     image=self.image)
            bottomPage.append(bottom)
            bottomInstance[0].show_frame(self.title)
            currentTime = 0
        else:
            currentTime = bottomPage[0].middle.sliderValue.get()
            bottom = bottomPage[0]

        self.player.music.play(start=currentTime)
        bottom.middle.TrackPlay(currentTime)

    def Stop(self):
        if self.player.music.get_busy():
            self.player.music.stop()
