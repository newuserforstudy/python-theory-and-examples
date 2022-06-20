import cv2 as cv


src = cv.imread("images/9.jpg")
src = cv.resize(src, (0, 0), fx=0.5, fy=0.5)
cv.imshow("input", src)

hog = cv.HOGDescriptor()
hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())

# Detect people in the image
(rects, weights) = hog.detectMultiScale(src,
                                        winStride=(4, 4),
                                        padding=(8, 8),
                                        scale=1.25,
                                        useMeanshiftGrouping=False)

for (x, y, w, h) in rects:
    cv.rectangle(src, (x, y), (x + w, y + h), (0, 0, 255), 2)

cv.imshow("hog-detector", src)

cv.waitKey(0)
cv.destroyAllWindows()
