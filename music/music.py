
from pygame import mixer

def clickSon():
    mixer.music.load("asset/sound/click.ogg")
    mixer.music.play()

def errorSon():
    mixer.music.load("asset/sound/over.ogg")
    mixer.music.play()

def sucSon():
    mixer.music.load("asset/sound/tir.ogg")
    mixer.music.play()
