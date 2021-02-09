# 지금까지 1차원으로 grayscale 이미지의 pixel의 강도, 즉 빛의 세기를 분석한 결과
# 2D Histogram은 color 이미지의 Hue(색상) & Saturation(채도)를 동시에 분석하는 방법
# 이 결과는 Histogram Back-Projection에 유용하게 사용됨
# Hue와 Saturation으로 분석하므로 대상 이미지를 HSV Format으로 변환을 하고, calcHist()를 적용함
# cv2.clacHist(image, channel(0->Hue, 1->Saturation), bins, range)

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../images/home.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

cv2.imshow('Hist', hist)

plt.imshow(hist)
plt.show()

# x축은 Saturation, y축은 Hue값을 나타냄
# y축을 보면 100 근처에 값이 모여있는 것을 알 수 있음 -> HSV모델에서 H가 100이면 하늘색
# 25 근처에도 값이 모여있음 -> H가 25이면 노란색 ----> 이 이미지는 하늘색과 노란색이 많이 분포되어 있다는 것을 알 수 있다.