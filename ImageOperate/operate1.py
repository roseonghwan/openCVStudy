import cv2
import numpy as np

img1 = cv2.imread('../images/flower1.jpg')
img2 = cv2.imread('../images/flower2.jpg')

def nothing(x):
    pass

cv2.namedWindow('image')
# 트랙바를 지정된 윈도우에 생성하는 함수
cv2.createTrackbar('W', 'image', 0, 100, nothing)

while True:
    # 트랙바의 현재 위치를 리턴하는 함수
    w = cv2.getTrackbarPos('W', 'image')
    # (이미지1, 이미지1 가중치, 이미지2, 이미지2 가중치, 각 뎃셈에 추가하는 값)
    dst = cv2.addWeighted(img1, float(100 - w) * 0.01, img2, float(w) * 0.01, 0)
    cv2.imshow('dst', dst)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()