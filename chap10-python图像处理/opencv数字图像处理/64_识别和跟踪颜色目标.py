import cv2
import numpy as np

capture = cv2.VideoCapture("video/1.mp4")
height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
count = capture.get(cv2.CAP_PROP_FRAME_COUNT)
fps = capture.get(cv2.CAP_PROP_FPS)
print(height, width, count, fps)


def process(image, opt=1):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  # 转为HSV颜色空间
    line = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15), (-1, -1))
    mask = cv2.inRange(hsv, (0, 43, 46), (10, 255, 255))
    cv2.imshow("mask", mask)

    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, line)
    cv2.imshow("masks", mask)

    # 轮廓提取, 发现最大轮廓
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    index = -1
    max = 0
    for c in range(len(contours)):
        area = cv2.contourArea(contours[c])
        if area > max:
            max = area
            index = c
    # 绘制
    if index >= 0:
        rect = cv2.minAreaRect(contours[index])
        print(len(rect))
        print(rect)
        """
        image:它是要在其上绘制椭圆的图像。
        centerCoordinates:它是椭圆的中心坐标。坐标表示为两个值的元组，即(X坐标值，Y坐标值)。
        axesLength:它包含两个变量的元组，分别包含椭圆的长轴和短轴(长轴长度，短轴长度)。
        angle:椭圆旋转角度，以度为单位。
        startAngle:椭圆弧的起始角度，以度为单位。
        endAngle:椭圆弧的终止角度，以度为单位。
        color:它是要绘制的形状边界线的颜色。对于BGR，我们通过一个元组。例如：(255，0，0)为蓝色。
        thickness:是形状边界线的粗细像素。厚度-1像素将用指定的颜色填充形状。
        lineType:这是一个可选参数，它给出了椭圆边界的类型。
        shift:这是一个可选参数。它表示中心坐标中的小数位数和轴的值。
        """

        # cv2.ellipse(image, rect, (150, 50), 360, 0, (0, 0, 255),2,cv2.LINE_8,0)
        cv2.ellipse(image, (256, 256), (150, 50), 360, 0, 360, (0, 255, 0), 2, cv2.LINE_8, 0)
        cv2.circle(image, (np.int32(rect[0][0]), np.int32(rect[0][1])), 2, (255, 0, 0), 2, 8, 0)
    return image


while True:
    ret, frame = capture.read()
    if ret:
        cv2.imshow("video-input", frame)
        result = process(frame)
        cv2.imshow("result", result)
        c = cv2.waitKey(50)
        # print(c)
        if c == 27:  # ESC
            break
    else:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
