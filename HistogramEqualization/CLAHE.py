# 지금까지의 처리는 이미지의 전체적인 부분에 균일화를 적용한 것임
# 하지만 일반적인 이미지는 밝은 부분과 어두운 부분이 섞여 있으므로 전체에 적용하는 것을 그닥 유용하지 않음(밝은 부분이 더 밝아질 수 있음)
# 이를 해결하기 위해 adaptive histogram equalization을 적용함
# 이미지를 작은 title 형태롤 나누어 그 안에서 equalization을 적용하는 방식
# 하지만 이도 작은 영역이다 보니 작은 노이즈(극단적으로 어둡거나 밝은 영역)이 있으면 이를 반영해버려 원하는 결과를 못 얻음
# 이 문제를 피하기 위해 contrast limit 값을 적용해 이 값을 넘기는 경우 그 영역은 다른 영역에 균일하게 배분해 적용시킴

import cv2
import numpy as np

img = cv2.imread('../images/clahe.png', 0)

# contrast limit이 2이고, title size는 8x8
clache = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
img2 = clache.apply(img)

img = cv2.resize(img, (400, 400))
img2 = cv2.resize(img2, (400, 400))

dst = np.hstack((img, img2)) # 이미지를 같은 행에 붙이기
cv2.imshow('img', dst)
cv2.waitKey()
cv2.destroyAllWindows()

# 그 결과, 이미지의 윤곽선도 유지가 되면서 전체적인 contrast가 높아졌다.