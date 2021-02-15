# 허프변환: 이미지에서 모양을 찾는 가장 유명한 방법
# 기본적으로 직선의 방정식을 이용.
# cv2.HoughLines(image, rho(r값의 범위: 0~1 실수), theta(0~180 정수), threshold(만나는 점의 기준, 숫자가 작으면 많은 선이 검출되지만 부정확, 많으면 정확도 상승))
# r의 정밀도->1로 지정했으면 1픽셀 단위, theta의 정밀도->1도로 지정했으면 라이언 단위
# 리턴->(r,theta)값들의 배열을 리턴

import cv2
import numpy as np

img = cv2.imread('../images/chessboard/frame01.jpg')
img_original = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3) # 우선 canny edge로 경계한 검출한 뒤 허프 선 검출

lines = cv2.HoughLines(edges, 1, np.pi / 180, 100)

for i in range(len(lines)):
    for rho, theta in lines[i]:
        # y = mx + c 를 삼각함수로 변형하면 r = xCos(theta) + ySin(theta)로 표현
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b)) # why 1000???
        y1 = int(y0 + 1000 * a)
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * a)

        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

res = np.vstack((img_original, img)) # 이미지를 위아래로 연결
cv2.imshow('img', res)

cv2.waitKey(0)
cv2.destroyAllWindows()