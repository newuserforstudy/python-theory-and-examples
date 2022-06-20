import cv2
import numpy as np

#
# THRESH_BINARY = 0
# THRESH_BINARY_INV = 1
# THRESH_TRUNC = 2
# THRESH_TOZERO = 3
# THRESH_TOZERO_INV = 4
#
src = cv2.imread("images/3.jpg")
cv2.namedWindow("input", cv2.WINDOW_AUTOSIZE)
cv2.imshow("input", src)
h, w = src.shape[:2]

# 自动阈值分割 OTSU/TRIANGLE
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)
print("ret :", ret)
cv2.imshow("binary", binary)

result = np.zeros([h, w * 2, 3], dtype=src.dtype)
result[0:h, 0:w, :] = src
result[0:h, w:2 * w, :] = cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)
cv2.putText(result, "input", (10, 30), cv2.FONT_ITALIC, 1.0, (0, 0, 255), 2)
cv2.putText(result, "binary, threshold = " + str(ret), (w + 10, 30), cv2.FONT_ITALIC, 1.0, (0, 0, 255), 2)
cv2.imshow("result", result)

b = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 25, 10)
cv2.imshow("b", b)

cv2.waitKey(0)
cv2.destroyAllWindows()
