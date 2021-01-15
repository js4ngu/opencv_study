import cv2

img1 = cv2.imread('D:\FIles\study\open-cv\study\opencv_study\ch02\cat.bmp', cv2.IMREAD_GRAYSCALE) #openCV는 영상 데이터를 numpy.ndarray로 표현
img2 = cv2.imread('D:\FIles\study\open-cv\study\opencv_study\ch02\cat.bmp',cv2.IMREAD_ANYCOLOR)

if img1 is None or img2 is None:
    print('image load failed')
    sys.exit()

print('type(img1) :', type(img1))
print('img1.shape :', img1.shape) #garay scale 영상은 높이와 폭만
print('img2.shape :', img2.shape) #color영상은 채널 수 까지 표현하는듯
print('img2.dtype :', img2.dtype) #img2 numpy.ndarray의 데이터 타입 

h, w = img1.shape #얘네는 데이터가 2개만 가지고 있어서 2개 만 적어도 됨 ㅇㅇ
print('img1 size : {} x {}'. format(w,h)) #format이 어찌 보면 C에서의 %d와 &arr[]의 역활이 통합된거임.ㅇㅇ

h, w = img2.shape[:2]
print('img2 size : {} x {}'. format(w,h)) #format이 어찌 보면 C에서의 %d와 &arr[]의 역활이 통합된거임.ㅇㅇ

if img1.ndim == 2:      #img1 의 차원의 수가 2개라서 그레이스케일임
    print('img1 is Grayscale')
if len(img2.shape) == 3: #returned numer of item(img2.shape) in a container
    print('img2 is TrueColor image')

#픽셀값을 보기위해선 
x = 20
y = 10
p1 = img1[y,x]
p2 = img2[y,x]
print('img1 {} x {} pixel value : {} ' .format(x,y,p1))
print('img2 {} x {} pixel value : {} ' .format(x,y,p2))

#픽셀값 수정
for y in range(240):
    for x in range(320):
        img1[y,x] = 0
        img2[y,x] = (0,255, 255)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.waitKey()

cv2.destroyAllWindows()

#전체 영역을 한번에 지정
img1[:, :] = 0
img2[:, :] = (0,255,255)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.waitKey()

cv2.destroyAllWindows()

