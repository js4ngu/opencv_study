import numpy as np
import sys
from matplotlib import pyplot as plt
import cv2
src = cv2.imread('/Users/yoojongsang/Documents/GitHub/opencv_study/ch03/lenna.bmp', cv2.IMREAD_GRAYSCALE)
hist = cv2.calcHist([src], [0], None, [256], [0,256])
cv2.imshow('src', src)

plt.plot(hist)
plt.show()

src = cv2.imread('/Users/yoojongsang/Documents/GitHub/opencv_study/ch03/lenna.bmp', cv2.IMREAD_COLOR)
cv2.imshow('src', src)
colors = ['b', 'g', 'r']
bgr_planes = cv2.split(src)

for (p, c) in zip(bgr_planes, colors):
    hist = cv2.calcHist([p], [0], None, [256], [0,256])
    plt.plot(hist, color=c)

plt.show()