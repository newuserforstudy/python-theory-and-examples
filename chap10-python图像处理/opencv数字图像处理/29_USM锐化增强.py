import cv2
import numpy as np

image = cv2.imread("images/3.jpg")

blur_image = cv2.GaussianBlur(image, (0, 0), 5)
usm = cv2.addWeighted(image, 1.5, blur_image, -0.5, 0)

cv2.imshow("usm", usm)
cv2.waitKey()
