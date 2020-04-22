from pygame import mixer
import tkinter as tk
import urllib.request
from io import BytesIO
import tkinter.messagebox as tkMessageBox
# from firebase.firebase import FirebaseApplication
from mutagen.mp3 import MP3
from mutagen import MutagenError


class Track:
    def __init__(self, master, trackName, trackUrl, *args, **kwargs):

        self.master = master
        self.track = None
        self.byteAudio = None
        # self.trackUrl = trackUrl
        self.TrackName = trackName
        self.songDuration = None
        self.player = None
        self.playButton = None
        self.stopButton = None
        self.slider = None
        self.sliderValue = None
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
        # self.byteAudio = byteAudio
        # song = MP3(byteAudio)
        # self.songDuration = song.info.length
        # # print(self.songDuration)
        # self.track = byteAudio
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

    def make_ui(self):

        # Title
        self.title = tk.Label(self, text=self.TrackName, background='#000000', foreground='white')
        self.title.pack()

        # play Button
        self.playButton = tk.Button(self, text='Play', command=self.Play)
        self.playButton.pack()

        # stop Button
        self.stopButton = tk.Button(self, text='Stop', command=self.Stop)
        self.stopButton.pack()

        # currentTime Label
        self.currentTime = tk.Label(self, text="--/--", foreground='white', background='#000000')
        self.currentTime.pack()
        # end time label
        endTime = self.convertTime(self.songDuration)
        self.endTime = tk.Label(self, text=endTime, foreground='white', background='#000000')
        self.endTime.pack()

        # slider
        self.sliderValue = tk.DoubleVar()
        self.slider = tk.Scale(self, to=self.songDuration, orient=tk.HORIZONTAL, length=700,
                               resolution=0.5, showvalue=False, digit=4,
                               variable=self.sliderValue, command=self.UpdateSlider)
        self.slider.pack()

        # volume slider
        self.volume = tk.DoubleVar()
        self.volume.set(70)
        self.volumeSlider = tk.Scale(self, to=100, orient=tk.VERTICAL, length=350,
                                     resolution=0.5, showvalue=False, variable=self.volume,
                                     command=self.UpdateVolume, troughcolor='green')
        self.volumeSlider.pack()

    def Play(self):
        # currentTime = self.sliderValue.get()
        currentTime = 0
        self.player.music.play(start=currentTime)
        # self.TrackPlay(currentTime)

    def TrackPlay(self, currentTime):
        if self.player.music.get_busy():
            self.sliderValue.set(currentTime)
            time = self.convertTime(currentTime)
            self.currentTime.config(text=time)
            currentTime += 1
            self.loopID = self.after(1000, lambda: self.TrackPlay(currentTime))
        else:
            print('Track has ended')
            if(self.repeatButton.config('text')[-1] == "Repeat"):
                self.sliderValue.set(0)
                self.Play()
            else:
                print("Track Not Playing (TrackPlay)")

    def UpdateSlider(self, value):
        if self.player.music.get_busy():
            self.after_cancel(self.loopID)
            self.sliderValue.set(value)
            self.Play()
        else:
            print("Track Not Playing")
            self.sliderValue.set(value)

    def Stop(self):
        if self.player.music.get_busy():
            self.player.music.stop()

    def UpdateVolume(self, value):
        percentValue = float(value) / 100
        self.player.music.set_volume(percentValue)

    def convertTime(self, currentTime):
        mins, sec = divmod(currentTime, 60)
        time = str(int(mins)).zfill(2) + ":" + str(int(sec)).zfill(2)
        return time


# def ask_quit():
#     '''Confirmation to quit application.'''
#     if tkMessageBox.askokcancel("Quit", "Exit MusicPlayer"):
#         app.Stop()
#         app.player.quit()
#         root.destroy()


# if __name__ == "__main__":
#     root = tk.Tk()
#     firebase = FirebaseApplication('https://tkintertest.firebaseio.com/', None)
#     result = firebase.get('/music/1', '')
#     trackName = result['filename']
#     trackUrl = result['url']
#     app = Track(root, trackName=trackName, trackUrl=trackUrl)
#     root.protocol("WM_DELETE_WINDOW", ask_quit)
#     root.mainloop()
