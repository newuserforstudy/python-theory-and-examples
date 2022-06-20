import cv2
import numpy as np

image = np.zeros((512, 512, 3), dtype=np.uint8)

cv2.rectangle(image, (100, 100), (300, 300), (255, 0, 0), 2, cv2.LINE_8, 0)
cv2.circle(image, (256, 256), 50, (0, 0, 255), 2, cv2.LINE_8, 0)
cv2.ellipse(image, (256, 256), (150, 50), 360, 0, 360, (0, 255, 0), 2, cv2.LINE_8, 0)
cv2.imshow("image", image)
cv2.waitKey(0)

for i in range(100000):
    image[:, :, :] = 0
    x1 = np.random.rand() * 512
    y1 = np.random.rand() * 512
    x2 = np.random.rand() * 512
    y2 = np.random.rand() * 512

    b = np.random.randint(0, 256)
    g = np.random.randint(0, 256)
    r = np.random.randint(0, 256)
    # cv.line(image, (np.int(x1), np.int(y1)), (np.int(x2), np.int(y2)), (b, g, r), 4, cv2.LINE_8, 0)
    cv2.rectangle(image, (np.int(x1), np.int(y1)), (np.int(x2), np.int(y2)), (b, g, r), 1, cv2.LINE_8, 0)
    cv2.imshow("image", image)
    c = cv2.waitKey(20)
    if c == 27:
        break  # ESC不

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
