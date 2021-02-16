import cv2
from imutils.video import WebcamVideoStream, FileVideoStream
from imutils.video import FPS
class ImageProcessor(object):
    def __init__(self):
        # 아래 두 개의 모듈은 소스로 부터 영상을 쓰레드를 이용해 받아와. 이렇게 쓰레드로 영상을 받아오면 좋은점은
        # 쓰레드를 통해 영상이 최신의 상태를 유지할 수 있어
        # 웹캠 라이브영상으로 영상처리
        # 파이참의 경우 command 키를 누른 상태로 모듈을 클릭하면 어떻게 구현되어있는지 알 수 있어
        self.cam = WebcamVideoStream(src=0).start()
        ## 녹화된 영상을 가지고 영상처리
        # self.cam = FileVideoStream(src= "VIDEO FILE PATH").start()
        # 알고리즘의 초당 프레임 처리 효율을 확인하기 위한 모듈
        self.fps = FPS()

    def get_image(self):
     # python openCV 에서 이미지는 numpy 배열 타입이기 때문에 이미지에 대해 numpy 모듈을 사용할 수 있어
     # self.cam.read() 는 이미지를 반환하는데 우리가 opencv 로 부터 받아와 변수에 저장하는 이미지는 실제로는 포인터야
     # 포인터이기 때문에 우리가 그 이미지를 가지고 영상처리를 하게되면 원본을 건드리는거야
     # 원본을 거드리지 않고 영상처리를 해주기위해서 Numpy의 Copy모듈을 이용해서 깊은 복사를 해 줘야해
        return self.cam.read().copy()

    ## 예시 ##
    # Canny Edge 알고리즘 #
    def canny(self, visualization=False):
        from imutils import auto_canny
     # 보통은 영상처리전 원본이미지를 src(source), 목표로 하는 영상처리 결과이미지를 dst(destination)라고 네이밍해
        src = self.get_image()
        dst = auto_canny(src)
        if visualization:
            cv2.imshow("Canny", dst)
            cv2.waitKey(1)
        return dst

 # Gaussian 필터링 #
    def gaussian_filtering(self, visualization=False):
        src = self.get_image()
        dst = cv2.GaussianBlur(src, ksize=(5, 5), sigmaX=0.1)
        if visualization:
            cv2.imshow("Gaussian", dst)
            cv2.waitKey(1)
        return dst

if __name__ == "__main__":
     imageProcessor = ImageProcessor()
     imageProcessor.fps.start()
     while imageProcessor.fps._numFrames < 200 : # fps 테스트 모드 , 200회를 테스트해본다는 의미야.
         ############ 테스트 알고리즘 적용 ############
         #_ = imageProcessor.get_image()
         _ = imageProcessor.gaussian_filtering(visualization=True)
         _ = imageProcessor.canny(visualization=True)
         imageProcessor.fps.update()
         ########################################
     imageProcessor.fps.stop()
     print("[INFO] time : " + str(imageProcessor.fps.elapsed())) # 테스트가 끝나면 총 걸린 시간을 확인해볼 수 있어
     print("[INFO] FPS : " + str(imageProcessor.fps.fps())) # 테스트가 끝나면 FPS가 얼마나 되는지 확인해볼 수 있어