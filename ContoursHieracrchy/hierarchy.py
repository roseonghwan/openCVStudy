# 여러개의 Contours가 존재하고, 그 사이에 서로 포함하는 관계를 Contours Hierarchy
# 이런 관계를 파악하기 위해서는 cv2.findContours()에 Contour Retrieval Mode값에 의해서 결정됨
import cv2
import numpy as np
import random
from matplotlib import pyplot as plt

img = cv2.imread('../images/imageHierarchy.png')

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 125, 255, 0)

image, contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for i in range(len(contours)):
    # 각 Contour Line을 구분하기 위해서 Color Random생성
    b = random.randrange(1, 255)
    g = random.randrange(1, 255)
    r = random.randrange(1, 255)

    cnt = contours[i]
    img = cv2.drawContours(img, [cnt], -1, (b, g, r), 2)

    titles = ['Result']
    images = [img]

for i in range(1):
    plt.subplot(1, 1, i + 1), plt.title(titles[i]), plt.imshow(images[i])
    plt.xticks([]), plt.yticks([])

plt.show()

# RETR_LIST -> shape는 (1, x, 4)의 형태, 여기서 3번째 차원의 4개의 값이 hierarchy를 표현
# 각 값의 의미는 (next, prev, child, parent)
# 선/후 관계만 표현하고, parent/child관계(모두 -1)를 표현하지 않은 모드

# RETR_EXTERNAL -> 가장 바깥쪽에 있는 contour만을 return

# RETR_CCOMP -> hierachy를 2레벨로 표현. 바깥쪽은 모두 1레벨, 안에 포함된건 2레벨

# RETR_TREE -> Hierarchy를 완전히 표현. 즉 누구에게도 포함되지 않은 contour는 hierarchy-0이 되고, 그 안쪽으로 포함되는 contours는 순서대로 hierachy를 부여받음
