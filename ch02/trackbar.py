import numpy as np
import cv2

def garyscale_level(pos):
    global img
    print(pos)
    level = pos *16
    level = np.clip(level, 0, 255)
    #if level >= 255:
    #    level = 255

    img[:, :] = level
    cv2.imshow('image', img)

img = np.zeros((480,640), np.uint8)
cv2.imshow('image', img)

cv2.createTrackbar('level', 'image', 0, 16, garyscale_level)
cv2.waitKey()

cv2.destroyAllWindows()