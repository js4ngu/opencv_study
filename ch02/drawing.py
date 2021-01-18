import numpy as np
import cv2

img = np.full((400,400,3),255,np.uint8)

cv2.line(img,(50,50),(200,50),(0,0,255),5,cv2.LINE_AA) #직선 그리기
cv2.line(img,(50,60),(150,160),(0,0,255)) #직선 그리기

cv2.rectangle(img, (50,200,150,100), (0,255,0),2)
cv2.rectangle(img, (700,200), (180,280), (0,128,0), -1) #color에 -1이면 Fill해줌

cv2.circle(img, (90,90), 30, (128,39,155), -1, cv2.LINE_AA)
cv2.circle(img, (90,90), 70, (128,39,155), 1, cv2.LINE_8)

pol_point = np.array([[250,50],[300,200],[350,250],[170,200]])
cv2.polylines(img, [pol_point], True, (127,46,79),3, cv2.LINE_AA)

cv2.putText(img, 'Hello CV', (100,200), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),1,cv2.LINE_AA)

cv2.imshow('img', img)
cv2. waitKey()
cv2.destroyAllWindows()