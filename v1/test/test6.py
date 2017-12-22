from PIL import Image, ImageDraw
from pywinauto.findwindows    import find_window
from pywinauto.win32functions import SetForegroundWindow
import matplotlib.pyplot as plt
import numpy as np


ImageAddress = 'arenaCurrent.png'
ImageItself = Image.open(ImageAddress)
ImageNumpyFormat = np.asarray(ImageItself)
plt.imshow(ImageNumpyFormat)
plt.draw()
plt.pause(0.1) # pause how many seconds
plt.close()
