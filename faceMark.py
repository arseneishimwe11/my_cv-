import cv2

image = cv2.imread("faces.png")
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = faceCascade.detectMultiScale(
    image,
    scaleFactor=1.2,
    minNeighbors=2,
    minSize=(50, 50)

)
count = 1
for (a, b, c, d) in faces:
    cv2.rectangle(image, (a, b), (a+c, b+d), (255, 0, 0), 2)

cv2.imshow("Faces", image)
cv2.imwrite("Scanned_Faces.jpg", image)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
