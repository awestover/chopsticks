import cv2
import time

image = cv2.imread('arenaCurrent.png')

cv2.imshow('Test image', image)
cv2.waitKey(1000)
cv2.destroyAllWindows()
