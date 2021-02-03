# 물체를 한 점을 중심으로 회전
# 양의 각도는 시계반대방향으로 회전, 변환행렬 필요
# cv2.getRotationMatrix2D(). (이미지 중심좌표, 회전각도, sclae)

import cv2

img = cv2.imread('../images/logo.png')
rows, cols = img.shape[:2]

# 이미지 중심점을 기준으로 90도 회전하면서 0.5배 scale
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 0.5)
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('Original', img)
cv2.imshow('Rotation', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()