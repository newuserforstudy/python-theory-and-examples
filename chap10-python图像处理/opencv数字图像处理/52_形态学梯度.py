import cv2

src = cv2.imread("images/3.jpg", 0)
cv2.namedWindow("input", cv2.WINDOW_AUTOSIZE)
cv2.imshow("input", src)

# 形态学梯度 - 基本梯度
se = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5), (-1, -1))
basic = cv2.morphologyEx(src, cv2.MORPH_GRADIENT, se)
cv2.imshow("basic gradient", basic)

# 外梯度
dilate = cv2.morphologyEx(src, cv2.MORPH_DILATE, se)
exteral = cv2.subtract(dilate, src)
cv2.imshow("external gradient", exteral)

# 内梯度
erode = cv2.morphologyEx(src, cv2.MORPH_ERODE, se)
interal = cv2.subtract(src, erode)
cv2.imshow("interal gradient", interal)

cv2.imwrite("gradient.png", basic)
cv2.waitKey(0)
cv2.destroyAllWindows()
