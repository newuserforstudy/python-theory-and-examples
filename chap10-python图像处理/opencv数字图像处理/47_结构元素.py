import cv2
"""
结构元素：
二维结构元素可以理解成一个二维矩阵，矩阵元素的值为0或者1；通常结构元素要小于待处理的图像。
"""

src = cv2.imread("images/3.jpg")
cv2.namedWindow("input", cv2.WINDOW_AUTOSIZE)

# 二值化图像
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imshow("input", binary)

# 使用3x3结构元素进行膨胀与腐蚀操作
se = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3), (-1, -1))
print(se)
dilate = cv2.dilate(binary, se, None, (-1, -1), 1)
erode = cv2.erode(binary, se, None, (-1, -1), 1)

# 显示
cv2.imshow("dilate", dilate)
cv2.imshow("erode", erode)

cv2.waitKey(0)
cv2.destroyAllWindows()