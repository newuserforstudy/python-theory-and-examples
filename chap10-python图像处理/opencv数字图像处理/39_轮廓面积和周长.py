import cv2
import numpy as np


def canny_demo(image):
    t = 80
    canny_output = cv2.Canny(image, t, t * 2)
    cv2.imshow("canny_output", canny_output)

    return canny_output


src = cv2.imread("images/3.jpg")
cv2.namedWindow("input", cv2.WINDOW_AUTOSIZE)
cv2.imshow("input", src)

binary = canny_demo(src)
k = np.ones((3, 3), dtype=np.uint8)
binary = cv2.morphologyEx(binary, cv2.MORPH_DILATE, k)

# 轮廓发现
contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for c in range(len(contours)):

    area = cv2.contourArea(contours[c])  # 计算面积
    arclen = cv2.arcLength(contours[c], True)  # 计算弧长， True表示闭合区域
    if area < 100 or arclen < 100:
        continue
    rect = cv2.minAreaRect(contours[c])
    cx, cy = rect[0]
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    cv2.drawContours(src, [box], 0, (0, 0, 255), 2)
    cv2.circle(src, (np.int32(cx), np.int32(cy)), 2, (255, 0, 0), 2, 8, 0)


# 显示
cv2.imshow("contours_analysis", src)
cv2.waitKey(0)
cv2.destroyAllWindows()
