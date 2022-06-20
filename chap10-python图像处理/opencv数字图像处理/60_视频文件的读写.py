import cv2
import numpy as np


capture = cv2.VideoCapture("video/test.mp4")
# capture = cv.VideoCapture(0) 打开摄像头
height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
count = capture.get(cv2.CAP_PROP_FRAME_COUNT)
fps = capture.get(cv2.CAP_PROP_FPS)
print(height, width, count, fps)
"""
cv2.VideoWriter_fourcc('M', 'P', '4', 'V')  MPEG-4编码 .mp4 可指定结果视频的大小
cv2.VideoWriter_fourcc('X','2','6','4')     MPEG-4编码 .mp4 可指定结果视频的大小
cv2.VideoWriter_fourcc('I', '4', '2', '0')  YUV编码类型，文件名后缀为.avi 广泛兼容，但会产生大文件
cv2.VideoWriter_fourcc('P', 'I', 'M', 'I')  MPEG-1编码类型，文件名后缀为.avi
cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')  MPEG-4编码类型，文件名后缀为.avi，可指定结果视频的大小
cv2.VideoWriter_fourcc('T', 'H', 'E', 'O')  Ogg Vorbis,文件名后缀为.ogv
cv2.VideoWriter_fourcc('F', 'L', 'V', '1')  Flash视频，文件名后缀为.flv
"""
out = cv2.VideoWriter("video/re.mp4", cv2.VideoWriter_fourcc('M', 'P', '4', 'V'), 15,
                     (np.int(width), np.int(height)), True)
while True:
    ret, frame = capture.read()
    if ret is True:
        cv2.imshow("video-input", frame)
        out.write(frame)
        c = cv2.waitKey(50)
        if c == 27:  # ESC
            break
    else:
        break

capture.release()
out.release()
