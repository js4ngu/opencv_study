import cv2
import numpy as np
import sys

img = cv2.imread('/Users/yoojongsang/Documents/GitHub/opencv_study/ch03/lenna.bmp', cv2.IMREAD_GRAYSCALE)
src = cv2.imread('/Users/yoojongsang/Documents/GitHub/opencv_study/ch03/lenna.bmp', cv2.IMREAD_COLOR)
dst = cv2.add(img, 100)
dst2 = cv2.add(src, (100,100,100,0))
cv2.imshow('image', img)
cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)
cv2.waitKey()

cv2.destroyAllWindows()