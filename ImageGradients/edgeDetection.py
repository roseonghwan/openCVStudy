# gradient(기울기)는 스칼라장(공간)이서 최대 증가율을 나타내는 벡터을 뜻
# gradient는 영상의 edge 및 그 방향을 찾는 용도
# 이미지(x, y)에서의 벡터값을 구해 해당 pixel이 edge에 얼마나 가깝고, 그 방향이 어디인지 파악 가능

# sobel & scharr Filter -> 가우시안 smoothing과 미분을 이용
# 노이즈가 있는 이미지에 적용하면 좋음
# cv2.Sobel(src, ddepth(output이미지의 depth(-1이면 input image와 동일)), dx(x축 미분차수), dy(y축 미분차수), kernal사이즈(-1이면 3x3으로 적용))
# cv2.Scharr(Sobel과 파라미터 동일)하나 ksize가 sobel의 3x3보다 더 정확

# Laplacian -> 이미지의 가로와 세로에 대한 gradient를 2차 미분한 값
# blob(주위의 pixel과 확연한 picel차이를 나타내는 덩어리) 검출에 많이 사용됨
# cv2.Laplacian(src, ddepth)

# CannyEdgeDetection -> 노이즈 제거(5x5 가우시안 필터 사용), edge Gradient Detection(경계값 후보군 선별), Non-maximum Suppression(이미지의 pixel을 full scan해 edge가 아닌 pixel 제거), Hysteresis Thresholding(지금까지 edge로 판단된 pixel이 진짜 edge인지 판별) 순으로 사용
# cv2.Canny(image, threshold1(Hysteresis Thresshold작업에서 min값), threshold2(작업에서 max값)

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../images/dave.png')
canny = cv2.Canny(img, 30, 70)

laplacian = cv2.Laplacian(img, cv2.CV_8U)
sobelx = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_8U, 0, 1, ksize=3)

images = [img, laplacian, sobelx, sobely, canny]
titles = ['Origianl', 'Laplacian', 'Sobel X', 'Sobel Y', 'Canny']

for i in range(5):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i]), plt.title([titles[i]])
    plt.xticks([]), plt.yticks([])

plt.show()