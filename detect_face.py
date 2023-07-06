import cv2

cap = cv2.VideoCapture("test.mp4")
if not cap.isOpened():
    print("Error! The video was not opened!")
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = faceCascade.detectMultiScale(
            frame,
            scaleFactor=1.5,
            minNeighbors=3,
            minSize=(60, 60)
        )
        for(a, b, c, d) in faces:
            cv2.rectangle(frame, (a, b), (a+c, b+d), (255, 0, 0), 3)
        cv2.imshow("Cap frames", frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()

