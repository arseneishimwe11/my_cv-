import cv2

stream = cv2.VideoCapture(0)

if not stream.isOpened():
    print("The live stream failed")
while stream.isOpened():
    ret, frame = stream.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=2,
            minSize=(100, 100)
        )
        stream.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        stream.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        for (a, b, c, d) in faces:
            cv2.rectangle(gray, (a, b), (a+c, b+d), (0, 255, 255), 2)
        cv2.imshow('Live Stream', gray)
        cv2.imwrite('Detected_face.png', gray)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
stream.release()
cv2.destroyAllWindows()
