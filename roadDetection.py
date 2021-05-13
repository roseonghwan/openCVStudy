<<<<<<< HEAD
import numpy as np
import cv2


# ROI 세팅
def region_of_interest(img, vertices):
    # mask -> img와 같은 크기의 빈 이미지
    mask = np.zeros_like(img)
    # 컬러 이미지
    if len(img.shape) > 2:
        channel_cnt = img.shape[2]
        mask_color = (255,) * channel_cnt
    # 흑백 이미지
    else:
        mask_color = 255

    # vertices에 정한 점들로 이뤄진 다각형부분을 mask_color로 채움
    cv2.fillPoly(mask, vertices, mask_color)

    # 이미지와 mask_color로 채워진 ROI를 합침
    ROI_img = cv2.bitwise_and(img, mask)
    return ROI_img


def mark_img(img):
    # BGR 제한 값 설정
    bgr_threshold = [200, 200, 200]

    # BGR 제한 값보다 작으면 검은색으로
    thresholds = (img[:, :, 0] < bgr_threshold[0]) | (img[:, :, 1] < bgr_threshold[1]) | (img[:, :, 2] < bgr_threshold[2])
    img[thresholds] = [0, 0, 0]
    return img


if __name__ == '__main__':
    # image = cv2.imread("road.png")
    cap = cv2.VideoCapture("lineTracing.mp4")

    while cap.isOpened():
        ret, image = cap.read()
        height, width = image.shape[:2]

        height, width = image.shape[:2]
        # 사다리꼴 모형의 Points
        # 왼쪽 아래부터 시계방향으로
        vertices = np.array(
            [[(50, height), (width / 2 - 45, height / 2 + 60), (width / 2 + 45, height / 2 + 60),
              (width - 50, height)]],
            dtype=np.int32)
        # 이미지 복사
        copy = np.copy(image)
        # 원하는 영역 추출
        roi = region_of_interest(copy, vertices)
        # 흰색 부분 찾기
        white = mark_img(copy)
        # 원하는 부분에서 흰색 영역 추출
        result = mark_img(roi)
        # 본 이미지에 차선을 빨간색으로 결과물 덮어씌우기
        color_threshold = (result[:, :, 0] > 200) & (result[:, :, 1] > 200) & (result[:, :, 2] > 200)
        image[color_threshold] = [0, 0, 255]

        cv2.imshow('result', image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # Release
    cap.release()
    cv2.destroyAllWindows()

    '''
    cv2.imshow("white", white)
    cv2.imshow("roi", roi)
    cv2.imshow("result", result)
    cv2.imshow("final", image)
    '''
=======
import numpy as np
import cv2


# ROI 세팅
def region_of_interest(img, vertices):
    # mask -> img와 같은 크기의 빈 이미지
    mask = np.zeros_like(img)
    # 컬러 이미지
    if len(img.shape) > 2:
        channel_cnt = img.shape[2]
        mask_color = (255,) * channel_cnt
    # 흑백 이미지
    else:
        mask_color = 255

    # vertices에 정한 점들로 이뤄진 다각형부분을 mask_color로 채움
    cv2.fillPoly(mask, vertices, mask_color)

    # 이미지와 mask_color로 채워진 ROI를 합침
    ROI_img = cv2.bitwise_and(img, mask)
    return ROI_img


def mark_img(img):
    # BGR 제한 값 설정
    bgr_threshold = [200, 200, 200]

    # BGR 제한 값보다 작으면 검은색으로
    thresholds = (img[:, :, 0] < bgr_threshold[0]) | (img[:, :, 1] < bgr_threshold[1]) | (img[:, :, 2] < bgr_threshold[2])
    img[thresholds] = [0, 0, 0]
    return img


if __name__ == '__main__':
    # image = cv2.imread("road.png")
    cap = cv2.VideoCapture("lineTracing.mp4")

    while cap.isOpened():
        ret, image = cap.read()
        height, width = image.shape[:2]

        height, width = image.shape[:2]
        # 사다리꼴 모형의 Points
        # 왼쪽 아래부터 시계방향으로
        vertices = np.array(
            [[(50, height), (width / 2 - 45, height / 2 + 60), (width / 2 + 45, height / 2 + 60),
              (width - 50, height)]],
            dtype=np.int32)
        # 이미지 복사
        copy = np.copy(image)
        # 원하는 영역 추출
        roi = region_of_interest(copy, vertices)
        # 흰색 부분 찾기
        white = mark_img(copy)
        # 원하는 부분에서 흰색 영역 추출
        result = mark_img(roi)
        # 본 이미지에 차선을 빨간색으로 결과물 덮어씌우기
        color_threshold = (result[:, :, 0] > 200) & (result[:, :, 1] > 200) & (result[:, :, 2] > 200)
        image[color_threshold] = [0, 0, 255]

        cv2.imshow('result', image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # Release
    cap.release()
    cv2.destroyAllWindows()

    '''
    cv2.imshow("white", white)
    cv2.imshow("roi", roi)
    cv2.imshow("result", result)
    cv2.imshow("final", image)
    '''
>>>>>>> 50ba5fb860587880913a1b25544fc3e9e62e9d9d
