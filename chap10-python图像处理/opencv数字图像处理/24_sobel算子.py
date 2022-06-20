import cv2

image = cv2.imread("images/3.jpg")
cv2.namedWindow("ori", cv2.WINDOW_AUTOSIZE)
cv2.imshow("ori", image)
cv2.waitKey()

h, w, c = image.shape
x_grad = cv2.Sobel(image, cv2.CV_32F, 1, 0)  # x方向梯度  32位float
y_grad = cv2.Sobel(image, cv2.CV_32F, 0, 1)  # y方向梯度  32位float

x_grad = cv2.convertScaleAbs(x_grad)  # 转为uint8
y_grad = cv2.convertScaleAbs(y_grad)  # 转为uint8

dst = cv2.add(x_grad, y_grad)
dst = cv2.convertScaleAbs(dst)  # 转为uint8

cv2.imshow("sobel", dst)
cv2.waitKey()
cv2.destroyAllWindows()
