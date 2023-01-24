import math as math

import cv2 as cv2


def find_eye(i):
    file_name = 'images/dice' + str(i) + '.png'
    src = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    _, img_bin = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(img_bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

    count = 0
    for pts in contours:
        if cv2.contourArea(pts) < 400:
            continue

        approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True) * 0.02, True)

        vtc = len(approx)

        if vtc != 3 and vtc != 4:
            length = cv2.arcLength(pts, True)
            area = cv2.contourArea(pts)
            ratio = 4. * math.pi * area / (length * length)

            if ratio > 0.75:
                count += 1

    print(count)


def main():
    print('=======dice1=======')
    find_eye(1)
    print('=======dice5=======')
    find_eye(5)
    print('=======dice7=======')
    find_eye(7)
    print('=======dice9=======')
    find_eye(9)


main()
