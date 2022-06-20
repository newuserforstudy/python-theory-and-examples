import cv2
import numpy as np

image = cv2.imread("images/3.jpg")
cv2.imshow("image", image)
cv2.waitKey()

dst1 = cv2.flip(image, 0)
cv2.imshow("x-flip", dst1)  # 上下翻转
cv2.waitKey()


dst2 = cv2.flip(image, 1)
cv2.imshow("y-flip", dst2)  # 左右翻转，镜像
cv2.waitKey()

dst3 = cv2.flip(image, -1)
cv2.imshow("z-flip", dst3)  # 中心翻转，旋转180
cv2.waitKey()