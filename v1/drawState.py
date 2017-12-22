from subprocess import Popen,PIPE,STDOUT,call
import os

def drawState(first=False):
    if not first:
        # os.system("Stop-Process -processname Microsoft.Photos")
        # os.system("TASKKILL /f /im Microsoft.Photos.exe")

        # super useful for SILENTLY doing this task
        proc=Popen('TASKKILL /f /im Microsoft.Photos.exe',
            shell=True, stdout=PIPE, )
        #output=proc.communicate()[0]
    os.startfile("arenaCurrent.png")
