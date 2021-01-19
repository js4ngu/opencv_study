import cv2

img = cv2.imread('D:/FIles/study/open-cv/study/opencv_study/ch02/cat.bmp',cv2.IMREAD_GRAYSCALE)
cv2.imshow('img',img)

while True:
    keycode = cv2.waitKey()
    if keycode == ord('i') or keycode == ord('I'):
        img = ~img
        cv2.imshow('img', img)
    
    elif keycode == 27:
        break

cv2.destroyAllWindows()