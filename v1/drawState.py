import psutil
import sys
import os
if len(sys.argv) == 1:
    os.system("taskkill /f /im Microsoft.Photos.exe")
os.startfile("arenaCurrent.png")
