from subprocess import Popen,PIPE,STDOUT,call
import time
import os

def drawState(first=False):
    try:
        if not first:
            # os.system("Stop-Process -processname Microsoft.Photos")
            # os.system("TASKKILL /f /im Microsoft.Photos.exe")

            # super useful for SILENTLY doing this task
            proc = Popen('TASKKILL /f /im Microsoft.Photos.exe',
                shell=True, stdout=PIPE, )
            output=proc.communicate()[0]

            proc.wait()

            time.sleep(0.3)

        os.startfile("arenaCurrent.png")

    except:
        print("Your computer does not support opening and closing image files")
        print("Open arenaCurrent.png to see the state or just remember the state")
        print("Only windows gets nice graphics :(")
