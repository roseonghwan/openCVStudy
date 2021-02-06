# convex Hull이란 contours point를 모두 포함하는 볼록한 외관선을 의미
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../images/hand.png')
img1 = img.copy()

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)

image, contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[1] # 1이 손모양 주변의 contour
hull = cv2.convexHull(cnt)

cv2.drawContours(img1, [hull], 0, (0, 255, 0), 3)

titles = ['Original', 'Convex Hull']
images = [img, img1]

for i in range(2):
    plt.subplot(1, 2, i + 1), plt.title(titles[i]), plt.imshow(images[i])
    plt.xticks([]), plt.yticks([])

plt.show()