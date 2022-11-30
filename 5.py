import math as math
import numpy as np
import cv2 as cv2


def setLabel(img, pts, label):
    (x, y, w, h) = cv2.boundingRect(pts)
    pt1 = (x, y)
    pt2 = (x + w, y + h)
    cv2.rectangle(img, pt1, pt2, (0, 0, 255), 1)
    cv2.putText(img, label, pt1, cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))


def main():
    src = cv2.imread('images/img.png', cv2.IMREAD_COLOR)

    if src is None:
        print('Image load failed!')
        return

    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    _, img_bin = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(img_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    count = 0
    is_max = False
    max_area = 0
    for pts in contours:
        area = cv2.contourArea(pts)
        if area < 50:
            continue

        approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True) * 0.02, True)

        vtc = len(approx)

        print('vtc: ', vtc)
        if vtc == 3:
            continue
        elif vtc == 4:
            if area > max_area:
                max_area = area
                count = 0
                is_max = True
            else:
                is_max = False
        elif is_max:
            length = cv2.arcLength(pts, True)
            area = cv2.contourArea(pts)
            ratio = 4. * math.pi * area / (length * length)

            if ratio > 0.8:
                count += 1

    print('count: ', count)
    cv2.imshow('src', src)
    cv2.waitKey()
    cv2.destroyAllWindows()


main()
