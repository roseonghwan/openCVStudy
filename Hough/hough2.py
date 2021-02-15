# 확률 허프 변환: 허프변환은 모든 점에 대해 계산을 하므로 오래걸리는 것을 개선해 임의의 점을 이용해 직선을 찾음
# cv2.HoughLinesP(image, rho(r 값의 범위), theta, threshold(만나는 점의 기준(숫자가 적으면 많은 선이 검출되지만 정확도가 떨어짐, 크면 정확도 향상), 선의 최소길이(이 값보다 작으면 reject), 선과 선 사이의 최대 허용 간격(이 값보다 크면 reject))
# 장점은 선의 시작점과 끝점을 리턴해주므로 쉽게 화면에 표현 가능

import cv2
import numpy as np

img = cv2.imread('../images/hough_images.jpg')
edges = cv2.Canny(img, 50, 200, apertureSize=3)

minLineLength = 100
maxLineGap = 10

lines = cv2.HoughLinesP(edges, 1, np.pi / 360, 100, minLineLength, maxLineGap)
for i in range(len(lines)):
    for x1, y1, x2, y2 in lines[i]:
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 3)

cv2.imshow('img1', img)
cv2.waitKey(0)
cv2.destroyAllWindows()