from gtts import gTTS
from pygame import mixer
from os import remove
from time import sleep
#from os import 
def funcaoTocarAudio(mensagem):
    tts = gTTS(text=mensagem, lang="pt-BR", slow=False)
    tts.save("output.mp3")
    mixer.init()
    mixer.music.load("output.mp3")
    mixer.music.play()
    while mixer.music.get_busy():
        mixer.music.get_busy() 
    mixer.music.unload()
    remove("output.mp3")
    sleep(1)
