import cv2
"""
方向梯度直方图
"""

src = cv2.imread("images/3.jpg")
print(src.shape)
hog = cv2.HOGDescriptor()
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
fv = hog.compute(gray, winStride=(8, 8), padding=(0, 0))
print(len(fv))
print(fv[0])
# cv2.namedWindow('hog-descriptor', cv2.WINDOW_NORMAL)
cv2.imshow("hog-descriptor", src)
cv2.waitKey(0)
cv2.destroyAllWindows()
