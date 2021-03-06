import cv2
import sys

print('Hello openCV', cv2.__version__)

img = cv2.imread('/Users/yoojongsang/Documents/GitHub/opencv_study/ch01/cat_gray.png', cv2.IMREAD_GRAYSCALE)

if img is None:
    print('Image load failed')
    sys.exit()

cv2.imwrite('D:\FIles\study\open-cv\study\opencv_study\ch01\cat_gray2.png', img)
cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
cv2.imshow('image', img)

while True:
    if cv2.waitKey() == ord('q'):
        break

cv2.destroyAllWindows()