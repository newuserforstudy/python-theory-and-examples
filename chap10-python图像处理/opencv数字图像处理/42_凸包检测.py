import cv2
import numpy as np

src = cv2.imread("images/3.jpg")
cv2.namedWindow("input", cv2.WINDOW_AUTOSIZE)
cv2.imshow("input", src)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
k = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

# 开运算去除外部噪点
binary = cv2.morphologyEx(binary, cv2.MORPH_OPEN, k)
cv2.imshow("binary", binary)

# 轮廓发现
contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))
for c in range(len(contours)):
    ret = cv2.isContourConvex(contours[c])
    points = cv2.convexHull(contours[c])

    total = len(points)
    print(total)
    for i in range(len(points)):
        x1, y1 = points[i][0]
        x2, y2 = points[(i+1)%total][0]
        cv2.circle(src, (x1, y1), 4, (255, 0, 0), 2, 8, 0)
        cv2.line(src, (x1, y1), (x2, y2), (0, 0, 255), 2, 8, 0)
    print(points)
    print("convex : ", ret)


# 显示
cv2.imshow("contours_analysis", src)
cv2.waitKey(0)
cv2.destroyAllWindows()
