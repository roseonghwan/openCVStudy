import cv2
import numpy as np


# 흑백 이미지로 변화
def grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


# Canny 알고리즘
def canny(img, low_threshold, high_threshold):
    return cv2.Canny(img, low_threshold, high_threshold)


# 가우시안 필터
def gaussian_blur(img, kernel_size):
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)


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

    # vertices에 정한 점들로 이뤄진 다각형 부분
    cv2.fillPoly(mask, vertices, mask_color)

    # 본 이미지와 mask를 합침
    ROI_image = cv2.bitwise_and(img, mask)

    return ROI_image


# 선 그리기
def draw_line(img, lines):
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(img, (x1, y1), (x2, y2), [0, 0, 255], 2)


# 허프 변환
def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):
    # lines에 차선의 시작점과 끝점의 좌표들이 저장되어 있음
    lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]), minLineLength=min_line_len,
                            maxLineGap=max_line_gap)
    # 빈 이미지로 만듦
    line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    # 빈 이미지에 선을 그림
    draw_line(line_img, lines)

    return line_img


# 두 이미지 overlap
def weight_img(img, initial_img, a=1, b=1., c=0.):
    # result = imgA * a + imgB * b + c
    # 가중치가 높은 이미지가 선명해짐
    return cv2.addWeighted(initial_img, a, img, b, c)


if __name__ == '__main__':
    #image = cv2.imread('road.png')  # 이미지 읽기
    cap = cv2.VideoCapture('lineTracing.mp4')
    while cap.isOpened():
        ret, image = cap.read()

        height, width = image.shape[:2]  # 이미지 높이, 너비

        gray_img = grayscale(image)  # 흑백이미지로 변환

        blur_img = gaussian_blur(gray_img, 3)  # Blur 효과

        canny_img = canny(blur_img, 70, 210)  # Canny edge 알고리즘

        # 사다리꼴 모양
        vertices = np.array(
            [[(50, height), (width / 2 - 45, height / 2 + 60), (width / 2 + 45, height / 2 + 60), (width - 50, height)]],
            dtype=np.int32)
        # ROI 설정
        ROI_img = region_of_interest(canny_img, vertices)

        # 허프 변환
        hough_img = hough_lines(ROI_img, 1, np.pi / 180, 30, 10, 20)

        # 원본 이미지에 검출된 선 overlap
        result = weight_img(hough_img, image)

        cv2.imshow('result', result)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # Release
    cap.release()
    cv2.destroyAllWindows()
    '''
    cv2.imshow('result', result)
    cv2.waitKey(0)'''
