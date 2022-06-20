import cv2

image = cv2.imread("images/1.jpg")
cv2.imshow("ori image", image)
cv2.waitKey()

dst = cv2.applyColorMap(image, cv2.COLORMAP_COOL)

cv2.imshow("enhance image", dst)
cv2.waitKey()

cv2.destroyAllWindows()