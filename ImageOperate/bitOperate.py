import cv2
import numpy as np

img1 = cv2.imread('../images/logo.png')
img2 = cv2.imread('../images/lena.jpg')
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)

# 삽입할 이미지의 row, col, channel 정보
rows, cols, channels = img1.shape

# 대상 이미지에서 삽입할 이미지의 영역을 추출
roi = img2[0:rows, 0:cols]
cv2.imshow('roi', roi)

# mask를 만들기 위해서 img1을 gray로 변경 후 binary image로 전환
# mask는 logo부분이 흰색(255), 바탕은 검은색(0)
# mask_inv는 logo부분이 검은색(0), 바탕은 흰색(255)

img2gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
# (이미지, 임계값(임계값보다 크면 백, 작으면 흑), 임게값을 넘었을 때 적용할 값, type)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# bitwise_and는 둘 다 0이 아닌 경우만 값을 통과시킴
# 즉, mask가 검정이 아닌 경우만 통과되므로 mask영역 이외는 모두 제거됨
# 아래 img1_fg는 bg가 제거되고, fg(logo 부분만) 남음
# img2_bg는 roi영역에서 logo부분이 제거되고 bg만 남음
# bitwise_and : 두 부분 모두 흰색인 부분만
img1_fg = cv2.bitwise_and(img1, img1, mask=mask) # 로고만 남음
img2_bg = cv2.bitwise_and(roi, roi, mask=mask_inv) # 배경만 남음

# 2개의 이미지를 합치면 바탕은 제거되고, logo부분만 합쳐짐
dst = cv2.add(img1_fg, img2_bg)
cv2.imshow('dst', dst)

# 합쳐진 이미지를 원본 이미지에 추가
img2[0:rows, 0:cols] = dst
cv2.imshow('img2_bg', img2_bg)
cv2.imshow('img1_fg', img1_fg)
cv2.imshow('mask_inv', mask_inv)
cv2.imshow('mask', mask)
cv2.imshow('res', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()