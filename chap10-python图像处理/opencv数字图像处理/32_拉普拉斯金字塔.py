import cv2


def pyramid_up(image, level=5):
    temp = image.copy()

    pyramid_images = []
    for i in range(level):
        dst = cv2.pyrDown(temp)
        pyramid_images.append(dst)
        temp = dst.copy()
    return pyramid_images


def laplaian_demo(pyramid_images):
    level = len(pyramid_images)
    for i in range(level-1, -1, -1):
        if (i-1) < 0:
            h, w = src.shape[:2]
            expand = cv2.pyrUp(pyramid_images[i], dstsize=(w, h))
            lpls = cv2.subtract(src, expand) + 127
            cv2.imshow("lpls_" + str(i), lpls)
        else:
            h, w = pyramid_images[i-1].shape[:2]
            expand = cv2.pyrUp(pyramid_images[i], dstsize=(w, h))
            lpls = cv2.subtract(pyramid_images[i-1], expand) + 127
            cv2.imshow("lpls_"+str(i), lpls)


src = cv2.imread("images/3.jpg")
laplaian_demo(pyramid_up(src))
cv2.waitKey()