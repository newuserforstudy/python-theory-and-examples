import cv2
import numpy as np

cap = cv2.VideoCapture("video/test.avi")

_, frame1 = cap.read()
frame1_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame1)

hsv[..., 1] = 255
# cv2.imshow("hsv", hsv)
# cv2.waitKey()

while True:
    ret, frame2 = cap.read()
    if ret:
        frame2_gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        """
        cv2.calcOpticalFlowFarneback参数
            prev：前一帧的图像
            next：下一帧的图像
            flow：与prevImg大小相同 且类型 为CV_32FC2的计算流图像
            pyrScale ：指定图像比例 (<1) 的参数，以便为每个图像构建金字塔。 pyrScale=0.5 表示经典金字塔，其中下一层比上一层小两倍。
            level:包括初始图像的金字塔层的数量；levels=1表示不创建额外的层，只使用原始图像。
            winsize ：平均窗口大小;较大的值会增加算法对图像噪声的鲁棒性，并可以检测更快速的运动，但会产生更模糊的运动场。
            iterations ：每个金字塔等级上执行迭代算法的迭代次数。用于在每个像素中查找多项式展开的像素邻域
            其余参数中poly_sigma与poly_n有对应关系
            poly_n：较大的值意味着图像将近似于更光滑的表面，产生更稳健的算法和更模糊的运动场，一般取poly_n = 5或7。
            oly_sigma：平滑导数的高斯的标准偏差，用作多项式展开的基础;
            对于poly_n = 5，可以设置poly_sigma = 1.1;对于poly_n = 7，可以设置poly_sigma = 1.5
            flag: 0 OPTFLOW_USE_INITIAL_FLOW; 1 OPTFLOW_FARNEBACK_GAUSSIAN;
        """
        flow = cv2.calcOpticalFlowFarneback(frame1_gray, frame2_gray, None, 0.5, 3, 15, 3, 5, 1.1, 0)
        mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
        hsv[..., 0] = ang * 180 / np.pi / 2
        hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
        bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        cv2.imshow('frame2', bgr)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            cv2.destroyAllWindows()
            break
    else:
        break
