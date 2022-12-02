import math as math

import cv2 as cv2


def main():
    src = cv2.imread('images/case5/img5_1.png', cv2.IMREAD_COLOR)
    if src is None:
        print('Image load failed!')
        return

    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    # unsharp mask filtering
    blurred = cv2.GaussianBlur(gray, (0, 0), 3)
    alpha = 9.0
    gray = cv2.addWeighted(gray, 1 + alpha, blurred, -alpha, 0)
    # 양방향 필터
    gray = cv2.bilateralFilter(gray, -1, 10, 15)
    # adaptive threshold
    img_bin = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 49, 5)
    # morphologyEx
    img_bin = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, None)
    contours, _ = cv2.findContours(img_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    count = 0
    # count when contour is circle
    for pts in contours:
        if cv2.contourArea(pts) < 300:
            continue

        approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True) * 0.02, True)

        vtc = len(approx)

        if vtc == 4:
            continue
        else:
            length = cv2.arcLength(pts, True)
            area = cv2.contourArea(pts)
            ratio = 4. * math.pi * area / (length * length)

            if ratio > 0.8:
                count += 1

    print(count)


main()
