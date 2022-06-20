import cv2
import numpy as np

image = cv2.imread("images/3.jpg")
sharpen_op = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], dtype=np.float32)

src = cv2.filter2D(image, cv2.CV_32F, sharpen_op)
src = cv2.convertScaleAbs(src)

cv2.imshow("sharp operator", src)
cv2.waitKey()
