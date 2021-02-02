import cv2
import numpy as np
from matplotlib import pyplot as plt

# 아래의 인자 kernal부분은 cv2.getStructuringElement()로 구함
# cv2.getStructuringElement(shape(element모양), ksize(structing element 사이즈))
# MORPH_RET: 사각형, MORPH_ELLIPSE: 타원형, MORPH_CROSS: 십자가

# 이미지를 segmentation하여 단순화, 제거, 보정을 통해 형태를 파악하는 목적
# dilation(팽창), erosion(침식), 2개를 조합한 opening, closing
# 여기에는 2가지 input이 있는데 하나는 원본이미지, 하나는 structing element

# Erosion(침식): pixel에 structing element를 적용하여 하나라도 0이 있으면 대상 pixel을 제거
# 작은 object를 제거하는 효과
# cv2.erode(src, kernal(structing element), anchor(structing element 중심(디폴트:(-1, -1)), erosion적용 반복횟수)

# Dilation(팽창): Erosion과 반대로 대상을 확장한 후 작은 구멍을 채우는 방법
# Erosion과 마찬가지로 각 pixel에 structing element 적용
# 대상 pixel에 대해 OR연산 수행
# 겹치는 부분이 하나라도 있으면 이미지 확장
# 경계가 부드러워지고, 구멍이 메꿔지는 효과
# cv2.diation(src, kernal(structing element), anchor(structing element의 중심(디폴트:(-1, -1), dilation적용 반복횟수)

# opening: erosion 적용 후 dilation 적용, 작은 obejct나 돌기 제거에 적합
# closing: dilation 적용 후 erosion 적용, 전체적인 윤곽 파악에 적합
# cv2.morphologyEX(src, op(type of a morphological operation), kernal(structing element))

dotImage = cv2.imread('../images/dot_image.png')
holeImage = cv2.imread('../images/hole_image.png')
orig = cv2.imread('../images/morph_origin.png')

kernal = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
# kernal = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
# kernal = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))

erosion = cv2.erode(dotImage, kernal, iterations=1)
dilation = cv2.dilate(holeImage, kernal, iterations=1)

opening = cv2.morphologyEx(dotImage, cv2.MORPH_OPEN, kernal)
closing = cv2.morphologyEx(dotImage, cv2.MORPH_CLOSE, kernal)
gradient = cv2.morphologyEx(dotImage, cv2.MORPH_GRADIENT, kernal)
tophat = cv2.morphologyEx(dotImage, cv2.MORPH_TOPHAT, kernal)
blackhat = cv2.morphologyEx(dotImage, cv2.MORPH_BLACKHAT, kernal)

images = [dotImage, erosion, opening, holeImage, dilation, closing, gradient, tophat, blackhat]
titles = ['Dot Image', 'Erosion', 'Opening', 'Hole Image', 'Dilation', 'Closing', 'Gradient', 'Tophat', 'Blackhot']

for i in range(9):
    plt.subplot(3, 3, i + 1), plt.imshow(images[i]), plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()