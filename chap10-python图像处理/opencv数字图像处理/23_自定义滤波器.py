import cv2
import numpy as np

src = cv2.imread("images/3.jpg")
cv2.namedWindow("input", cv2.WINDOW_AUTOSIZE)
cv2.imshow("input", src)

blur_op = np.ones([5, 5], dtype=np.float32)/25.
shape_op = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]], np.float32)
grad_op = np.array([[1, 0],[0, -1]], dtype=np.float32)

dst1 = cv2.filter2D(src, -1, blur_op)
dst2 = cv2.filter2D(src, -1, shape_op)
dst3 = cv2.filter2D(src, cv2.CV_32F, grad_op)
dst3 = cv2.convertScaleAbs(dst3)

cv2.imshow("blur=5x5", dst1)
cv2.imshow("shape=3x3", dst2)
cv2.imshow("gradient=2x2", dst3)

cv2.waitKey(0)
cv2.destroyAllWindows()
