import cv2

src = cv2.imread("images/3.jpg")
cv2.namedWindow("input", cv2.WINDOW_AUTOSIZE)
cv2.imshow("input", src)

# get binary
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

se = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3), (-1, -1))
binary = cv2.morphologyEx(binary, cv2.MORPH_OPEN, se)
cv2.imshow("binary", binary)

# Get contours
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
height, width = src.shape[:2]
for c in range(len(contours)):
    x, y, w, h = cv2.boundingRect(contours[c])
    area = cv2.contourArea(contours[c])
    if h > (height//2):
        continue
    if area < 150:
        continue
    cv2.rectangle(src, (x, y), (x+w, y+h), (0, 0, 255), 1, 8, 0)
    cv2.drawContours(src, contours, c, (0, 255, 0), 2, 8)

cv2.imshow("result", src)
cv2.imwrite("binary2.png", src)

cv2.waitKey(0)
cv2.destroyAllWindows()
