import cv2
import numpy as np


# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)

# calllback 함수
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 100, (255, 0, 0), -1)


# 빈 이미지 생성
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)  # (window이름, callback함수, 함수에는 (event, x, y, flags, param)이 전달됨, callback에 전달되는 데이터)

while 1:
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
