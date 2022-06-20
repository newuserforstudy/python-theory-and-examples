import cv2

# 第一步：使用cv2.VideoCapture读取视频
camera = cv2.VideoCapture(f"video/1.avi")

# 判断视频是否打开
if camera.isOpened():
    print('视频正常 or 摄像头已打开')
else:
    print('视频不正常 or 摄像头未打开')

size = (int(camera.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT)))

fps = camera.get(cv2.CAP_PROP_FPS)
frame_nums = camera.get(cv2.CAP_PROP_FRAME_COUNT)
print('size: ', repr(size))
print("fps: ", fps)
print("frames: ", frame_nums)

# 第二步：cv2.getStructuringElement构造形态学使用的kernel
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))

# 第三步：构造高斯混合模型
model = cv2.createBackgroundSubtractorMOG2()

point_list = []

while True:
    # 第四步：读取视频中的图片，并使用高斯模型进行拟合
    ret, frame = camera.read()
    if ret:
        # 运用高斯模型进行拟合，在两个标准差内设置为0，在两个标准差外设置为255
        fgmk = model.apply(frame)

        # 第五步：使用形态学的开运算做背景的去除
        fgmk = cv2.morphologyEx(fgmk, cv2.MORPH_OPEN, kernel)

        # 第六步：cv2.findContours计算fgmk的轮廓
        """
        cv2.findContours函数参数：
            image：参数是寻找轮廓的图像；
            mode：参数表示轮廓的检索模式，有四种（本文介绍的都是新的cv2接口）：
                cv2.RETR_EXTERNAL：表示只检测外轮廓
                cv2.RETR_LIST：检测的轮廓不建立等级关系
                cv2.RETR_CCOMP：建立两个等级的轮廓，上面的一层为外边界，里面的一层为内孔的边界信息。如果内孔内还有一个连通物体，这个物体的边界也在顶层。
                cv2.RETR_TREE：建立一个等级树结构的轮廓。
            method：轮廓的近似办法：
            cv2.CHAIN_APPROX_NONE：存储所有的轮廓点，相邻的两个点的像素位置差不超过1，即max（abs（x1-x2），abs（y2-y1））==1
            cv2.CHAIN_APPROX_SIMPLE：压缩水平方向，垂直方向，对角线方向的元素，只保留该方向的终点坐标，例如一个矩形轮廓只需4个点来保存轮廓信息
            cv2.CHAIN_APPROX_TC89_L1，CV_CHAIN_APPROX_TC89_KCOS：使用teh-Chinl chain 近似算法

        返回值：

        cv2.findContours()函数返回两个值，一个是轮廓列表contours,，还有一个是每条轮廓对应的属性hierarchy。
        """
        contours, hierarchy = cv2.findContours(fgmk.copy(), cv2.RETR_EXTERNAL,
                                               cv2.CHAIN_APPROX_SIMPLE)  # 该函数计算一幅图像中目标的轮廓

        # print(contours)
        for c in contours:
            if cv2.contourArea(c) < 100:
                continue
            """
            cv2.boundingRect()，参数是一个轮廓点，
            返回四个值，分别是x，y，w，h；
            x，y是矩阵左上点的坐标，w，h是矩阵的宽和高
            """
            (x, y, w, h) = cv2.boundingRect(c)  # 该函数计算矩形的边界框
            point_list.append([x, y, w, h])

            for point in point_list:
                cv2.rectangle(frame, (point[0] + point[2], point[1] + point[3]),
                              (point[0] + point[2], point[1] + point[3]),
                              (0, 0, 255), 3)

        # 第八步：进行图片的展示
        cv2.imshow('fgmk', fgmk)
        cv2.imshow('frame', frame)

        if cv2.waitKey(100) & 0xff == 27:
            break
    else:
        break

camera.release()
cv2.destroyAllWindows()

