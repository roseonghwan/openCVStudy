# Aspect Ratio: Contours Line의 가로 세로 비율 속성
# Extend: Contour Line을 포함하는 사각형 면적대비 Contour의 면적 비율
# Solidity: Solidity Ratio(고형비)
# Extream Points: Contour Line의 좌우상하의 끝점을 찾는 방법

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../images/UK.jpg')
img1 = img.copy()

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 125, 255, 0)

image, contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[14] # 14번째가 지도의 contour line

# 끝점 좌표 찾기
# cnt[:,:,0] -> point의 x좌표값만 포함하는 배열, argmin()을 적용하면 x좌표가 가장 작은 array의 위치가 나옴
# 그 위치를 다시 cnt에서 찾으면 가장 왼쪽에 있는 좌표를 얻들 수 있음
leftmost = tuple(cnt[cnt[:, :, 0].argmin()][0])
rightmost = tuple(cnt[cnt[:, :, 0].argmax()][0])
topmost = tuple(cnt[cnt[:, :, 1].argmin()][0])
bottommost = tuple(cnt[cnt[:, :, 1].argmax()][0])

img1 = cv2.drawContours(img1, cnt, -1, (255, 0, 0), 5)

titles = ['Original', 'Result']
images = [img, img1]

for i in range(2):
    plt.subplot(1, 2, i + 1), plt.title(titles[i]), plt.imshow(images[i])
    plt.xticks([]), plt.yticks([])

plt.show()