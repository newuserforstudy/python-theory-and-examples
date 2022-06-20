import cv2
import matplotlib.pylab as plt
import matplotlib

matplotlib.use("TKAgg")
src = cv2.imread("images/3.jpg")
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
cv2.namedWindow("input", cv2.WINDOW_AUTOSIZE)
cv2.imshow("input", gray)
dst = cv2.equalizeHist(gray)  # 直方图均衡化
cv2.imshow("eh", dst)
cv2.waitKey()

h1 = cv2.calcHist([src], [0], None, [256], [0, 256])
h2 = cv2.calcHist([dst], [0], None, [256], [0, 256])

plt.plot(h1)
plt.plot(h2)
plt.show()
