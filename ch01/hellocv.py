import cv2
import sys

print('Hello openCV', cv2.__version__)

img = cv2.imread('opencv-study\ch01\cat.bmp')

if img is None:
    print('Image load failed')
    sys.exit()

cv2.namedWindow('image')
cv2.imshow('image', img)
cv2.waitKey(0)

cv2.destroyAllWindows()
