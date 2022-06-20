
import cv2
import numpy as np


def add_salt_pepper_noise(image):
    h, w = image.shape[:2]
    nums = 10000
    rows = np.random.randint(0, h, nums, dtype=np.int)
    cols = np.random.randint(0, w, nums, dtype=np.int)
    for i in range(nums):
        if i % 2 == 1:
            image[rows[i], cols[i]] = (255, 255, 255)
        else:
            image[rows[i], cols[i]] = (0, 0, 0)
    return image


def gaussian_noise(image):
    noise = np.zeros(image.shape, image.dtype)
    m = (15, 15, 15)
    s = (30, 30, 30)
    cv2.randn(noise, m, s)
    dst = cv2.add(image, noise)
    cv2.imshow("gaussian noise", dst)
    return dst


src = cv2.imread("images/3.jpg")
cv2.imshow("input", src)
h, w = src.shape[:2]
src = gaussian_noise(src)

result1 = cv2.blur(src, (5, 5))
cv2.imshow("result-1", result1)

result2 = cv2.GaussianBlur(src, (5, 5), 0)
cv2.imshow("result-2", result2)

result3 = cv2.medianBlur(src, 5)
cv2.imshow("result-3", result3)

result4 = cv2.fastNlMeansDenoisingColored(src, None, 15, 15, 10, 30)
cv2.imshow("result-4", result4)

cv2.waitKey(0)
cv2.destroyAllWindows()

