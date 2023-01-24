import math as math

import cv2 as cv2


def main():
    src = cv2.imread('images/case4/img4_16.png', cv2.IMREAD_COLOR)

    if src is None:
        print('Image load failed!')
        return

    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    # unsharp mask
    alpha = 0.5
    blur = cv2.GaussianBlur(gray, (0, 0), 5)
    gray = cv2.addWeighted(gray, 1 + alpha, blur, -alpha, 0)
    # adaptive thresholding
    gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 17, 3)
    # bilateral filter
    gray = cv2.bilateralFilter(gray, -3, 19, 5)
    contours, _ = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    count = -1
    circles = []
    for pts in contours:
        if cv2.contourArea(pts) < 100:
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

            if ratio > 0.836:
                circles[count] += 1
    circles.sort()
    for i in circles:
        if i != 0:
            print(i)


main()
