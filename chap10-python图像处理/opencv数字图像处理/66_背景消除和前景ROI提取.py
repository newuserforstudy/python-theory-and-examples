import numpy as np
import cv2

cap = cv2.VideoCapture('video/1.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2(
    history=500, varThreshold=100, detectShadows=False)


def process(image, opt=1):
    mask = fgbg.apply(frame)
    line = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 5), (-1, -1))
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, line)
    cv2.imshow("mask", mask)
    # 轮廓提取, 发现最大轮廓
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in range(len(contours)):
        area = cv2.contourArea(contours[c])
        if area < 150:
            continue
        rect = cv2.minAreaRect(contours[c])
        cv2.ellipse(image, rect, (0, 255, 0), 2, 8)
        cv2.circle(image, (np.int32(rect[0][0]), np.int32(rect[0][1])), 2, (255, 0, 0), 2, 8, 0)
    return image, mask


while True:

    ret, frame = cap.read()
    cv2.imshow('input', frame)
    result, m_ = process(frame)
    cv2.imshow('result', result)
    k = cv2.waitKey(50) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
