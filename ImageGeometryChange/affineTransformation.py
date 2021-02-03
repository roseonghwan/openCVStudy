# 선의 평행성은 유지가 되면서 이미지 변환(이동, 확대, scale, 반전 포함)
# affine변환을 위해서는 3개 Match가 되는 점이 있으면 반환행렬을 구할 수 있음

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../images/chessboard.jpg')
rows, cols, ch = img.shape

pts1 = np.float32([[200, 100], [400, 100], [200, 200]])
pts2 = np.float32([[200, 300], [400, 200], [400, 200]])

# pst1의 좌표에 표시. Affine 변환 후 이동 점 확인
cv2.circle(img, (200, 100), 10, (255, 0,  0), -1)
cv2.circle(img, (400, 100), 10, (0, 255, 0), -1)
cv2.circle(img, (200, 200), 10, (0, 0, 255), -1)

M = cv2.getAffineTransform(pts1, pts2)

dst = cv2.warpAffine(img, M, (cols, rows))

plt.subplot(121), plt.imshow(img), plt.title('image')
plt.subplot(122), plt.imshow(dst), plt.title('Affine')
plt.show()