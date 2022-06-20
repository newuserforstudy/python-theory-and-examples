import cv2
import numpy as np


def canny_demo(image):
    t = 80
    canny_output = cv2.Canny(image, t, t * 2)
    return canny_output


src = cv2.imread("images/3.jpg")
cv2.namedWindow("input", cv2.WINDOW_AUTOSIZE)
cv2.imshow("input", src)
binary = canny_demo(src)
cv2.imshow("binary", binary)

# 概率霍夫曼直线检测
"""
image： 必须是二值图像，推荐使用canny边缘检测的结果图像； 
rho: 线段以像素为单位的距离精度，double类型的，推荐用1.0 
theta： 线段以弧度为单位的角度精度，推荐用numpy.pi/180 
threshod: 累加平面的阈值参数，int类型，超过设定阈值才被检测出线段，值越大，基本上意味着检出的线段越长，检出的线段个数越少。根据情况推荐先用100试试
lines：这个参数的意义未知，发现不同的lines对结果没影响，但是不要忽略了它的存在 
minLineLength：线段以像素为单位的最小长度，根据应用场景设置 
maxLineGap：同一方向上两条线段判定为一条线段的最大允许间隔（断裂），超过了设定值，则把两条线段当成一条线段，值越大，允许线段上的断裂越大，越有可能检出潜在的直线段
"""
linesP = cv2.HoughLinesP(binary, 1, np.pi / 180, 55, None, 50, 10)


if linesP is not None:
    for i in range(0, len(linesP)):
        l = linesP[i][0]
        cv2.line(src, (l[0], l[1]), (l[2], l[3]), (255, 0, 0), 1, cv2.LINE_AA)

# 显示
cv2.imshow("hough line demo", src)
cv2.waitKey(0)
cv2.destroyAllWindows()
