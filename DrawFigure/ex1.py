import cv2
import numpy as np

# 모두 0으로 되어 있는 빈 캔버스(검정색)
img = np.zeros((512, 512, 3), np.uint8)
# 직선
img = cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)  # (그릴 이미지, 시작좌표, 종료좌표, 색, 선의 두께)
# 사각형
img = cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)  # (그릴 이미지, 시작좌표, 종료좌표, 색, 선의 두께)
# 원
img = cv2.circle(img, (477, 63), 63, (0, 0, 255), -1)  # (그릴 이미지, 중심좌표, 반지름, 색, 선의 두께(-1이면 원 안쪽을 채움)
# 타원
img = cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)  # (그릴 이미지, 중심좌표, 중심에서 큰 거리와 작은 거리,  기울기 각, 시작각도, 종료각도, 타원 색, 선 두께)
# polygon
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)  # 각 꼭지점은 2차원 행렬로 선언
# 이미지에 표현하기 위해 3차원 행렬로 변환. 변환 이전과 이후의 행렬 개수는 동일해야 함
# -1은 원본에 해당하는 값을 그대로 유지
pts = pts.reshape(-1, 1, 2)
img = cv2.polylines(img, [pts], True, (0, 255, 255))  # (그릴 이미지, 연결할 꼭짓점 좌표(array), 닫힌 도형 여부, 색, 선 두께)
# 텍스트 추가
cv2.putText(img, 'OpenCV', (10, 500), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 2) # (그릴 이미지, 표시할 문자열, 문자열이 표시될 위치(왼쪽 아래기준), 폰트, 크기, 색, 선 두께)
cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()