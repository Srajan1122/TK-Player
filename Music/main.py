from pygame import mixer
import tkinter as tk
from firebase.firebase import FirebaseApplication
import urllib.request
from io import BytesIO

def requestSong(id):
    firebase = FirebaseApplication('https://tkintertest.firebaseio.com/', None)
    result = firebase.get('/music/{id}', '')
    req = urllib.request.Request(result['url'])
    resp = urllib.request.urlopen(req)
    song = BytesIO(resp.read())
    return song

def load(self, song):
    mixer.init()
    mixer.music.load(song)

def play():
    if(mixer.music.get_busy()):
        mixer.music.unpause()
    else:
        mixer.music.play()

def stop(currentSong):
    if mixer.music.get_busy():
        mixer.music.stop()

def playNext(listOfSongs,currentSong):
    pass

def pause():
    if mixer.music.get_busy():
        mixer.music.stop()