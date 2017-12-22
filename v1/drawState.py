import os

def drawState(first=False):
    if not first:
        os.system("taskkill /f /im Microsoft.Photos.exe")
    os.startfile("arenaCurrent.png")
