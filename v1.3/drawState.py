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
