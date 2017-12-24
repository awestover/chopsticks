# from subprocess import Popen,PIPE,STDOUT,call
# import time
# import os
#
# def drawState(first=False):
#     try:
#         if not first:
#             # super useful for SILENTLY doing this task
#             proc = Popen('TASKKILL /f /im Microsoft.Photos.exe',
#                 shell=True, stdout=PIPE, )
#             output=proc.communicate()[0]
#
#             proc.wait()
#
#             time.sleep(0.3)
#
#         os.startfile("arenaCurrent.png")
#     except:
#         print("Your computer does not support opening and closing image files")
#         print("Open arenaCurrent.png to see the state or just remember the state")
#         print("Only windows gets nice graphics :(")
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def drawState(first=False):
    try:
        if not first:
            # hide image
            for proc in psutil.process_iter():
                print(proc.name())
                if proc.name() == "display" or "microsoft.photo" in proc.name().lower():
                    proc.kill()
    except:
        pass
        # print("image closing error")

    a = Image.open("arenaCurrent.png")
    a.show()
