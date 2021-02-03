# 원근법 변환은 직선의 성질만 유지가 되고, 선의 평행성은 유지가 안되는 변환
# 4개의 point의 input과 이동할 output point가 필요
# 변환행렬을 구하기 위해 cv2.getPerspectiveTransform()함수가 필요하며, cv2.warpPerspective()함수에 변환행렬값을 적용해 최종 이미지를 얻음

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../images/perspective.jpg')
# [x,y] 좌표점을 4x2의 행렬로 작성
# 좌표점은 좌상->좌하->우상->우하
pts1 = np.float32([[504, 1003], [243, 1525], [1000, 1000], [1280, 1685]])
# 좌표의 이동점
pts2 = np.float32([[10, 10], [10, 1000], [1000, 10], [1000, 1000]])

# pts1의 좌표에 표시. perspective 변환 후 이동 점 확인
cv2.circle(img, (504, 1003), 20, (255, 0, 0), -1)
cv2.circle(img, (243, 1524), 20, (0, 255, 0), -1)
cv2.circle(img, (1000, 1000), 20, (0, 0, 255), -1)
cv2.circle(img, (1280, 1685), 20, (0, 0, 0), -1)

M = cv2.getPerspectiveTransform(pts1, pts2)

dst = cv2.warpPerspective(img, M, (1100, 1100))

plt.subplot(121), plt.imshow(img), plt.title('image')
plt.subplot(122), plt.imshow(dst), plt.title('Perspective')
plt.show()