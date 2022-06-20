import cv2
"""
开运算：先腐蚀再膨胀,除去较亮的部分。
"""

src = cv2.imread("images/3.jpg")
cv2.namedWindow("input", cv2.WINDOW_AUTOSIZE)
cv2.imshow("input", src)

# 高斯模糊去噪声
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
dst = cv2.GaussianBlur(gray, (9, 9), 2, 2)
binary_1 = cv2.adaptiveThreshold(dst, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                 cv2.THRESH_BINARY_INV, 45, 15)

# MORPH_OPEN：开操作,先腐蚀再膨胀
se = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5), (-1, -1))
binary = cv2.morphologyEx(binary_1, cv2.MORPH_OPEN, se)

cv2.imshow("binary", binary)

cv2.waitKey(0)
cv2.destroyAllWindows()
