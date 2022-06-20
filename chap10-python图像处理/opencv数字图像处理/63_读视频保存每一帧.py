import cv2

video = cv2.VideoCapture(f"video/test.avi")
i = 0
while True:

    ret, frame = video.read()
    if ret:

        name = "D:\\sdh\\NowWorks\\opencv\\video\\images\\" + "%03d" % i
        image_name = name + ".jpg"
        print(image_name)
        cv2.imwrite(image_name, frame)
        i = i + 1
    else:
        break
