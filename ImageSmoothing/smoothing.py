# cv2.filter2D()로 이미지에 kernal(filter)을 적용해 이미지를 필터링
# kernal은 행렬을 의미, 크기가 크면 이미지 전체가 blur(흐려짐)처리가 많이 됨
# (이미지, 출력 영상 데이터 타입(-1: src와 같은 타입의 dst 생성), 마스크 행렬)

import cv2
import numpy as np

def nothing(x):
    pass

img = cv2.imread('../images/lena.jpg')
cv2.namedWindow('image')
cv2.createTrackbar('K', 'image', 1, 20, nothing)

while 1:
    if cv2.waitKey(1) & 0xFF == 27:
        break
    k = cv2.getTrackbarPos('K', 'image')
    # (0, 0)이면 에러가 발생하므로 1로 치환
    if k == 0:
        k = 1
    # trackbar에 의해 (1, 1) ~ (20, 20) kernal 생성
    kernal = np.ones((k, k), np.float32) / (k * 2)
    dst = cv2.filter2D(img, -1, kernal)

    cv2.imshow('image', dst)
cv2.destroyAllWindows()