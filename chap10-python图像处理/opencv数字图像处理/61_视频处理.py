import cv2
import numpy as np

capture = cv2.VideoCapture("video/test.mp4")
# capture = cv.VideoCapture(0) 打开摄像头
height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
count = capture.get(cv2.CAP_PROP_FRAME_COUNT)
fps = capture.get(cv2.CAP_PROP_FPS)

print(height, width, count, fps)
out = cv2.VideoWriter("video/re.mp4", cv2.VideoWriter_fourcc('M', 'P', '4', 'V'), 15,
                     (np.int(width), np.int(height)), True)

while True:
    ret, frame = capture.read()
    if ret:
        gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        dst = cv2.Canny(gray_image, 100, 200)
        """
        image： 必须是二值图像，推荐使用canny边缘检测的结果图像； 
        rho: 线段以像素为单位的距离精度，double类型的，推荐用1.0 
        theta： 线段以弧度为单位的角度精度，推荐用numpy.pi/180 
        threshod: 累加平面的阈值参数，int类型，超过设定阈值才被检测出线段，值越大，基本上意味着检出的线段越长，检出的线段个数越少。根据情况推荐先用100试试
        lines：这个参数的意义未知，发现不同的lines对结果没影响，但是不要忽略了它的存在 
        minLineLength：线段以像素为单位的最小长度，根据应用场景设置 
        maxLineGap：同一方向上两条线段判定为一条线段的最大允许间隔（断裂），超过了设定值，则把两条线段当成一条线段，值越大，允许线段上的断裂越大，越有可能检出潜在的直线段
        """
        lines = cv2.HoughLinesP(dst, 1, np.pi / 180, 55, None, 300, 30)
        if lines is not None:
            for i in range(0, len(lines)):
                line = lines[i][0]
                cv2.line(frame, (line[0], line[1]), (line[2], line[3]), (0, 255, 255), 3, cv2.LINE_AA)

        # 显示
        cv2.imshow("line detect", frame)
        out.write(frame)

        c = cv2.waitKey(30)
        if c == 27:
            break
    else:
        break
