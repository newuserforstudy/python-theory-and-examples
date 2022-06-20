import cv2

image = cv2.imread("images/3.jpg")
dst1 = cv2.medianBlur(image, ksize=3)
dst2 = cv2.medianBlur(image, ksize=5)
dst3 = cv2.medianBlur(image, ksize=9)

cv2.imshow("image", image)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)
cv2.imshow("dst3", dst3)
cv2.waitKey()
