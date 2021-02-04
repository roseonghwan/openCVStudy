# Contours: 영역의 경계선을 연결한 선(등고선, 일기예보), 대상의 외형을 파악하는데 유용
# 정확도를 높이기 위해 BinaryImage사용, thresholding이나 cannyedge를 선처리롤 수행
# 대상은 흰색, 배경은 검은색

# cv2.findContours(image, mode(countours를 찾는 방법), method(contours를 찾을때 사용하는 근사치 방법))
# 리턴 -> image, contours, hierachy

# cv2.drawContours(image, contours(contours정보), contourIdx(contours list type에서 몇번째 contours line을 그릴 것인지, -1이면 전체), 색, contours line 두께)
# image는 검은색, 흰색으로만 구성된 binary image이어야 함
# 리턴 -> image에 contours가 그려진 결과

import cv2

img = cv2.imread('../images/rectangle.jpg')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 회색으로 변경 -> binary 이미지로 바꾸기 위해 필요한 단계

# threshold를 이용해 binary image로 전환
ret, thresh = cv2.threshold(imgray, 127, 255, 0) # 흰색, 검은색으로 구성됨

# contours는 point의 list형태
# hierachy는 contours line의 계층구조
image, contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
image = cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()