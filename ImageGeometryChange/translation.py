# 이미지 위치를 변경
# cv2.warpAffine(). (이미지, 변환행렬, output 이미지 사이즈(튜플))
# width-> 열 수(cols), height-> 행 수(rows)

import cv2
import numpy as np

img = cv2.imread('../images/logo.png')
rows, cols = img.shape[:2]

# 변환 행렬, x축으로 10, y축으로 20 이동
M = np.float32([[1, 0, 10], [0, 1, 20]])

dst = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow('Original', img)
cv2.imshow('Translation', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
