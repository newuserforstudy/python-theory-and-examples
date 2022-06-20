import cv2
"""
# 顶帽运算：原图像减去开运算结果。
"""

src = cv2.imread("images/3.jpg")
cv2.namedWindow("input", cv2.WINDOW_AUTOSIZE)
cv2.imshow("input", src)

# 高斯模糊去噪声
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# TOPHAT:顶帽操作
se = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3), (-1, -1))
binary = cv2.morphologyEx(binary, cv2.MORPH_TOPHAT, se)


cv2.imshow("binary", binary)

cv2.waitKey(0)
cv2.destroyAllWindows()
