import sys
import cv2

cap = cv2.VideoCapture(0) #camera 불러오가

if not cap.isOpened():
    print('camera opened failed!')
    sys.exit()

w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #round()는 반올림 함수
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) #round()는 반올림 함수
fps = cap.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*'DIVX') # *'DIVX' = 'D','I','V','X'
delay = round(1000/fps)

out = cv2.VideoWriter('Ouput.avi', fourcc, fps, (w,h))

if not out.isOpened():
    print('File open failed')
    cap.release()
    sys.exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    #inversed = ~frame
    edge = cv2.Canny(frame, 50 ,150)
    edge_color = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)
    out.write(edge_color)

    cv2.imshow('frame', frame)
    #cv2.imshow('inversed', inversed)
    cv2.imshow('edge', edge)
    if cv2.waitKey(delay) == 27:
        break

cap.release() #open된 video 나 영상장치를 닫습니다/
out.release()
cv2.destroyAllWindows()