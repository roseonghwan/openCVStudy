# 이미지를 Equalization을 하면 동일한 밝기가 되므로 동일한 환경에서 작업이 가능
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../images/hist_unequ.jpg')


hist, bins = np.histogram(img.flatten(), 256, [0, 256])
cdf = hist.cumsum()

# cdf의 값이 0이 되는 경우 mask처리를 해 계산에서 제외
# mask처리가 되면 numpy 계산에서 제외가 됨
# 아래는 cdf array에서 값이 0인 부분을 mask 처리
cdf_m = np.ma.masked_equal(cdf, 0)

# Histogram Equalization 공식
cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())

# Mask처리를 했던 부분을 다시 0으로 변환
cdf = np.ma.filled(cdf_m, 0).astype('uint8')

img2 = cdf[img]
plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.subplot(122), plt.imshow(img2), plt.title('Equalization')
plt.show()