import cv2
import numpy as np

image = cv2.imread("images/3.jpg")

prewitt_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=np.float32)
prewitt_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]], dtype=np.float32)

prewitt_x_grad = cv2.filter2D(image, cv2.CV_16S, prewitt_x)
prewitt_y_grad = cv2.filter2D(image, cv2.CV_16S, prewitt_y)

prewitt_x_grad = cv2.convertScaleAbs(prewitt_x_grad)
prewitt_y_grad = cv2.convertScaleAbs(prewitt_y_grad)

dst = cv2.add(prewitt_x_grad, prewitt_y_grad)
dst = cv2.convertScaleAbs(dst)

cv2.imshow("robert", dst)
cv2.waitKey()
