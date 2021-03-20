import cv2

img = cv2.imread('sonny.PNG')
print(img.shape)
print(len(img))
print(len(img[0]))
print(img[0][0])
print(img[0, 0])
print(img[0, 0][0] == 24)
img = img[100:300, 300:500]
cv2.imshow("son", img)
cv2.waitKey(0)
cv2.destroyAllWindows()