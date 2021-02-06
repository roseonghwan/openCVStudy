# cv2.isContourConvex(), contour가 convex인지 아닌지 판단해 t or f 로 판단
# convex란 contour line이 볼록하거나 최소한 평평한 것을 의미

# cv2.isContourConvex(contours[0]) # 외곽선 contour line -> True
# cv2.isContourConvex(contours[1]) # 손 모양 contour line -> Flase

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../images/lightning.jpg')
img1 = img.copy()

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
image, contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[1]

# Straight Rectangle: 대상의 rotation은 무시한 사각형 모양
x, y, w, h = cv2.boundingRect(cnt)
img1 = cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 255, 0), 3) # green

# Rotated Rectangle: 대상을 모두 포함하면서, 최소한의 영역을 차지하는 사각형 모양
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
img1 = cv2.drawContours(img1, [box], 0, (0, 0, 255), 3) # blue

# Minimum Enclosing Circle: contour line을 완전히 포함하는 원 중 가장 작은 원
(x, y), radius = cv2.minEnclosingCircle(cnt)
center = (int(x), int(y))
radius = int(radius)
img1 = cv2.circle(img1, center, radius, (255, 255, 0), 3) # yellow

# Fitting an Ellipse: Contour line을 둘러싸는 타원
ellipse = cv2.fitEllipse(cnt)
img1 = cv2.ellipse(img1, ellipse, (255, 0, 0), 3) #red

titles = ['Original', 'Result']
images = [img, img1]

for i in range(2):
    plt.subplot(1, 2, i + 1), plt.title(titles[i]), plt.imshow(images[i])
    plt.xticks([]), plt.yticks([])

plt.show()