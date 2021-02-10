# 전 파일은 numpy를 이용한 균일화 작업
# 지금은 cv2를 이용한 균일화 작업
import cv2
import numpy as np


img = cv2.imread('../images/hist_unequ.jpg', 0)

# openCV의 Equalization 함수
img2 = cv2.equalizeHist(img)
img = cv2.resize(img, (400, 400))
img2 = cv2.resize(img2, (400, 400))

dst = np.hstack((img, img2))
cv2.imshow('img', dst)
cv2.waitKey()
cv2.destroyAllWindows()