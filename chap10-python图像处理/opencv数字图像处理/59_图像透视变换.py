import cv2
import numpy as np
"""
仿射变换affine transformation：是另外两种简单变换的叠加：一个是线性变换，一个是平移变换
仿射变换变化包括缩放（Scale、平移(transform)、旋转(rotate)、反射（reflection,对图形照镜子）、错切(shear mapping，感觉像是一个图形的倒影)，
原来的直线仿射变换后还是直线，原来的平行线经过仿射变换之后还是平行线，这就是仿射。

透视变换（Perspective Transformation），又称Homography Transformation。
透视变换 === 单应性变换
单应性变换 Homography transformation：单应性变换其实就是一个平面到另一个平面的变换关系。
    两幅图像中的相同物理点，称之为对应点。一个Homography是一个变换（3×3矩阵），将一个图像中的点映射到另一个图像中的对应点。


"""
src = cv2.imread("images/6.jpg")
cv2.namedWindow("input", cv2.WINDOW_AUTOSIZE)
cv2.imshow("input", src)

# 图像二值化
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

se = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3), (-1, -1))
binary = cv2.morphologyEx(binary, cv2.MORPH_OPEN, se)
cv2.imshow("binary", binary)


# 轮廓提取, 发现最大轮廓
contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 寻找最大面积轮廓
cnt_maxArea = sorted(contours, key=cv2.contourArea)[0]

# 寻找最小外接矩形,返回最小外接矩形的（中心(x,y), (宽,高), 旋转角度）
rect = cv2.minAreaRect(cnt_maxArea)
print(rect[2])
print(rect[0])
# trick
height, width = rect[1]
print(rect[1])
box = cv2.boxPoints(rect)
src_pts = np.int0(box)
print(src_pts)

dst_pts = [[width, height], [0, height], [0, 0], [width, 0]]

# 透视变换
"""
Finds a perspective transformation between two planes. 计算透视矩阵
Applies a perspective transformation to an image. 应用透视矩阵
"""
M, status = cv2.findHomography(src_pts, np.array(dst_pts))  # 原图到透视后的图的四个点的转换矩阵
result = cv2.warpPerspective(src, M, (np.int32(width), np.int32(height)))

if height < width:
    result = cv2.rotate(result, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow("result", result)


cv2.waitKey(0)
cv2.destroyAllWindows()
