pages = []
rightPage = []
current_playing = []
musicPages = []
focusCard = []
musicList = []
currentTrack = []
bottomInstance = []
bottomPage = []


c = 1
f = 0


def flag():
    global f
    return f


def setFlagValue():
    global f
    f = 1
    return f


def getCount():
    global c
    return c


def incrementCount():
    global c
    c += 1
    return


def resetCount():
    global c
    c = 1
    return
