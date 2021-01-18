import sys
import cv2

#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('D:/FIles/study/open-cv/study/opencv_study/ch02/video1.mp4')

if not cap.isOpened():
    print('camera open fail')
    sys.exit

w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(w, h)

while True:
    ret, frame = cap.read()#한프레임씩 받아온다

    if not ret:#정상적으로 받아왔는지 확인
        break
    
    #여기선 영상처리 코드 입력
    edge = cv2.Canny(frame, 50, 150)
    orign_msec = int(cap.get(cv2.CAP_PROP_POS_MSEC))
    edge_msec = int(cap.get(cv2.CAP_PROP_POS_MSEC))

    cv2.putText(frame, 'Orignal', (20,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,255,255),1,cv2.LINE_AA)
    cv2.putText(edge, 'Edge', (20,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 255,1,cv2.LINE_AA)
    
    cv2.imshow('frame',frame)
    cv2.imshow('edge',edge)
    if cv2.waitKey(20) == 27:
        break

cap.release()
cv2.destroyAllWindows()