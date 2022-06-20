import cv2
import numpy as np

image = cv2.imread("images/3.jpg")

robert_x = np.array([[1, 0], [0, -1]], dtype=np.float32)
robert_y = np.array([[0, -1], [1, 0]], dtype=np.float32)

robert_x_grad = cv2.filter2D(image,cv2.CV_16S,robert_x)
robert_y_grad = cv2.filter2D(image,cv2.CV_16S,robert_y)

robert_x_grad = cv2.convertScaleAbs(robert_x_grad)
robert_y_grad = cv2.convertScaleAbs(robert_y_grad)

dst = cv2.add(robert_x_grad,robert_y_grad)
dst = cv2.convertScaleAbs(dst)

cv2.imshow("robert",dst)
cv2.waitKey()

