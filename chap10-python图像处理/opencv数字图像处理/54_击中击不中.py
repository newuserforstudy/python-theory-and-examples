import cv2

"""
击中击不中：B1 B2为不相交结构元素，用B1去腐蚀X，然后用B2去腐蚀X的补集，得到的结果相减！
"""
src = cv2.imread("images/3.jpg")
cv2.namedWindow("input", cv2.WINDOW_AUTOSIZE)
cv2.imshow("input", src)

# Binary image
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

# Hit and Miss
se = cv2.getStructuringElement(cv2.MORPH_CROSS, (12, 12))
binary = cv2.morphologyEx(binary, cv2.MORPH_HITMISS, se)


cv2.imshow("hit miss", binary)

cv2.waitKey(0)
cv2.destroyAllWindows()
