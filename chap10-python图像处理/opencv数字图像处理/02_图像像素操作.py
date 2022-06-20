import cv2
import numpy as np

image = cv2.imread("images/1.jpg")
cv2.namedWindow("ori image", cv2.WINDOW_AUTOSIZE)
cv2.imshow("ori image", image)
cv2.waitKey()

# 1 复制图像
copy_image = np.copy(image)
cv2.imshow("copy image", copy_image)
cv2.waitKey()

copy_image[300:800, 300:800, :] = 255  # 区域像素修改
cv2.imshow("copy image", copy_image)
cv2.waitKey()
