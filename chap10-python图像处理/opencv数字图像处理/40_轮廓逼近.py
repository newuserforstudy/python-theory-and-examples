import cv2
import numpy as np

src = cv2.imread("images/3.jpg")
cv2.namedWindow("input", cv2.WINDOW_AUTOSIZE)
cv2.imshow("input", src)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# 轮廓发现
contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for c in range(len(contours)):
    rect = cv2.minAreaRect(contours[c])
    cx, cy = rect[0]
    result = cv2.approxPolyDP(contours[c], 4, True)
    vertexes = result.shape[0]
    if vertexes == 3:
        cv2.putText(src, "triangle", (np.int32(cx), np.int32(cy)),
                    cv2.FONT_HERSHEY_SIMPLEX, .7, (0, 0, 255), 2, 8)
    if vertexes == 4:
        cv2.putText(src, "rectangle", (np.int32(cx), np.int32(cy)),
                    cv2.FONT_HERSHEY_SIMPLEX, .7, (0, 0, 255), 2, 8)
    if vertexes == 6:
        cv2.putText(src, "poly", (np.int32(cx), np.int32(cy)),
                    cv2.FONT_HERSHEY_SIMPLEX, .7, (0, 0, 255), 2, 8)
    if vertexes > 10:
        cv2.putText(src, "circle", (np.int32(cx), np.int32(cy)),
                    cv2.FONT_HERSHEY_SIMPLEX, .7, (0, 0, 255), 2, 8)


# 显示
cv2.imshow("contours_analysis", src)

cv2.waitKey(0)
cv2.destroyAllWindows()
