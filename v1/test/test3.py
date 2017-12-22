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

bbox =  (x/2-100, y/2 - eY/2, x/2 + eX/2, y/2 + eY/2)
draw = ImageDraw.Draw(im)
draw.ellipse(bbox, fill=128)
del draw

im.save("arenaCurrent.png")
im.show()
