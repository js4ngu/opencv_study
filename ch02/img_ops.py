import cv2
import numpy as np

img1 = cv2.imread('D:\FIles\study\open-cv\study\opencv_study\ch02\HappyFish.jpg')
img2 = img1[40:120, 30:150] #참조
img3 = img1[40:120, 30:150].copy() #ndarray 지원 함수, 데이터만 복사

#img2.fill(0)
cv2.circle(img2, (50,50), 20, (0,0,255),2)

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('img3',img3)
cv2.waitKey()
cv2.destroyAllWindows()