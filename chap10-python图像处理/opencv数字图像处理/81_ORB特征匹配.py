import cv2

box = cv2.imread("images/01.png", 0)
box_in_sence = cv2.imread("images/02.png", 0)
cv2.imshow("box", box)
cv2.imshow("box_in_sence", box_in_sence)

# 创建ORB特征检测器
orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(box, None)
kp2, des2 = orb.detectAndCompute(box_in_sence, None)

# 暴力匹配 汉明距离匹配特征点
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)

# 绘制匹配
result = cv2.drawMatches(box, kp1, box_in_sence, kp2, matches, None)
cv2.imshow("orb-match", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
