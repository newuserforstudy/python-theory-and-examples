import cv2

image = cv2.imread("images/1.jpg")
cv2.imshow("image", image)
cv2.waitKey()

# 1 bgr 转为 rgb
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imshow("rgb", rgb_image)
cv2.waitKey()

bgra_image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
cv2.imshow("bgra", bgra_image)
cv2.waitKey()

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("hsv", hsv_image)
cv2.waitKey()

yuv_image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
cv2.imshow("yuv", yuv_image)
cv2.waitKey()

ycrcb_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
cv2.imshow("ycrcb", ycrcb_image)
cv2.waitKey()

