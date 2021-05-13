<<<<<<< HEAD
# CamShift: 우선 평균 알고리즘으로 이동 위치 계산
# MeanShift는 반환값으로 반복을 몇 번 헀는지에 대한 값을 반환했지만
# CamShift는 반환값으로 회전되어 있는 사각형을 표현하는 정보를 반환

import cv2
import numpy as np

col, width, row, height = -1, -1, -1, -1
frame = None
frame2 = None
inputMode = False
rectangle = False
trackWindow = None
roi_hist = None
channels = [0, 1]
ranges = [0, 180, 0, 256]

def onMouse(event, x, y, flags, param):
    global col, width, row, height, frame, frame2, inputMode, rectangle, roi_hist, trackWindow

    if inputMode == True:
        if event == cv2.EVENT_LBUTTONDOWN:
            rectangle = True
            col, row = x, y

        elif event == cv2.EVENT_MOUSEMOVE:
            if rectangle == True:
                frame = frame2.copy()
                cv2.rectangle(frame, (col, row), (x, y), (0, 255, 0), 2)
                cv2.imshow('frame', frame)

        elif event == cv2.EVENT_LBUTTONUP:
            inputMode = False
            rectangle = False
            cv2.rectangle(frame, (col, row), (x, y), (0, 255, 0), 2)
            height, width = abs(row - y), abs(col - x)
            trackWindow = (col, row, width, height)
            roi = frame[row:row + height, col:col + width]
            # 지정한 영역을 HSV로 변환
            roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
            # roi 이미지 히스트그램 구하기
            roi_hist = cv2.calcHist([roi], channels, None, [90, 128], ranges)
            # 이미지 정규화를 통해 픽셀 값이 고르게 펴져 화질 개선
            cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
    return


def camShift():
    global frame, frame2, inputMode, trackWindow, roi_hist

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Video open failed!")
        exit()

    cv2.namedWindow('frame')
    cv2.setMouseCallback('frame', onMouse)

    # CamShift 알고리즘 종료 기준
    # 최대 10번 반복하며, 정확도가 1이하이면(이동크기가 1픽셀보다 작으면) 종료
    termination = (cv2.TermCriteria_EPS | cv2.TermCriteria_COUNT, 10, 1)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Frame read failed!")
            break

        # 마우스로 영역을 표시해준 후
        if trackWindow is not None:
            # 정지된 화면을 HSV로 변환
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            # 위에서 지정한 roi의 히스토그램을 역투영-> 원하는 색 도출 가능
            dst = cv2.calcBackProject([hsv], channels, roi_hist, ranges, 1)
            # dst: 관심 객체에 대한 히스토그램 역투영 영상, termination: 알고리즘 종료 기준
            # ret: 알고리즘 내부 반복 횟수, trackWindow: 초기 검색 영역 윈도우 & 결과 영역 반환(튜플)
            ret, trackWindow = cv2.CamShift(dst, trackWindow, termination)
            '''
            x, y, w, h = trackWindow
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            '''
            pts = cv2.boxPoints(ret)
            pts = np.int0(pts)
            cv2.polylines(frame, [pts], True, (0, 255, 0), 2)

        cv2.imshow('frame', frame)

        k = cv2.waitKey(60) & 0xFF
        if k == 27:
            break
        # i를 누를 때 화면을 정지하고 영역을 선택할 수 있다.
        if k == ord('i'):
            print("Select Area for MeanShift and Enter a key")
            inputMode = True
            frame2 = frame.copy()

            while inputMode == True:
                cv2.imshow('frame', frame)
                cv2.waitKey(0)
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    camShift()
=======
# CamShift: 우선 평균 알고리즘으로 이동 위치 계산
# MeanShift는 반환값으로 반복을 몇 번 헀는지에 대한 값을 반환했지만
# CamShift는 반환값으로 회전되어 있는 사각형을 표현하는 정보를 반환

import cv2
import numpy as np

col, width, row, height = -1, -1, -1, -1
frame = None
frame2 = None
inputMode = False
rectangle = False
trackWindow = None
roi_hist = None
channels = [0, 1]
ranges = [0, 180, 0, 256]

def onMouse(event, x, y, flags, param):
    global col, width, row, height, frame, frame2, inputMode, rectangle, roi_hist, trackWindow

    if inputMode == True:
        if event == cv2.EVENT_LBUTTONDOWN:
            rectangle = True
            col, row = x, y

        elif event == cv2.EVENT_MOUSEMOVE:
            if rectangle == True:
                frame = frame2.copy()
                cv2.rectangle(frame, (col, row), (x, y), (0, 255, 0), 2)
                cv2.imshow('frame', frame)

        elif event == cv2.EVENT_LBUTTONUP:
            inputMode = False
            rectangle = False
            cv2.rectangle(frame, (col, row), (x, y), (0, 255, 0), 2)
            height, width = abs(row - y), abs(col - x)
            trackWindow = (col, row, width, height)
            roi = frame[row:row + height, col:col + width]
            # 지정한 영역을 HSV로 변환
            roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
            # roi 이미지 히스트그램 구하기
            roi_hist = cv2.calcHist([roi], channels, None, [90, 128], ranges)
            # 이미지 정규화를 통해 픽셀 값이 고르게 펴져 화질 개선
            cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
    return


def camShift():
    global frame, frame2, inputMode, trackWindow, roi_hist

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Video open failed!")
        exit()

    cv2.namedWindow('frame')
    cv2.setMouseCallback('frame', onMouse)

    # CamShift 알고리즘 종료 기준
    # 최대 10번 반복하며, 정확도가 1이하이면(이동크기가 1픽셀보다 작으면) 종료
    termination = (cv2.TermCriteria_EPS | cv2.TermCriteria_COUNT, 10, 1)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Frame read failed!")
            break

        # 마우스로 영역을 표시해준 후
        if trackWindow is not None:
            # 정지된 화면을 HSV로 변환
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            # 위에서 지정한 roi의 히스토그램을 역투영-> 원하는 색 도출 가능
            dst = cv2.calcBackProject([hsv], channels, roi_hist, ranges, 1)
            # dst: 관심 객체에 대한 히스토그램 역투영 영상, termination: 알고리즘 종료 기준
            # ret: 알고리즘 내부 반복 횟수, trackWindow: 초기 검색 영역 윈도우 & 결과 영역 반환(튜플)
            ret, trackWindow = cv2.CamShift(dst, trackWindow, termination)
            '''
            x, y, w, h = trackWindow
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            '''
            pts = cv2.boxPoints(ret)
            pts = np.int0(pts)
            cv2.polylines(frame, [pts], True, (0, 255, 0), 2)

        cv2.imshow('frame', frame)

        k = cv2.waitKey(60) & 0xFF
        if k == 27:
            break
        # i를 누를 때 화면을 정지하고 영역을 선택할 수 있다.
        if k == ord('i'):
            print("Select Area for MeanShift and Enter a key")
            inputMode = True
            frame2 = frame.copy()

            while inputMode == True:
                cv2.imshow('frame', frame)
                cv2.waitKey(0)
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    camShift()
>>>>>>> 50ba5fb860587880913a1b25544fc3e9e62e9d9d
