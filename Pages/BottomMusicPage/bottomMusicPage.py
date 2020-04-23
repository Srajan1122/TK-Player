import tkinter as tk
from PIL import ImageTk, Image


class BottomMusicPage(tk.Frame):
    def __init__(self, master, controller, title, artist, image, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self['background'] = 'red'
        self.controller = controller
        self.playing = True
        print(image)

        self.label = tk.Label(self, text=title)
        self.label.grid(row=0, column=0, sticky='nsew')

        self.artistLabel = tk.Label(self, text=artist)
        self.artistLabel.grid(row=2, column=0, sticky='nsew')

        self.image = ImageTk.PhotoImage(image)
        self.imageLabel = tk.Label(self, image=self.image)
        self.imageLabel.grid(row=2, column=1, sticky='nsew')

        from Base.listOfPage import currentTrack
        self.sliderValue = tk.DoubleVar()
        self.slider = tk.Scale(self,
                               to=currentTrack[0]['instance'].songDuration,
                               orient=tk.HORIZONTAL,
                               length=700,
                               resolution=0.5,
                               showvalue=False,
                               digit=4,
                               variable=self.sliderValue,
                               command=self.UpdateSlider)

        self.volume = tk.DoubleVar()
        self.volume.set(70)
        self.volumeSlider = tk.Scale(self, to=100, orient=tk.HORIZONTAL, length=350,
                                     resolution=0.5, showvalue=False, variable=self.volume,
                                     command=self.UpdateVolume, troughcolor='green')

        self.button = tk.Button(self, text='play', bg='green', command=self.click)

        self.currentTime = tk.Label(self, text="--/--", foreground='white', background='#000000')

        endTime = self.convertTime(currentTrack[0]['instance'].songDuration)
        self.endTime = tk.Label(self, text=endTime, foreground='white', background='#000000')

        self.slider.grid(row=0, column=1, sticky='nsew')
        self.volumeSlider.grid(row=0, column=2, sticky='nsew')
        self.button.grid(row=1, column=0, sticky='nsew')
        self.endTime.grid(row=1, column=2, sticky='nsew')
        self.currentTime.grid(row=1, column=1, sticky='nsew')

    def TrackPlay(self, currentTime):
        from Base.listOfPage import currentTrack
        if currentTrack[0]['instance'].player.music.get_busy():
            self.sliderValue.set(currentTime)
            time = self.convertTime(currentTime)
            self.currentTime.config(text=time)
            currentTime += 1
            self.loopID = self.after(1000, lambda: self.TrackPlay(currentTime))
        else:
            pass
            # print('Track has ended')

    def UpdateSlider(self, value):
        from Base.listOfPage import currentTrack
        if currentTrack[0]['instance'].player.music.get_busy():
            self.after_cancel(self.loopID)
            self.sliderValue.set(value)
            currentTrack[0]['instance'].Play()
        else:
            # print("Track Not Playing")
            self.sliderValue.set(value)

    def UpdateVolume(self, value):
        from Base.listOfPage import currentTrack
        percentValue = float(value) / 100
        currentTrack[0]['instance'].player.music.set_volume(percentValue)

    def convertTime(self, currentTime):
        mins, sec = divmod(currentTime, 60)
        time = str(int(mins)).zfill(2) + ":" + str(int(sec)).zfill(2)
        return time

    def click(self):
        self.controller.play_button.click()

    def changeButton(self):
        if self.playing:
            self.button.config(bg='yellow')
            self.playing = False
        else:
            self.button.config(bg='green')
            self.playing = True
