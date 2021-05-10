import numpy as np
import sys
from matplotlib import pyplot as plt
import cv2

src = cv2.imread('/Users/yoojongsang/Documents/GitHub/opencv_study/ch03/lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image Load is failed')
    sys.exit()

alpha = 3.0
#dst = np.clip((1 + alpha) * src -128 * alpha, 0, 255).astype(np.uint8)
dst = cv2.normalize(src, None, 0, 255, cv2.NORM_MINMAX)

hist = cv2.calcHist([src], [0], None, [256], [0,255])
hist2 = cv2.calcHist([dst], [0], None, [256], [0,255])


cv2.imshow('src',src)
cv2.imshow('dst', dst)
plt.plot(hist)
plt.plot(hist2)
plt.show()
cv2.waitKey()

cv2.destroyAllWindows()