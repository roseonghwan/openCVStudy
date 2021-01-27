import cv2

img = cv2.imread('../sonny.PNG', cv2.IMREAD_COLOR)
img2 = cv2.imread('../sonny.PNG', cv2.IMREAD_GRAYSCALE)
img3 = cv2.imread('../sonny.PNG', cv2.IMREAD_UNCHANGED)
cv2.imshow('image', img)
cv2.imshow('Gray', img2)
cv2.imshow('Unchanged', img3)
k = cv2.waitKey(0)
if k == 27: # esc
    cv2.destroyAllWindows()
elif k == ord('s'): # s
    cv2.imwrite('../songray.png', img2)
    cv2.destroyAllWindows()