# 히스토그램은 이미지의 밝기의 분포를 그래프로 표현한 방식(이미지의 전체의 밝기 분포와 채도를 알 수 있다)
# x축: 색의 강도(0~255), y축: x축에 해당하는 색의 개수
# BINS: 히스토그램 그래프 x축의 간격, DIMS: 이미지에서 조사하고자 하는 값, RANGE: 측정하고자 하는 값의 범위
# cv2.calcHist(image(array형태), channels(분석체널(x축의 대상, 이미지가 grayscale이면 [0], color이미지면[1 or 2 or3](1:B, 2:G, 3:R)), mask(None이면 전체영역), BINS값, RANGE값)

import cv2
import numpy as np
import random
from matplotlib import pyplot as plt

img1 = cv2.imread('../images/flower1.jpg', 0)
img2 = cv2.imread('../images/flower2.jpg', 0)

hist1 = cv2.calcHist([img1], [0], None, [256], [0, 256])
hist2 = cv2.calcHist([img2], [0], None, [256], [0, 256])

plt.subplot(221), plt.imshow(img1, 'gray'), plt.title('Red Line')
plt.subplot(222), plt.imshow(img2, 'gray'), plt.title('Green Line')
plt.subplot(223), plt.plot(hist1, color='r'), plt.plot(hist2, color='g')
plt.xlim([0, 256])
plt.show()