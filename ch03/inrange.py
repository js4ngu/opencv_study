import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt

src = cv2.imread('/Users/yoojongsang/Documents/GitHub/opencv_study/ch03/dog.bmp', cv2.IMREAD_COLOR)
src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

def on_trackbar(pos):
    hmin = cv2.getTrackbarPos('h_min', 'dst')
    hmax = cv2.getTrackbarPos('h_max', 'dst')

    dst = cv2.inRange(src_hsv, (hmin,150,0), (hmax, 255, 255))
    cv2.imshow('dst', dst)

cv2.imshow('src', src)
cv2.namedWindow('dst')

cv2.createTrackbar('h_min', 'dst', 50, 179, on_trackbar)
cv2.createTrackbar('h_max', 'dst', 80, 179, on_trackbar)
on_trackbar(0)

cv2.waitKey()