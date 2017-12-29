import matplotlib.pyplot as plt
import numpy as np
import time
from matplotlib import animation

data = np.random.rand(128, 128)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

im = ax.imshow(data, animated=True)

def update_image(i):
    data = np.random.rand(128, 128)
    im.set_array(data)
    time.sleep(0.5)
    plt.pause(0.5)
ani = animation.FuncAnimation(fig, update_image, interval=0)

plt.show()
