
import cv2

cap = cv2.VideoCapture('video/test.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=25, detectShadows=False)

while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    background = fgbg.getBackgroundImage()
    cv2.imshow('input', frame)
    cv2.imshow('mask',fgmask)
    cv2.imshow('background', background)
    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
