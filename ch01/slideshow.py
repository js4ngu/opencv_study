import sys
import glob
import cv2

img_files = glob.glob('D:\\FIles\\study\\open-cv\\study\\opencv_study\\ch01\\images\*.jpg') #해당 디렉터리에 해당 확장자를 변수(배열)에 넣어줌

for f in img_files: ## img_files라는 배열의 각각의 항목 f에 대하
    print(f)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)

cnt = len(img_files) #len함수로 배열의 크기를 알아냄
idx = 0

while True:
    img = cv2.imread(img_files[idx])
    cv2.imshow('image', img)

    if cv2.waitKey(1000) == 27: #ESC
        break
    idx += 1

    if idx >= cnt:
        idx = 0

cv2.destroyAllWindows()