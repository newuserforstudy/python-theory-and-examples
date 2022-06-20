import cv2
"""
opencv 中的2种背景检测的方法：
createBackgroundSubtractorKNN
cv2.createBackgroundSubtractorMOG2

"""
# Step1. 构造VideoCapture对象
cap = cv2.VideoCapture(f"video/test.avi")

# Step2. 创建一个背景分割器
# createBackgroundSubtractorKNN()函数里，可以指定detectShadows的值
# detectShadows=True，表示检测阴影，反之不检测阴影
# knn = cv2.createBackgroundSubtractorKNN(detectShadows=True)
model = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()  # 读取视频
    # fgmask = knn.apply(frame)  # 背景分割
    fgmask = model.apply(frame)  # 背景分割
    cv2.imshow('frame', fgmask)  # 显示分割结果
    if cv2.waitKey(100) & 0xff == 27:  # 27 Esc
        break

cap.release()
cv2.destroyAllWindows()
