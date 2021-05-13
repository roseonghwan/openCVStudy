<<<<<<< HEAD
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret == True:
        # BGR->HSV로 변환
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # red 영역의 from ~ to
        lower_red = np.array([161, 155, 84])
        upper_red = np.array([179, 255, 255])

        # 이미지에서 red 영역
        red_mask = cv2.inRange(hsv, lower_red, upper_red)  # range 범위 안에 들어오면 흰색(255)표시, 아니면 검은색(0)으로 표시
        res = cv2.bitwise_and(frame, frame, mask=red_mask)  # mask와 원본 이미지를 비트연산
        cv2.imshow('Mask', red_mask)
        cv2.imshow('Original', frame)
        # 빨간 화살표를 추출한 이미지를 gray이미지로 변환
        gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Gray", gray)
        # corner 검출
        dst = cv2.cornerHarris(gray, 2, 3, 0.04)
        # 검출된 코너 부분을 좀더 확대(필수 x)
        # dst = cv2.dilate(dst, None)
        cv2.imshow("dst", dst)
        # 변화량 결과의 최댓값 * 상수이상의 좌표만 표시
        # 빨간 화살표를 추출한 이미지에서 dst.max()에 곱한 상수를 적절하게 조절하면 검출된 코너를 최적화해 초록색으로 표시
        res[dst > 0.4 * dst.max()] = [0, 255, 0]
        cv2.imshow('res', res)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
=======
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret == True:
        # BGR->HSV로 변환
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # red 영역의 from ~ to
        lower_red = np.array([161, 155, 84])
        upper_red = np.array([179, 255, 255])

        # 이미지에서 red 영역
        red_mask = cv2.inRange(hsv, lower_red, upper_red)  # range 범위 안에 들어오면 흰색(255)표시, 아니면 검은색(0)으로 표시
        res = cv2.bitwise_and(frame, frame, mask=red_mask)  # mask와 원본 이미지를 비트연산
        cv2.imshow('Mask', red_mask)
        cv2.imshow('Original', frame)
        # 빨간 화살표를 추출한 이미지를 gray이미지로 변환
        gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Gray", gray)
        # corner 검출
        dst = cv2.cornerHarris(gray, 2, 3, 0.04)
        # 검출된 코너 부분을 좀더 확대(필수 x)
        # dst = cv2.dilate(dst, None)
        cv2.imshow("dst", dst)
        # 변화량 결과의 최댓값 * 상수이상의 좌표만 표시
        # 빨간 화살표를 추출한 이미지에서 dst.max()에 곱한 상수를 적절하게 조절하면 검출된 코너를 최적화해 초록색으로 표시
        res[dst > 0.4 * dst.max()] = [0, 255, 0]
        cv2.imshow('res', res)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
>>>>>>> 50ba5fb860587880913a1b25544fc3e9e62e9d9d
