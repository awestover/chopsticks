from PIL import Image, ImageDraw
from pywinauto.findwindows    import find_window
from pywinauto.win32functions import SetForegroundWindow
import matplotlib.pyplot as plt
import numpy as np


im = Image.open("arena.png")

x, y =  im.size
eX, eY = 30, 60 #Size of Bounding Box for ellipse

bbox =  (x/2 - eX/2, y/2 - eY/2, x/2 + eX/2, y/2 + eY/2)
draw = ImageDraw.Draw(im)
draw.ellipse(bbox, fill=128)
del draw

im.save("arenaCurrent.png")

ImageAddress = 'arenaCurrent.png'
ImageItself = Image.open(ImageAddress)
ImageNumpyFormat = np.asarray(ImageItself)
plt.axis('off')
plt.imshow(ImageNumpyFormat)
plt.draw()
plt.pause(5) # pause how many seconds
plt.close()
