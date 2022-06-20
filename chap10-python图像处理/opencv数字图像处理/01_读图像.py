import cv2

# 1 读入一张图像
img_path = "images/1.jpg"
image = cv2.imread(img_path)  # imread 读入图像
print(image.shape)  # 图像尺寸 [h,w,c]
print(image.size)  # 图像的像素点 h*w*c
print(image.dtype) # 数据类型 uint8
# 2 显示图像
cv2.namedWindow("ori img", cv2.WINDOW_AUTOSIZE)
cv2.imshow("ori img", image)
cv2.waitKey(0)

# 3 彩色图像的3个通道：g,b,r
b, g, r = image[:, :, 0], image[:, :, 1], image[:, :, 2]
cv2.imshow("b channel", b)
cv2.imshow("g channel", g)
cv2.imshow("r channel", r)
cv2.waitKey(0)

c1, c2, c3 = cv2.split(image)  # split函数
cv2.imshow("b channel", c1)
cv2.imshow("g channel", c2)
cv2.imshow("r channel", c3)
cv2.waitKey(0)

# 4 合并3个通道
merge_image = cv2.merge([c1, c2, c3])
cv2.imshow("merge image", merge_image)
cv2.waitKey(0)

# 5 灰度图像
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray image", gray_image)
cv2.waitKey()
cv2.destroyAllWindows()
