<<<<<<< HEAD
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 320)
cap.set(4, 240)

while True:
    ret, frame = cap.read()
    if ret == True:
        # BGR->HSV로 변환
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # red 영역의 from ~ to
        lower_red = np.array([0, 70, 50])
        upper_red = np.array([10, 255, 255])

        # 이미지에서 red 영역
        mask = cv2.inRange(hsv, lower_red, upper_red)  # range 범위 안에 들어오면 흰색(255)표시, 아니면 검은색(0)으로 표시
        res = cv2.bitwise_and(frame, frame, mask=mask)  # mask와 원본 이미지를 비트연산
        cv2.imshow('Mask', mask)
        cv2.imshow('Original', frame)
        cv2.imshow('res', res)
        frame[mask > 0] = (255, 0, 0)  # frame에서는 픽셀 값을 읽으므로 HSV가 아닌 BGR # 위에 mask값이 되면 색을 바꿔줌
        cv2.imshow('Change', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
=======
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 320)
cap.set(4, 240)

while True:
    ret, frame = cap.read()
    if ret == True:
        # BGR->HSV로 변환
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # red 영역의 from ~ to
        lower_red = np.array([0, 70, 50])
        upper_red = np.array([10, 255, 255])

        # 이미지에서 red 영역
        mask = cv2.inRange(hsv, lower_red, upper_red) # range 범위 안에 들어오면 흰색(255)표시, 아니면 검은색(0)으로 표시
        res = cv2.bitwise_and(frame, frame, mask=mask) # mask와 원본 이미지를 비트연산
        cv2.imshow('Mask', mask)
        cv2.imshow('Original', frame)
        cv2.imshow('res', res)
        frame[mask > 0] = (255, 0, 0) # frame에서는 픽셀 값을 읽으므로 HSV가 아닌 BGR # 위에 mask값이 되면 색을 바꿔줌
        cv2.imshow('Change', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
>>>>>>> 50ba5fb860587880913a1b25544fc3e9e62e9d9d
