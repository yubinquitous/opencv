import math as math

import cv2 as cv2


def main():
    src = cv2.imread('images/dices.png', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    _, img_bin = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(img_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    count = -1
    circles = []
    for pts in contours:
        if cv2.contourArea(pts) < 400:
            continue

        approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True) * 0.02, True)

        vtc = len(approx)

        if vtc == 4:
            count += 1
            circles.append(0)
        else:
            length = cv2.arcLength(pts, True)
            area = cv2.contourArea(pts)
            ratio = 4. * math.pi * area / (length * length)

            if ratio > 0.8:
                circles[count] += 1

    circles.sort()
    for i in circles:
        if i != 0:
            print(i)


main()
