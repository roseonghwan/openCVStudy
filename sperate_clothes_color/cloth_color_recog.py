import numpy as np
import cv2
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
import color_data


def extraction(x):
    image = cv2.resize(x, dsize=(500, 500), interpolation=cv2.INTER_AREA)
    mask = np.zeros(image.shape[:2], np.uint8)
    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)
    rect = (10, 10, x.shape[0] - 10, x.shape[1] - 10)
    cv2.grabCut(image, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    # arr_y = []
    # arr_x = []
    # for i in range(500):
    #     for j in range(500):
    #         if mask2[i][j] == 1:
    #             arr_y.append(i)
    #             arr_x.append(j)
    image *= mask2[:, :, np.newaxis]
    # image = image[min(arr_y):max(arr_y),min(arr_x):max(arr_x)]
    return image


def centroid_histogram(clt):
    # grab the number of different clusters and create a histogram
    # based on the number of pixels assigned to each cluster
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)
    # normalize the histogram, such that it sums to one
    hist = hist.astype("float")
    hist /= hist.sum()
    # return the histogram
    return hist


def plot_colors(hist, centroids):
    # initialize the bar chart representing the relative frequency
    # of each of the colors
    # loop over the percentage of each cluster and the color of
    # each cluster
    percent_list = []
    color_list = []
    # 배경은 퍼센트 부분에 포함x
    for (percent, color) in zip(hist, centroids):
        # plot the relative percentage of each cluster
        if int(color.astype("uint8").tolist()[0]) == int(color.astype("uint8").tolist()[1]) == int(
                color.astype("uint8").tolist()[2]) == 0:
            pass
        else:
            percent_list.append(percent)
    bar = np.zeros((50, int(300 * (sum(percent_list))), 3), dtype="uint8")
    startX = 0

    # histogram에서 배경색 제외
    for (percent, color) in zip(hist, centroids):
        # plot the relative percentage of each cluster
        endX = startX + (percent * 300)
        if int(color.astype("uint8").tolist()[0]) == int(color.astype("uint8").tolist()[1]) == int(
                color.astype("uint8").tolist()[2]) == 0:
            pass
        else:
            cv2.rectangle(bar, (int(startX), 0), (int(endX), 50), color.astype("uint8").tolist(), -1)
            startX = endX
            color_list.append(color)

    # return the bar chart
    return bar, percent_list, color_list


def image_color_cluster(image, k=8):
    # image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = image.reshape((image.shape[0] * image.shape[1], 3))
    clt = KMeans(n_clusters=k)
    clt.fit(image)
    hist = centroid_histogram(clt)
    bar, p_list, c_list = plot_colors(hist, clt.cluster_centers_)
    print(p_list)
    print(c_list)
    plt.figure()
    plt.axis("off")
    plt.imshow(bar)
    plt.show()
    return c_list, p_list


if __name__ == '__main__':
    picture = cv2.imread('orange.png')
    img = extraction(picture)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    rgb_list, percent_list = image_color_cluster(img)
    color_list = color_data.extract_color(rgb_list)
    priority_color = color_list[percent_list.index(max(percent_list))]
    print("====", priority_color, "====")
