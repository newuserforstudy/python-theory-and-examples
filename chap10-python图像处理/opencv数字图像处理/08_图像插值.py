import cv2
import numpy as np

image = cv2.imread("images/3.jpg")
cv2.imshow("image", image)
cv2.waitKey()

h, w, c = image.shape
print(h, w)

# 1 最近邻插值
dst1 = cv2.resize(image, (w * 2, h * 2), fx=0.75, fy=0.75, interpolation=cv2.INTER_NEAREST)
print(dst1.shape)
cv2.imshow("INTER_NEAREST", dst1)
cv2.waitKey()

# 2 双线性插值
dst2 = cv2.resize(image, (w * 2, h * 2), fx=0.75, fy=0.75, interpolation=cv2.INTER_LINEAR)
print(dst2.shape)
cv2.imshow("INTER_LINEAR", dst2)
cv2.waitKey()

# 3 双三次插值 4x4
dst3 = cv2.resize(image, (w * 2, h * 2), fx=0.75, fy=0.75, interpolation=cv2.INTER_CUBIC)
print(dst3.shape)
cv2.imshow("INTER_CUBIC", dst3)
cv2.waitKey()

# 4 LANCZOS插值 8x8
dst4 = cv2.resize(image, (w * 2, h * 2), fx=0.75, fy=0.75, interpolation=cv2.INTER_LANCZOS4)
print(dst4.shape)
cv2.imshow("INTER_LANCZOS4", dst4)
cv2.waitKey()

# 5 区域重采样
dst5 = cv2.resize(image, (w * 2, h * 2), fx=0.75, fy=0.75, interpolation=cv2.INTER_AREA)
print(dst4.shape)
cv2.imshow("INTER_INTER_AREA", dst5)
cv2.waitKey()
