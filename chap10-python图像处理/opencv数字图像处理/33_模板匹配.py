import cv2

image1 = cv2.imread("images/3.jpg")
image2 = cv2.imread("images/4.jpg")

"""
模板匹配的方法：
CV_TM_SQDIFF：差值平方和匹配 
CV_TM_SQDIFF_NORMED：标准化差值平方和匹配 
CV_TM_CCORR：相关匹配 
CV_TM_CCORR_NORMED：标准相关匹配 
CV_TM_CCOEFF：相关匹配 
CV_TM_CCOEFF_NORMED：标准相关匹配 

"""
# 1 单模板匹配单个目标
res = cv2.matchTemplate(image1, image2, cv2.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

# 2 单模板匹配多个目标
pass
