import cv2
import sys

# imagePath = sys.argv[0]
image = cv2.imread("Lena.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

faces = faceCascade.detectMultiScale(
    gray_image,
    scaleFactor=1.3,
    minNeighbors=3,
    minSize=(200, 200)
)
print("[INFO] Found {0} faces".format(len(faces)))
count = 1
for (x, y, z, h) in faces:
    face = image[x:x+z, y:y+h]
    filename = str(count)+'.jpg'
    status = cv2.imwrite(filename, face)
    print("Image" + filename + "saved?", status)
    count += 1
    cv2.imshow("Faces", face)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()


