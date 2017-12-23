# from gtts import gTTS
# import os
# tts = gTTS(text='Good morning', lang='en')
# tts.save("good.wav")
# # os.system("mpg321 good.wav")
# os.system("(New-Object Media.SoundPlayer 'good.wav').Play();")
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
speak.Speak("Hello World")

def sayState(state):
    s = [str(si) for si in state]
    s = " ".join(s)
    speak.Speak("The state is currently " + s)
sayState([1,1,1,1])
def promptMove():
    speak.Speak("Please take a move esteemed user")
promptMove()
