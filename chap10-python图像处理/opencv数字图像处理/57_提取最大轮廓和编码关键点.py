import cv2
import numpy as np

src = cv2.imread("images/3.jpg")
cv2.namedWindow("input", cv2.WINDOW_AUTOSIZE)
cv2.imshow("input", src)

# 图像二值化
# src = cv.GaussianBlur(src, (5, 5), 0)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

se = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3), (-1, -1))
binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, se)
cv2.imshow("binary", binary)

# 轮廓提取
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
height, width = src.shape[:2]
index = 0
max = 0
for c in range(len(contours)):
    x, y, w, h = cv2.boundingRect(contours[c])
    if h >=height or w >= width:
        continue
    area = cv2.contourArea(contours[c])
    if area > max:
        max = area
        index = c

print(index)

# 绘制轮廓关键点与轮廓
result = np.zeros(src.shape, dtype=np.uint8)
keypts = cv2.approxPolyDP(contours[index], 4, True)
cv2.drawContours(src, contours, index, (0, 0, 255), 1, 8)
cv2.drawContours(result, contours, index, (0, 0, 255), 1, 8)

for pt in keypts:
    cv2.circle(src, (pt[0][0], pt[0][1]), 2, (0, 255, 0), 2, 8, 0)
    cv2.circle(result, (pt[0][0], pt[0][1]), 2, (0, 255, 0), 2, 8, 0)
cv2.imshow("result", result)
cv2.imshow("output", src)

cv2.waitKey(0)
cv2.destroyAllWindows()