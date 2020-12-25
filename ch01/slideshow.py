import sys
import glob
import cv2

img_files = glob.glob('D:\\FIles\\study\\open-cv\\study\\opencv_study\\ch01\\images\*.jpg') #해당 디렉터리에 해당 확장자를 변수(배열)에 넣어줌

for f in img_files: ## img_files라는 배열의 각각의 항목 f에 대하
    print(f)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)

cnt = len(img_files) #len함수로 배열의 크기를 알아냄
idx = 0 #배열 인덱스 

while True: #무한반복
    img = cv2.imread(img_files[idx]) # img변수에 img_files[idx]를 넣어줌
    cv2.imshow('image', img) #이미지 출력, 참고로 waitKey해야지만, 이미지 나오더라

    if cv2.waitKey(1000) == 27: #ESC 압력시 while문 탈출, 아니면 1sec 딜레이 후 if문 탈출
        break
    idx += 1 #index 늘려줌

    if idx >= cnt: #idx가 cnt(이미지갯수) 보다 커지면 초기화
        idx = 0

cv2.destroyAllWindows() #창 전부다 꺼져버리는거임ㅋㅋ