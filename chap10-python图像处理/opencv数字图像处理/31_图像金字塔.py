import cv2


def pyramid_down(pyramid_images):
    level = len(pyramid_images)
    print("level = ",level)
    for i in range(level-1, -1, -1):
        expand = cv2.pyrUp(pyramid_images[i])
        cv2.imshow("pyramid_down_"+str(i), expand)


def pyramid_up(image, level=3):
    temp = image.copy()
    pyramid_images = []
    for i in range(level):
        dst = cv2.pyrDown(temp)
        pyramid_images.append(dst)
        temp = dst.copy()

    return pyramid_images


src = cv2.imread("images/3.jpg")
cv2.namedWindow("input", cv2.WINDOW_AUTOSIZE)
cv2.imshow("input", src)

pyramid_down(pyramid_up(src))

cv2.waitKey(0)
cv2.destroyAllWindows()
