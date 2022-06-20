import cv2
import matplotlib.pylab as plt
import matplotlib
matplotlib.use('TkAgg')
image = cv2.imread('images/3.jpg', 0)  # 0表示灰度图

hist = cv2.calcHist([image], [0], None, [256], [0, 256])

plt.plot(hist)
plt.show()

color = ('blue', 'green', 'red')
image1 = cv2.imread('images/3.jpg')  # 彩色图像
for i, color in enumerate(color):
    hist = cv2.calcHist([image1], [i], None, [256], [0, 256])
    plt.plot(hist, color=color)
    plt.xlim([0, 256])

plt.legend(["b-hist", "g-hist", "r-hist"], loc='upper right')
plt.title("b-g-r Hist")
plt.show()
