import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt

src = cv2.imread('/Users/yoojongsang/Documents/GitHub/opencv_study/ch03/lenna.bmp', cv2.IMREAD_COLOR)

if src is None:
    print("Img load failed!")
    sys.exit()

print('src.shape : ', src.shape)
print('src.dtype : ', src.dtype)

src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
planes = cv2.split(src_hsv)

cv2.imshow('src', src)
cv2.imshow('planes[0]', planes[0])
cv2.imshow('planes[1]', planes[1])
cv2.imshow('planes[2]', planes[2])
cv2.waitKey()

cv2.destroyAllWindows()