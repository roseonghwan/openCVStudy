# image Moment는 대상을 구분할 수 있는 특징
# 특징으로는 Area, Perimeter, 중심점 등
# cv2.boundingRect(cnt): 물건을 둘러싼 최소 사각형

import cv2

img = cv2.imread('../images/rectangle.jpg')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)

image, contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 첫번째 contours의 moment 특징 추출
cnt = contours[0]
M = cv2.moments(cnt)

print(M.items())
# contour면적(contour로 둘러싸인 픽셀 수를 리턴)
'''
for cnt in contours:
    area = cv2.contourArea(cnt)
    print(area) 도 같음
'''
print(cv2.contourArea(cnt))

# contour둘레길이(True->폐곡선 도형을 만들어 둘레길이 구함, false->시작점, 끝점을 연결하지 않고 둘레길이 구함)
print(cv2.arcLength(cnt, True))
print(cv2.arcLength(cnt, False))

# Contour Approximation
# cv2.findContours()함수에 의해 찾은 contours line은 각각 contours point를 가짐
# 이 point의 수를 줄여 근사한 line을 그릴 때 사용됨
# cv2.approxPolyDP(curve(contours point array), epsilon(original curve와 근사치의 최대거리(최대거리가 클수록 더 먼 곳의 point까지 고려하므로 point 수가 줄어듦), closed(폐곡선 여부))
# 리턴 -> 근사치가 적용된 contours point array

from matplotlib import pyplot as plt

img = cv2.imread('../images/bad_rect.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img1 = img.copy()
img2 = img.copy()

ret, thresh = cv2.threshold(imgray, 127, 255, 0)

image, contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]

# 적용하는 숫자가 커질수록 point의 개수 감소
epsilon1 = 0.01 * cv2.arcLength(cnt, True)
epsilon2 = 0.1 * cv2.arcLength(cnt, True)

approx1 = cv2.approxPolyDP(cnt, epsilon1, True)
approx2 = cv2.approxPolyDP(cnt, epsilon2, True)

cv2.drawContours(img, [cnt], 0, (0, 255, 0), 3) # 215개의 point
cv2.drawContours(img1, [approx1], 0, (0, 255, 0), 3) # 21개의 point
cv2.drawContours(img2, [approx2], 0, (0, 255, 0), 3) # 4개의 point

titles = ['Original', '1%', '10%']
images = [img, img1, img2]

for i in range(3):
    plt.subplot(1, 3, i + 1), plt.title(titles[i]), plt.imshow(images[i])
    plt.xticks([]), plt.yticks([])

plt.show()