import cv2
import numpy as np

image = cv2.imread("images/3.jpg")
cv2.imshow("image", image)

h, w, c = image.shape
cy = h // 2
cx = w // 2

roi = image[cy - 200:cy - 10, cx - 100:cx + 100, :]
cv2.imshow("roi image", roi)
cv2.waitKey()

image2 = cv2.imread("images/3.jpg")
cv2.imshow("image2", image2)
hsv = cv2.cvtColor(image2, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, (30, 30, 30), (200, 200, 200))

cv2.imshow("mask", mask)
cv2.waitKey()

mask = cv2.bitwise_not(mask)
person = cv2.bitwise_and(image2, image2, mask=mask)
cv2.imshow("person",person)
cv2.waitKey()
