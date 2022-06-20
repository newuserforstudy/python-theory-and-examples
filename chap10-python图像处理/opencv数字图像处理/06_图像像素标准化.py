import cv2
import numpy as np

image = cv2.imread("images/1.jpg", 0)  # 灰度图
cv2.imshow("image", image)
cv2.waitKey()

gray_image = np.float32(image)
dst = np.zeros(gray_image.shape, dtype=np.float32)
cv2.normalize(gray_image, dst=dst, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

cv2.imshow("norm minmax", np.uint8(dst*255))
cv2.waitKey()
