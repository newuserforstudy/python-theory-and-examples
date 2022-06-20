import cv2
import numpy as np

src = cv2.imread("images/3.jpg")
cv2.namedWindow("input", cv2.WINDOW_AUTOSIZE)
cv2.imshow("input", src)
# sift = cv2.xfeatures2d.SIFT_create()  # 版本问题 3.4.2.16
sift = cv2.SIFT_create()  # 4.4以上

kps = sift.detect(src)
result = cv2.drawKeypoints(src, kps, None, -1, cv2.DrawMatchesFlags_DEFAULT)
cv2.imshow("sift-detector", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

