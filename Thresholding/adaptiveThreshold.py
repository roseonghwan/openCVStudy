# 적응 임계처리
import cv2
import numpy as np
from matplotlib import pyplot as plt
# flag-> 0: gray로 읽음 1: color로 읽음 -1: alpha channel까지 포함해 읽음

img = cv2.imread('../images/dave.png', 0)

ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# (이미지, 임계값, thresholding 값을 결정하는 계산 방법, threshold type, thresholding을 적용할 영역 사이즈, 평균이나 가중평균에서 차감할 값)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 2)  # 임계값은 주변영역의 평균값
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 3) # 임계값은 가중치가 가우시안 창 기반 인접 값의 가중치 합

titles = ['Original', 'Global', 'Mean', 'Gaussian']
images = [img, th1, th2, th3]

for i in range(4):
    plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()