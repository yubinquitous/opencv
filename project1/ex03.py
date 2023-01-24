import cv2 as cv2
import numpy as np


def main():
    cap = cv2.VideoCapture('images/webcam.avi')

    if not cap.isOpened():
        print("Video open failed!")
        exit()

    w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    delay = round(1000 / fps)

    output = cv2.VideoWriter('images/output.avi', fourcc, fps, (w, h))
    if not output.isOpened():
        print('File open failed!')
        exit()

    i = 0
    before_brightness = 0
    reverse_fps = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if reverse_fps > 0:
            output_frame = ~frame
        else:
            if i > 0 and np.abs(before_brightness - np.mean(frame, dtype=np.int32)) > 30:
                output_frame = frame
                reverse_fps = fps * 3
            else:
                output_frame = frame

        output.write(output_frame)

        if cv2.waitKey(delay) == 27:
            break
        i += 1
        before_brightness = np.mean(frame, dtype=np.int32)
        reverse_fps -= 1

    cv2.destroyAllWindows()


main()
