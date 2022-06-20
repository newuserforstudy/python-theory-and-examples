import cv2
import numpy as np

src = cv2.imread("images/3.jpg")
cv2.namedWindow("input", cv2.WINDOW_AUTOSIZE)
cv2.imshow("input", src)

h, w = src.shape[:2]
dst = cv2.edgePreservingFilter(src, sigma_s=100, sigma_r=0.4, flags=cv2.RECURS_FILTER)
result = np.zeros([h, w * 2, 3], dtype=src.dtype)
result[0:h, 0:w, :] = src
result[0:h, w:2 * w, :] = dst
result = cv2.resize(result, (w, h // 2))
cv2.imshow("result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
