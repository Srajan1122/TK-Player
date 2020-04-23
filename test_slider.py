from pygame import mixer
import tkinter as tk
import urllib.request
from io import BytesIO
import tkinter.messagebox as tkMessageBox
from firebase.firebase import FirebaseApplication
from mutagen.mp3 import MP3
from mutagen import MutagenError
from tkinter import ttk
from ttkthemes import ThemedTk
from ttkthemes import ThemedStyle


class Track(tk.Frame):
    def __init__(self, master, trackName, trackUrl, *args, **kwargs):
        super().__init__(master)

        self.trough = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x02\x00\x00\x00\x90\x08\x06\x00\x00\x00"\x18\xbal\x00\x00\x00\x04sBIT\x08\x08\x08\x08|\x08d\x88\x00\x00\x00\tpHYs\x00\x00\n\xfc\x00\x00\n\xfc\x01\x99\xdb\xbb\xef\x00\x00\x00\x19tEXtSoftware\x00www.inkscape.org\x9b\xee<\x1a\x00\x00\x00\x1fIDAT8\x8dc\\\xb5j\xd5\x7f\x06\x06\x06\x06&\x06(\x18e\x8c2F\x19\xa3\x8c\x91\xc9\x00\x00\xf7\xe7\x04\x1dd\xcc\xbe\x83\x00\x00\x00\x00IEND\xaeB`\x82'
        self.img_trough = tk.PhotoImage(master=self, data=self.trough)

        self.label = tk.Label(self, image=self.img_trough, bg='red')
        self.label.pack()

        style = ThemedStyle(self)
        style.set_theme("breeze")

        style.element_create('custom.Horizontal.Scale.trough', 'from', 'default')
        style.element_create('custom.Horizontal.Scale.slider', 'from', 'default')

        style.layout('Horizontal.TScale',
                     [('custom.Horizontal.Scale.trough', {'sticky': 'ew'}),
                      ('Horizontal.Scale.slider',
                       {'side': 'left', 'sticky': '',
                        'children': [('Horizontal.Scale.label', {'sticky': ''})]
                        })])

        print(style.element_names())
        print(style.element_options('custom.Scale.trough'))
        print(style.element_options('custom.Scale.slider'))

        print(style.theme_use())
        # style.configure("custom.Horizontal.TScale", style.configure("Horizontal.TScale"))
        # style.configure('custom.Horizontal.TScale')

        self.pack()
        self['background'] = '#000000'
        self['padx'] = 25

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

        self.byteAudio = self.get_audio_from_url(trackUrl)
        self.byteAudio2 = self.get_audio_from_url(trackUrl)
        self.track = self.byteAudio
        # self.get_duration(self.byteAudio2)
        self.load_music()
        self.make_ui()

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
        return duration

    def load_music(self):
        player = mixer
        player.init()
        # song = player.Sound(self.track)
        # duration = song.get_length()
        # print(duration)
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
        self.currentTime = tk.Label(self, text="--/--", foreground='white', background='black')
        self.currentTime.pack(side='left')

        # end time label
        self.endTime = tk.Label(self, text="--/--", foreground='white', background='black')
        self.endTime.pack(side='right')

        # slider
        self.sliderValue = tk.DoubleVar()
        self.songDuration = self.get_duration(self.byteAudio2)
        self.slider = ttk.Scale(self, to=self.songDuration, orient=tk.HORIZONTAL, length=700,
                                variable=self.sliderValue,
                                command=self.UpdateSlider,
                                style='Horizontal.TScale'
                                )
        self.slider.pack()

        # volume slider
        self.volume = tk.DoubleVar()
        self.volume.set(70)
        self.volumeSlider = tk.Scale(self, to=100, orient=tk.VERTICAL, length=350,
                                     resolution=0.5, showvalue=False, variable=self.volume,
                                     command=self.UpdateVolume)
        self.volumeSlider.pack()

    def Play(self):
        currentTime = self.sliderValue.get()
        self.player.music.play(start=currentTime)
        self.TrackPlay(currentTime)

    def TrackPlay(self, currentTime):
        if self.player.music.get_busy():
            self.sliderValue.set(currentTime)
            currentTime += 1
            self.loopID = self.after(1000, lambda: self.TrackPlay(currentTime))
        else:
            print('Track has ended')

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


def ask_quit():
    '''Confirmation to quit application.'''
    if tkMessageBox.askokcancel("Quit", "Exit MusicPlayer"):
        app.Stop()
        app.player.quit()
        root.destroy()


if __name__ == "__main__":
    # root = ThemedTk(theme="breeze")
    root = tk.Tk()
    firebase = FirebaseApplication('https://tkintertest.firebaseio.com/', None)
    result = firebase.get('/music/1', '')
    trackName = result['filename']
    trackUrl = result['url']
    app = Track(root, trackName=trackName, trackUrl=trackUrl)
    root.protocol("WM_DELETE_WINDOW", ask_quit)
    root.mainloop()
