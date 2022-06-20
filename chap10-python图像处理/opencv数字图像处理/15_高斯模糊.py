import cv2
import numpy as np


src = cv2.imread("images/3.jpg")
cv2.namedWindow("input", cv2.WINDOW_AUTOSIZE)
cv2.imshow("input", src)

dst1 = cv2.blur(src, (5, 5))
dst2 = cv2.GaussianBlur(src, (5, 5), sigmaX=15)
dst3 = cv2.GaussianBlur(src, (0, 0), sigmaX=15)

cv2.imshow("blur ksize=5", dst1)  # 均值滤波
cv2.imshow("gaussian ksize=5", dst2)
cv2.imshow("gaussian sigmax=15", dst3)

cv2.waitKey(0)
cv2.destroyAllWindows()
