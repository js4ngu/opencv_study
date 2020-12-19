import cv2
import sys

print('Hello openCV', cv2.__version__)

img = cv2.imread('D:\FIles\study\open-cv\study\opencv_study\ch01\img.bmp')

if img is None:
    print('Image load failed')
    sys.exit()

cv2.namedWindow('image')
cv2.imshow('image', img)
cv2.waitKey(0)

cv2.destroyAllWindows()
