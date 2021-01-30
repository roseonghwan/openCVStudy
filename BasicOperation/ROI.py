import cv2

img = cv2.imread('../images/baseball-player.jpg')
cv2.imshow('image1', img)
ball = img[409:454, 817:884] # img[행 시작점: 끝점, 열 시작점: 끝점]
img[470:515, 817:884] = ball # 동일 역역 copy
cv2.imshow('image', img)

b = img[:, :, 0] # 0:Blue, 1:Green, 2:Red
img[:, :, 2] = 0 # red를 제거하는 효과
cv2.imshow('image3', img)

b, g, r = cv2.split(img) # 각 체널별로 분리
img = cv2.merge((r, g, b)) # b,g,r->r,g,b

cv2.imshow('image2', img)
cv2.waitKey(0)
cv2.destroyAllWindows()