import math as math

import cv2 as cv2


def setLabel(img, pts, label):
    (x, y, w, h) = cv2.boundingRect(pts)
    pt1 = (x, y)
    pt2 = (x + w, y + h)
    cv2.rectangle(img, pt1, pt2, (255, 255, 0), 1)
    cv2.putText(img, label, pt1, cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 255))


def main():
    for i in range(1, 12):
        src = cv2.imread('images/case5/img5_' + str(i) + '.png', cv2.IMREAD_COLOR)
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
        # # 이진화
        # _, img_bin = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        # group threshold
        img_bin = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 49, 5)
        # img_bin = cv2.adaptiveThreshold(img_bin, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 51, 5)
        # morphologyEx
        img_bin = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, None)
        # img_bin = cv2.Canny(gray, 100, 300)  # Canny Edge
        contours, _ = cv2.findContours(img_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        count = 0
        # count when contour is circle
        for pts in contours:
            if cv2.contourArea(pts) < 300:
                continue

            approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True) * 0.02, True)

            vtc = len(approx)

            if vtc == 4:
                setLabel(src, pts, 'RECT')
            else:
                length = cv2.arcLength(pts, True)
                area = cv2.contourArea(pts)
                ratio = 4. * math.pi * area / (length * length)

                if ratio > 0.8:
                    setLabel(src, pts, 'CIR')
                    count += 1

        print(count)
        window_name = 'src' + str(i)
        cv2.imshow(window_name, src)
        cv2.waitKey()
        cv2.destroyAllWindows()

    # cv2.imshow('img_bin', img_bin)
    # cv2.waitKey()
    cv2.destroyAllWindows()


main()
