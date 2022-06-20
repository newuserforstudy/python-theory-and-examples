import cv2 as cv
import numpy as np

cap = cv.VideoCapture('video/001.mp4')

# 读取第一帧
ret, frame = cap.read()
cv.namedWindow("Demo", cv.WINDOW_AUTOSIZE)

# 选择ROI区域
"""
Select a ROI and then press SPACE or ENTER button!
Cancel the selection process by pressing c button!
"""
x, y, w, h = cv.selectROI("Demo", frame, True, False)  # 按 空格键space or 确认键Enter 结束！
track_window = (x, y, w, h)

# 获取ROI直方图
roi = frame[y:y + h, x:x + w]
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv_roi, (26, 43, 46), (34, 255, 255))
roi_hist = cv.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX)

# 设置搜索跟踪分析
term_crit = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)
tracking_path = []
while True:
    ret, frame = cap.read()
    if ret is False:
        break
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    dst = cv.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

    # ，搜索更新roi区域， 保持运行轨迹
    ret, track_box = cv.CamShift(dst, track_window, term_crit)
    track_window = track_box

    # 椭圆中心
    pt = np.int32(ret[0])
    if pt[0] > 0 and pt[1] > 0:
        tracking_path.append(pt)

    # 绘制跟踪对象位置窗口与对象运行轨迹
    # cv.ellipse(frame, ret, (0, 0, 255), 3, 8)
    for i in range(1, len(tracking_path)):
        cv.line(frame, (tracking_path[i - 1][0], tracking_path[i - 1][1]),
                (tracking_path[i][0], tracking_path[i][1]), (0, 255, 0), 2, 6, 0)

    cv.imshow('Demo', frame)
    k = cv.waitKey(150) & 0xff
    if k == 27:
        break

cv.destroyAllWindows()
cap.release()
