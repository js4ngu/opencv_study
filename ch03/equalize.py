import numpy as np
import sys
from matplotlib import pyplot as plt
import cv2

src = cv2.imread('/Users/yoojongsang/Documents/GitHub/opencv_study/ch03/lenna.bmp', cv2.IMREAD_COLOR)

if src is None:
    print('Image Load is failed')
    sys.exit()

scr_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
planes = cv2.split(scr_ycrcb)

planes[0] = cv2.equalizeHist(planes[0])
dst = cv2.merge(planes)

hist1 = cv2.calcHist([src], [0], None, [256], [0,255])
hist2 = cv2.calcHist([dst], [0], None, [256], [0,255])

dst = cv2.cvtColor(dst, cv2.COLOR_YCrCb2BGR)

cv2.imshow('src',src)
cv2.imshow('eq', dst)

plt.subplot(121), plt.axis('on'), plt.plot(hist1), plt.title('src')
plt.subplot(122), plt.axis('on'), plt.plot(hist2), plt.title('dst')

plt.show()
cv2.waitKey()

cv2.destroyAllWindows()