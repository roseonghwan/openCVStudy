import cv2
import numpy as np

cap = cv2.VideoCapture(0)


def make_gray(img):
    be_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return be_gray


while True:
    ret, frame = cap.read()
    if ret:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        cv2.imshow('origin', frame)
        # red 영역의 from ~ to
        lower_red = np.array([161, 155, 84])
        upper_red = np.array([179, 255, 255])

        # 이미지에서 red 영역
        red_mask = cv2.inRange(hsv, lower_red, upper_red)  # range 범위 안에 들어오면 흰색(255)표시, 아니면 검은색(0)으로 표시
        res = cv2.bitwise_and(frame, frame, mask=red_mask)  # mask와 원본 이미지를 비트연산

        # 빨간 화살표를 추출한 이미지를 gray이미지로 변환
        gray = make_gray(res)

        ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        _, contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:

            epsilon = 0.005 * cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, epsilon, True)

            size = len(approx)

            cv2.line(frame, tuple(approx[0][0]), tuple(approx[size - 1][0]), (0, 0, 255), 3)
            for k in range(size - 1):
                cv2.line(frame, tuple(approx[k][0]), tuple(approx[k + 1][0]), (0, 0, 255), 3)

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        red_mask = cv2.inRange(hsv, lower_red, upper_red)  # range 범위 안에 들어오면 흰색(255)표시, 아니면 검은색(0)으로 표시
        res = cv2.bitwise_and(frame, frame, mask=red_mask)  # mask와 원본 이미지를 비트연산
        gray = make_gray(res)
        corners = cv2.goodFeaturesToTrack(gray, 5, 0.01, 20)
        try:
            for i in corners:
                cv2.circle(res, tuple(i[0]), 3, (0, 255, 0), 2)
        except:
            continue
        cv2.imshow('result', res)
        corners = np.ravel(corners)
        x = []
        for i, data in enumerate(corners):
            if i % 2 != 0:
                continue
            else:
                x.append(data)
        big = max(x)
        small = min(x)
        mid = (big + small) / 2
        rcount = 0
        lcount = 0
        for i in x:
            if i > mid:
                rcount += 1
            else:
                lcount += 1
        if rcount > lcount:
            print('right')
        else:
            print('left')

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
