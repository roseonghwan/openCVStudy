import cv2
import numpy as np


def nothing(x):
    pass


img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('image')

# trackbar를 생성해 named window에 등록
# 트랙바를 지정된 윈도우에 생성하는 함수
# (trackbarName, namedWindow(트랙바를 부착할 윈도우 창), 트랙바가 생성될 때 초기값, 트랙바의 max값, slide 값이 변경될 때 호출되는 callback함수(전달되는 파라미터는 트랙바 포지션)
cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)

switch = '0:OFF\n1:On'
cv2.createTrackbar(switch, 'image', 1, 1, nothing)

while 1:
    cv2.imshow('image', img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

    # 트랙바 값 설정 함수(trackbarName, windowName)
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    s = cv2.getTrackbarPos(switch, 'image')

    if s == 0:
        img[:] = 0  # 모든 행/열 좌표값을 0으로 변경, 검은색
    else:
        img[:] = [b, g, r]  # 모든 행/열 좌표값을 [b,g,r]로 변경

cv2.destroyAllWindows()
