import cv2 as cv2
import numpy as np


def saturated(value):
    if value > 255:
        value = 255
    elif value < 0:
        value = 0

    return value


def contrast():
    src = cv2.imread('images/sample.jpg', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    # 평균 이미지 픽셀값
    mean_img = np.mean(src, dtype=np.int32)

    # dst에 변경된 픽셀값 저장
    dst = np.empty(src.shape, dtype=src.dtype)

    alpha = 2.0
    for y in range(src.shape[0]):
        for x in range(src.shape[1]):
            before = src[y, x] + (src[y, x] - mean_img) * alpha
            dst[y, x] = saturated(before)

    cv2.imwrite('images/contrast.jpg', dst)
    return


def main():
    contrast()


main()
