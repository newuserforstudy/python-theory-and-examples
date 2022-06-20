import numpy as np
import cv2

# 调用本地摄像头
cap = cv2.VideoCapture(f"video/test.avi")
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
fgbg = cv2.createBackgroundSubtractorMOG2()

frame1 = np.zeros((np.int(h), np.int(w)))

while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    (cnts, _) = cv2.findContours(fgmask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    maxArea = 0
    for c in cnts:
        Area = cv2.contourArea(c)
        if Area < maxArea:
            (x, y, w, h) = (0, 0, 0, 0)
            continue
        else:
            if Area < 100:
                (x, y, w, h) = (0, 0, 0, 0)
                continue
            else:
                maxArea = Area
                m = c
                (x, y, w, h) = cv2.boundingRect(m)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('frame', frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
