import cv2 as cv2
import numpy as np


def darkness():
    src = cv2.imread('images/sample.jpg', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    # 평균 이미지 픽셀값
    mean_img = np.mean(src, dtype=np.int32)

    # dst에 변경된 픽셀값 저장
    dst = np.empty(src.shape, dtype=src.dtype)

    for y in range(src.shape[0]):
        for x in range(src.shape[1]):
            if src[y, x] < mean_img:
                dst[y, x] = 0
            else:
                dst[y, x] = src[y, x]

    # output.jpg로 저장
    cv2.imwrite('images/output.jpg', dst)
    return


def main():
    darkness()


main()
