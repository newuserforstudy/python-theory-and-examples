import cv2
import numpy as np


def threshold_demo(image):
    # 去噪声+二值化
    dst = cv2.GaussianBlur(image,(3, 3), 0)
    gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
    ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY)
    cv2.imshow("binary", binary)
    return binary


def canny_demo(image):
    t = 100
    canny_output = cv2.Canny(image, t, t * 2)
    cv2.imshow("canny_output", canny_output)
    return canny_output


src = cv2.imread("images/3.jpg")
cv2.namedWindow("input", cv2.WINDOW_AUTOSIZE)
cv2.imshow("input", src)
binary = threshold_demo(src)
canny = canny_demo(src)

# 轮廓发现
contours, hierarchy = cv2.findContours(canny.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for c in range(len(contours)):
    cv2.drawContours(src, contours, c, (0, 0, 255), 2, 8)

# 显示
cv2.imshow("contours-demo", src)

cv2.waitKey(0)
cv2.destroyAllWindows()
