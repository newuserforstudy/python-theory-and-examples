# cv2.calcOpticalFlowPyrLK
"""
prevImg ：buildOpticalFlowPyramid构造的第一个8位输入图像或金字塔。
nextImg ：与prevImg相同大小和相同类型的第二个输入图像或金字塔
prevPts ：需要找到流的2D点的矢量(vector of 2D points for which the flow needs to be found;);点坐标必须是单精度浮点数。
nextPts ：输出二维点的矢量（具有单精度浮点坐标），包含第二图像中输入特征的计算新位置;当传递OPTFLOW_USE_INITIAL_FLOW标志时，向量必须与输入中的大小相同。
status ：输出状态向量（无符号字符）;如果找到相应特征的流，则向量的每个元素设置为1，否则设置为0。
err ：输出错误的矢量; 向量的每个元素都设置为相应特征的错误，错误度量的类型可以在flags参数中设置; 如果未找到流，则未定义错误（使用status参数查找此类情况）。
winSize ：每个金字塔等级的搜索窗口的winSize大小。
maxLevel ：基于0的最大金字塔等级数;如果设置为0，则不使用金字塔（单级），如果设置为1，则使用两个级别，依此类推;如果将金字塔传递给输入，那么算法将使用与金字塔一样多的级别，但不超过maxLevel。
criteria ：参数，指定迭代搜索算法的终止条件（在指定的最大迭代次数criteria.maxCount之后或当搜索窗口移动小于criteria.epsilon时）。
flags ：操作标志：
OPTFLOW_USE_INITIAL_FLOW使用初始估计，存储在nextPts中;如果未设置标志，则将prevPts复制到nextPts并将其视为初始估计。
OPTFLOW_LK_GET_MIN_EIGENVALS使用最小特征值作为误差测量（参见minEigThreshold描述）;如果没有设置标志，则将原稿周围的色块和移动点之间的L1距离除以窗口中的像素数，用作误差测量。
minEigThreshold ：算法计算光流方程的2x2正常矩阵的最小特征值，除以窗口中的像素数;如果此值小于minEigThreshold，则过滤掉相应的功能并且不处理其流程，因此它允许删除坏点并获得性能提升。
"""

import numpy as np
import cv2

cap = cv2.VideoCapture('video/test.avi')

# 角点检测所需参数
feature_params = dict(maxCorners=100,
                      qualityLevel=0.3,
                      minDistance=7)

# lucas kanade参数
lk_params = dict(winSize=(15, 15),
                 maxLevel=2)  # 窗口大小为15*15，金字塔层数为2

# 随机颜色条
color = np.random.randint(0, 255, (100, 3))

# 拿到第一帧图像
ret, old_frame = cap.read()
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
# 返回所有检测特征点，需要输入图像，角点最大数量（效率），品质因子（特征值越大的越好，来筛选）
# 距离相当于这区间有比这个角点强的，就不要这个弱的了
p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)  # 寻找角点

# 创建一个mask
mask = np.zeros_like(old_frame)

while True:
    ret, frame = cap.read()  # 这个是取的第二帧图像，上面已经取出了第一帧图像
    if ret:
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 需要传入前一帧和当前图像以及前一帧检测到的角点
        p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)

        # st=1表示
        good_new = p1[st == 1]
        print(p1.shape)  # (n,1,2)
        print(good_new.shape)  # (n, 2)
        good_old = p0[st == 1]

        # 绘制轨迹
        for i, (new, old) in enumerate(zip(good_new, good_old)):
            # new=[692.99805  83.00432]
            a, b = new.ravel()  # 或者[a, b] = new
            c, d = old.ravel()
            mask = cv2.line(mask, (a, b), (c, d), color[i].tolist(), 2)
            # python tolist()方法，将数组或者矩阵转换成列表
            frame = cv2.circle(frame, (a, b), 5, color[i].tolist(), -1)

        img = cv2.add(frame, mask)  # 这个相加不会超出边界

        cv2.imshow('frame', img)
        k = cv2.waitKey(50) & 0xff
        if k == 27:
            break
        # 更新
        old_gray = frame_gray.copy()
        p0 = good_new.reshape(-1, 1, 2)
    else:
        break
cv2.destroyAllWindows()
cap.release()
