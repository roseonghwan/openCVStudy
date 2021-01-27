import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../sonny.PNG', cv2.IMREAD_COLOR)
b, g, r = cv2.split(img)

img2 = cv2.merge([r, g, b])
plt.imshow(img2)
plt.xticks([]) # x축 눈금
plt.yticks([]) # y축 눈금
plt.show()
# openCV는 BGR, Matplot은 RGB 이미지로 보여줌
print(cv2.__version__)
