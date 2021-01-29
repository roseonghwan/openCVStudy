import cv2
cap = cv2.VideoCapture(0)
# 영상을 저장하기 위해서는 cv2.VideoWriter object를 생성해야 함
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('images/output.avi', fourcc, 25.0, (640, 480)) # (저장될 파일명, codec 정보, 초당 저장될 frame, 저장될 size)

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        # 이미지 반전, 0:상하, 1:좌우
        frame = cv2.flip(frame, 0)
        out.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(0) & 0xFF == ord('q'):
            break
        else:
            break
cap.release()
out.release()
cv2.destroyAllWindows()