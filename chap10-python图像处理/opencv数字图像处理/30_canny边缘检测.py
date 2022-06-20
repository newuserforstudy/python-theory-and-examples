import cv2
import numpy as np

image = cv2.imread("images/3.jpg")

edge = cv2.Canny(image,100,200)
cv2.imshow("canny",edge)
cv2.waitKey()

edge_src = cv2.bitwise_and(image,image,mask=edge)
cv2.imshow("edge image",edge_src)
cv2.waitKey()