import cv2

src = cv2.imread("images/03.png")

cv2.imshow("input", src)
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
# Detect people in the image
(rects, weights) = hog.detectMultiScale(src,
                                        winStride=(4, 4),
                                        padding=(8, 8),
                                        scale=1.25,
                                        useMeanshiftGrouping=False)
for (x, y, w, h) in rects:
    cv2.rectangle(src, (x, y), (x + w, y + h), (255, 0, 255), 2)

cv2.imshow("hog-detector", src)
cv2.waitKey(0)
cv2.destroyAllWindows()
