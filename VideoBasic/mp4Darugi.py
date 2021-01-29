import cv2

cap = cv2.VideoCapture(0)
print('width: {0}, height: {1}'.format(cap.get(3), cap.get(4)))
cap.set(3, 320)
cap.set(4, 240)

while True:
    # ret: frame capture결과(boolean)
    # frame: Capture한 frame
    ret, frame = cap.read()

    if ret:
        # 이미지 반전, 0: 상하, 1: 좌우
        frame = cv2.flip(frame, 0)
        # image를 Grayscale로 Convert 함
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()