import cv2

src = cv2.imread("images/1.jpg")
cv2.namedWindow("input", cv2.WINDOW_AUTOSIZE)
cv2.imshow("input", src)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (9, 9), 2, 2)
dp = 1
param1 = 100
param2 = 50

circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp, 10, None, param1, param2, 20, 100)
for c in circles[0, :]:
    print(c)
    cx, cy, r = c
    cv2.circle(src, (cx, cy), 2, (0, 255, 0), 2, 8, 0)
    cv2.circle(src, (cx, cy), r, (0, 0, 255), 2, 8, 0)

# show
cv2.imshow("hough circle", src)

cv2.waitKey(0)
cv2.destroyAllWindows()
