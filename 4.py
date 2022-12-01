import math as math

import cv2 as cv2


def setLabel(img, pts, label):
    (x, y, w, h) = cv2.boundingRect(pts)
    pt1 = (x, y)
    pt2 = (x + w, y + h)
    cv2.rectangle(img, pt1, pt2, (255, 255, 0), 1)
    cv2.putText(img, label, pt1, cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 255))


def find_eyes(i):
    file_name = 'images/case4/img4_' + str(i) + '.png'
    src = cv2.imread(file_name, cv2.IMREAD_COLOR)

    if src is None:
        print('Image load failed!')
        return

    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 13, 3)  # 적응형 이진화
    # # gausian blur
    gray = cv2.GaussianBlur(gray, (1, 1), 3)
    # unsharp mask filter
    gray = cv2.GaussianBlur(gray, (0, 0), 1)
    alpha = 1.0
    gray = cv2.addWeighted(gray, 1 + alpha, gray, -alpha, 0)
    # # bilateralFilter
    gray = cv2.bilateralFilter(gray, -1, 10, 15)
    # morphologyEx
    # gray = cv2.morphologyEx(gray, cv2.MORPH_OPEN, None)
    # gray = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, None)

    img_bin = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 51, 4)  # 적응형 이진화
    contours, _ = cv2.findContours(img_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for pts in contours:
        if cv2.contourArea(pts) < 200:
            continue

        approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True) * 0.2, True)

        vtc = len(approx)

        if vtc == 4:
            setLabel(src, pts, 'RECT')
        else:
            length = cv2.arcLength(pts, True)
            area = cv2.contourArea(pts)
            ratio = 4. * math.pi * area / (length * length)

            if ratio > 0.85:
                setLabel(src, pts, 'CIR')

    cv2.imshow('src' + str(i), src)
    cv2.imshow('img_bin' + str(i), img_bin)
    cv2.waitKey()
    cv2.destroyAllWindows()


def main():
    # for i in range(1, 8):
    #     find_eyes(i)

    find_eyes(7)


main()
