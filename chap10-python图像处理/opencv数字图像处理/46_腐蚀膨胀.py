import cv2
import numpy as np
"""
膨胀就是求局部最大值的操作。
从数学角度来说，就是将图像与核进行卷积，计算核B覆盖区域的像素点的最大值，
并把这个最大值赋值给参考点指定的元素。这样就会使图像中的高亮区域逐渐增长。
"""
"""
腐蚀和膨胀是相反的操作，腐蚀是求局部最小值的操作。腐蚀操作会使图像中的高亮区逐渐减小。
"""
src = cv2.imread("images/3.jpg")
cv2.namedWindow("input", cv2.WINDOW_AUTOSIZE)
cv2.imshow("input", src)

# 使用3x3结构元素进行膨胀与腐蚀操作
se = np.ones((3, 3), dtype=np.uint8)
dilate = cv2.dilate(src, se, None, (-1, -1), 1)  # 腐蚀
erode = cv2.erode(src, se, None, (-1, -1), 1)  # 膨胀

# 显示
cv2.imshow("dilate", dilate)
cv2.imshow("erode", erode)

cv2.waitKey(0)
cv2.destroyAllWindows()
