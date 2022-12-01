import math as math
import cv2 as cv2

# def set_label(img, pts, label):
#     (x, y, w, h) = cv2.boundingRect(pts)
#     pt1 = (x, y)
#     pt2 = (x + w, y + h)
#     cv2.rectangle(img, pt1, pt2, (255, 255, 0), 1)
#     cv2.putText(img, label, pt1, cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 255))

def find_eyes(i):
    file_name = 'images/case3/img3_' + str(i) + '.png'
    src = cv2.imread(file_name, cv2.IMREAD_COLOR)

    if src is None:
        print('Image load failed!')
        return

    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    blur = cv2.blur(gray, (3, 3))
    _, img_bin = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(img_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

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

            if ratio > 0.8:
                circles[count] += 1
                # set_label(src, pts, 'CIR') #test

    circles.sort()
    for j in circles:
        if j != 0:
            print(j)

    cv2.imshow('src' + str(i), src)
    cv2.imshow('img_bin' + str(i), img_bin)
    cv2.waitKey()
    cv2.destroyAllWindows()


def main():
    for i in range(3, 5):
        find_eyes(i)


main()
