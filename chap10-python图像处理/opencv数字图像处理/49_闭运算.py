import cv2
"""
闭运算,先膨胀再腐蚀,出区较暗的部分！
"""

src = cv2.imread("images/3.jpg")
cv2.namedWindow("input", cv2.WINDOW_AUTOSIZE)
cv2.imshow("input", src)

# 高斯模糊去噪声
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imshow("binary1", binary)

# MORPH_CLOSE:闭运算,先膨胀再腐蚀
se1 = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 5), (-1, -1))
# se2 = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 25), (-1, -1))
# binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, se1)
binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, se1)

cv2.imshow("binary", binary)

cv2.waitKey(0)
cv2.destroyAllWindows()
