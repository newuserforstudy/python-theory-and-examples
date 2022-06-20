import numpy as np
import cv2
cap = cv2.VideoCapture(f"video/1.avi")
_, prevFrame = cap.read()
prevGray = cv2.cvtColor(prevFrame, cv2.COLOR_BGR2GRAY)
prevGray = cv2.GaussianBlur(prevGray, (0, 0), 15)
k = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (0, 0), 15)
    # 两帧法
    diff = cv2.subtract(gray, prevGray)
    t, binary = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    binary = cv2.morphologyEx(binary, cv2.MORPH_OPEN, k)
    cv2.imshow('input', frame)
    cv2.imshow('result', binary)

    c = cv2.waitKey(50) & 0xff
    prevGray = np.copy(gray)
    if c == 27:
        break
cap.release()
cv2.destroyAllWindows()
