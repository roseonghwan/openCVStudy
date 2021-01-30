import cv2
import numpy as np

img = cv2.imread('../images/lena.jpg')

px = img[100, 200]

b = img[100, 200, 0]

img[100, 200] = [255, 255, 255] # 흰색으로 변경
# print(img.item(10, 10, 2)) # Red 값
img.itemset((10, 10, 2), 100) # Red값을 100으로 변경
#print(img.item(10, 10, 2))
print(img.shape) # 행, 열, 체널 개수 확인
print(img.size)
print(img.dtype)

