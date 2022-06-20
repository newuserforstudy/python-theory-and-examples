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
h, w = src.shape[:2]
copy = np.copy(src)
copy = add_salt_pepper_noise(copy)

result = np.zeros([h, w * 2, 3], dtype=src.dtype)
result[0:h, 0:w, :] = src
result[0:h, w:2 * w, :] = copy
cv2.putText(result, "original image", (10, 30), cv2.FONT_HERSHEY_PLAIN, 2.0, (0, 255, 255), 1)
cv2.putText(result, "salt pepper image", (w + 10, 30), cv2.FONT_HERSHEY_PLAIN, 2.0, (0, 255, 255), 1)
cv2.imshow("salt pepper noise", result)
# cv2.imwrite("./result.png", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
