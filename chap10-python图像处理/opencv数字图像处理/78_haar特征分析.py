import cv2

# capture = cv2.VideoCapture(1)
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt2.xml")
eye_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
smile_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")

image = cv2.imread('images/7.jpg')
faces = face_detector.detectMultiScale(image, scaleFactor=1.05, minNeighbors=3,
                                       minSize=(50, 50), maxSize=(300, 300))
for x, y, width, height in faces:
    cv2.rectangle(image, (x, y), (x + width, y + height), (0, 0, 255), 2, cv2.LINE_8, 0)
    roi = image[y:y + height, x:x + width]

    eyes = eye_detector.detectMultiScale(roi, scaleFactor=1.1, minNeighbors=5,
                                         minSize=(20, 20), maxSize=(30, 30))
    smiles = smile_detector.detectMultiScale(roi, scaleFactor=1.05, minNeighbors=2,
                                             minSize=(20, 20))

    for ex, ey, ew, eh in eyes:
        cv2.rectangle(roi, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)

    for sx, sy, sw, sh in smiles:
        cv2.rectangle(roi, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 2)
        cv2.putText(image, 'Smile', (x + 10, y - 7), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

cv2.imshow("faces", image)

cv2.waitKey(0)
'''
while True:
    ret, image = capture.read()
    if ret is True:
        cv2.imshow("frame", image)
        faces = face_detector.detectMultiScale(image, scaleFactor=1.05, minNeighbors=3,
                                          minSize=(30, 30), maxSize=(300, 300))
        for x, y, width, height in faces:
            cv2.rectangle(image, (x, y), (x+width, y+height), (0, 0, 255), 2, cv2.LINE_8, 0)
        roi = image[y:y+height,x:x+width]
        smiles = smile_detector.detectMultiScale(roi, scaleFactor=1.7, minNeighbors=3,
                                               minSize=(15, 15), maxSize=(100, 100))
        for sx, sy, sw, sh in smiles:
            cv2.rectangle(roi, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 1)

        cv2.imshow("faces", image)
        c = cv2.waitKey(50)
        if c == 27:
            break
    else:
        break
'''
cv2.destroyAllWindows()
