import cv2

# capture = cv2.VideoCapture(1)
detector = cv2.CascadeClassifier("xml/lbpcascade_frontalface_improved.xml")
image = cv2.imread('images/7.jpg')

faces = detector.detectMultiScale(image, scaleFactor=1.05, minNeighbors=1, minSize=(30, 30), maxSize=(200, 200))

for x, y, width, height in faces:
    cv2.rectangle(image, (x, y), (x+width, y+height), (0, 0, 255), 2, cv2.LINE_8, 0)

cv2.imshow("faces", image)


c = cv2.waitKey(0)
'''
while True:
    ret, image = capture.read()
    if ret is True:
        cv.imshow("frame", image)
        faces = detector.detectMultiScale(image, scaleFactor=1.05, minNeighbors=1,
                                          minSize=(30, 30), maxSize=(120, 120))
        for x, y, width, height in faces:
            cv.rectangle(image, (x, y), (x+width, y+height), (0, 0, 255), 2, cv.LINE_8, 0)
        cv.imshow("faces", image)
        c = cv.waitKey(50)
        if c == 27:
            break
    else:
        break
'''
cv2.destroyAllWindows()

