# 이미지의 사이즈 변경
#  cv2.resize(). (이미지, 가로/세로 형태의 튜플, 가로사이즈의 배수, 세로사이즈의 배수, 보간법)
# 사이즈 줄일 때: cv2.INTER_AREA, 크게할 때: cv2.INTER_CUBIC, cv2.INTER_LINEAR
import cv2

img = cv2.imread('../images/logo.png')

# 행: Height, 열: Width
height, width = img.shape[:2]

# 이미지 축소
shrink = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# Manual size 지정
zoom1 = cv2.resize(img, (width * 2, height * 2), interpolation=cv2.INTER_CUBIC)

# 배수 size 지정
zoom2 = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

cv2.imshow('Origianl', img)
cv2.imshow('Shrink', shrink)
cv2.imshow('Zoom1', zoom1)
cv2.imshow('Zoom2', zoom2)

cv2.waitKey(0)
cv2.destroyAllWindows()