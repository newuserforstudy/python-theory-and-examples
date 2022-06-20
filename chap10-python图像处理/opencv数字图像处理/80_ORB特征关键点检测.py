import cv2

src = cv2.imread("images/8.jpg")
cv2.namedWindow("input", cv2.WINDOW_AUTOSIZE)
cv2.imshow("input", src)

# 创建orb检测器
orb = cv2.ORB_create()
kps = orb.detect(src)

# -1表示随机颜色
result = cv2.drawKeypoints(src, kps, None, -1, cv2.DrawMatchesFlags_DEFAULT)
cv2.imshow("result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
