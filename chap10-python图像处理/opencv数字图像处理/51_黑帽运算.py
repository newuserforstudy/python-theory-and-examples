# 黑帽运算(img) = 闭运算图像(img) - 原始图像(img)
import cv2

src = cv2.imread("images/3.jpg")
cv2.namedWindow("input", cv2.WINDOW_AUTOSIZE)
cv2.imshow("input", src)

# 图像二值化
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# BLACKHAT:黑帽操作
se = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9), (-1, -1))
binary = cv2.morphologyEx(binary, cv2.MORPH_BLACKHAT, se)


cv2.imshow("black hat", binary)

cv2.waitKey(0)
cv2.destroyAllWindows()
