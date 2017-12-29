#!/usr/bin/env python3

import speech_recognition as sr
import webbrowser
import sys
import os


# get audio from the microphone
r = sr.Recognizer()
res = []
with sr.Microphone() as source:
    while len(res) != 2:
        print("Speak:")
        try:
            audio = r.listen(source, timeout = 1)
            try:
                out = r.recognize_google(audio)
                print("You said " + out)
                if out == "quit":
                    playing = False
                elif out.lower() == "google":
                    os.system("start chrome.exe")
                elif " " in out:
                    outs = out.split(" ")
                    if outs[0].lower() == "google":
                        webbrowser.open(" ".join(outs[1:len(outs)]))

                for string in out.split(" "):
                    try:
                        res.append(int(string))
                    except:
                        pass

            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))


        except sr.WaitTimeoutError:
            print("hurry up man")



print(res)
