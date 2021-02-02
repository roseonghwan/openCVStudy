# cv2.blur(src, kernal사이즈)
# 박스 형태의 kernal을 이미지에 적용한 후 평균값을 박스의 중심점에 적용
# cv2.blur() 또는 cv2.boxFilter() 함수로 적용 가능

# 가우시안 필터는 가우시안 함수를 이용한 커널을 적용
# 즉, 커널 행렬의 값을 가우시안 함수를 통해서 생성해 적용
# cv2.GaussianBlur(img, kernal사이즈(양수의 홀수), sigmaX)
# 밀도가 동일한 노이즈, 백색노이즈에 효과적

# kernal window와 pixel의 값들을 정렬한 후 중간값을 선택해 적용
# cv2. medianBlur(src, kernal사이즈(1보다 큰 홀수))
# salt-and-pepper noise(점 잡음)에 효과적

# 지금까지는 경계선까지 Blur처리가 되어 경계선이 흐려지는데, Bilateral Filtering은 경계선을 유지하면서 가우시안 Blur처리
# cv2.bilateralFilter(src, pixel지름, sigmaColor(color을 고려한 공간), sigmaSpace(숫자가 크면 멀리 있는 pixel도 고려))
# 가우시안 필터를 적용하고, 가우시안 필터 주변 픽셀까지 고려해 적용한 방식

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../images/lena.jpg')

# pyplot을 사용하기 위해 BGR을 RGB로 변환
b, g, r = cv2.split(img)
img = cv2.merge([r, g, b])

# 일반 Blur
dst1 = cv2.blur(img, (7, 7))

# GaussianBlur
dst2 = cv2.GaussianBlur(img, (5, 5), 0)

# Median Blur
dst3 = cv2.medianBlur(img, 9)

# Bilateral Filtering
dst4 = cv2.bilateralFilter(img, 9, 75, 75)

images = [img, dst1, dst2, dst3, dst4]
titles = ['Original', 'Blur(7X7)', 'Gaussian Blur(5X5)', 'Median Blur', 'Bilateral']

for i in range(5):
    plt.subplot(3, 2, i + 1), plt.imshow(images[i]), plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()