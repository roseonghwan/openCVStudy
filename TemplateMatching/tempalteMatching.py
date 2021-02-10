# 템플릿 매칭은 원본 이미지에서 특정 이미지를 찾는 방법
# 이 때 사용하는 함수는 cv2.matchTemplate()
# 원본 이비지에 템플릿 이미지를 좌측상단부터 미끄러지듯이 우측으로 이동하면서 계속 비교
# 리턴-> Gray이미지로, 원본의 픽셀이 템플릿 이미지와 유사한 정도를 표현, 이 때 강도는 매칭 방법에 따라 다름
# cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED는 가장 어두운 곳이 매칭지점이고, 나머지는 가장 밝은 곳이 매칭 지점

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../images/capture 0.png', 0)  # 0이면 GrayScale로 읽음
img2 = img.copy()

template = cv2.imread('../images/cap_template.png', 0)

# template 이미지의 가로/세로
w, h = template.shape[::-1]


# Template Match Method
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
for meth in methods:
    img = img2.copy()
    method = eval(meth)

    # cv2.matchTemplate(원본이미지, 템플릿이미지, 템플릿매칭 플래그)
    res = cv2.matchTemplate(img, template, method)
    # cv2.minMaxLoc():  행렬 또는 영상에서 최솟값, 최댓값, 그리고 최솟값과 최댓값 위치를 찾을 때 사용합니다.
    min_val, max_val, min_loc, max_loc, = cv2.minMaxLoc(res) # 템플릿과 일치하는 사각 영역의 왼쪽 위 코너 위치를 지정

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc

    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(img, top_left, bottom_right, (0, 0, 255), 5)

    plt.subplot(121), plt.title(meth), plt.imshow(res, cmap='gray'), plt.yticks([]), plt.xticks([])
    plt.subplot(122), plt.imshow(img, cmap='gray')

    plt.show()
