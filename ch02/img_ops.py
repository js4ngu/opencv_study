import sys
import cv2


# 마스크 영상을 이용한 영상 합성
src = cv2.imread('D:/FIles/study/open-cv/study/opencv_study/ch02/opencv-logo-white.png', cv2.IMREAD_UNCHANGED)
mask = src[:,:,-1]
src = src[:,:,0:3]
#mask = cv2.imread('D:/FIles/study/open-cv/study/opencv_study/ch02/mask_plane.bmp', cv2.IMREAD_GRAYSCALE)
dst = cv2.imread('D:/FIles/study/open-cv/study/opencv_study/ch02/field.bmp', cv2.IMREAD_COLOR)

h, w = src.shape[:2]

crop = dst[0:h, 0:w]

cv2.copyTo(src,mask,crop)

#dst[mask > 0] = src[mask > 0]

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('mask', mask)
cv2.waitKey()

cv2.destroyAllWindows()
