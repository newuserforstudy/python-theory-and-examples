import cv2


src = cv2.imread("images/3.jpg")
# src = cv2.resize(src,(800,300),interpolation=cv2.INTER_CUBIC)
cv2.namedWindow("input", cv2.WINDOW_AUTOSIZE)
cv2.imshow("input", src)

# 形态学梯度 - 基本梯度
se = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3), (-1, -1))
basic = cv2.morphologyEx(src, cv2.MORPH_GRADIENT, se)
cv2.imshow("basic gradient", basic)

gray = cv2.cvtColor(basic, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imshow("binary", binary)

se = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 5), (-1, -1))
binary = cv2.morphologyEx(binary, cv2.MORPH_DILATE, se)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for c in range(len(contours)):
    x, y, w, h = cv2.boundingRect(contours[c])
    area = cv2.contourArea(contours[c])
    if area < 200:
        continue
    if h > (3*w) or h < 20:
        continue
    cv2.rectangle(src, (x, y), (x+w, y+h), (0, 0, 255), 1, 8, 0)


cv2.imshow("result", src)
cv2.waitKey(0)
cv2.destroyAllWindows()
