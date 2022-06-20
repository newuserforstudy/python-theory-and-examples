import cv2
import numpy as np

image1 = cv2.imread("images/1.jpg")
image2 = cv2.imread("images/2.jpg")

cv2.imshow("image1", image1)
cv2.imshow("image2", image2)
cv2.waitKey()

add_image = np.zeros(image1.shape, image1.dtype)
cv2.add(image1, image2, add_image)
cv2.imshow("add image", add_image)
cv2.waitKey()

sub_image = cv2.subtract(image1, image2)
cv2.imshow("sub image", sub_image)
cv2.waitKey()

mul_image = cv2.multiply(image1, image2)
cv2.imshow("mul image", mul_image)
cv2.waitKey()

div_image = cv2.divide(image1, image2)
cv2.imshow("div image", div_image)
cv2.waitKey()
