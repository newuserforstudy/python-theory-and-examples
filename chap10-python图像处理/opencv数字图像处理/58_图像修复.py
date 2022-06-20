import cv2

src = cv2.imread("images/5.jpg")
cv2.imshow("watermark image", src)

# 提取划痕
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, (100, 43, 46), (124, 255, 255))
cv2.imshow("mask", mask)


# 修复
se = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
mask = cv2.dilate(mask, se)  # 膨胀
result = cv2.inpaint(src, mask, 3, cv2.INPAINT_TELEA)  # 图像修复
cv2.imshow("result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
