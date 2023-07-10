import cv2
import face_recognition

img1 = cv2.imread('bezos.png')
img1_to_rgb = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img_encoding = face_recognition.face_encodings(img1_to_rgb)[0]

img2 = cv2.imread('lena.jpg')
img2_to_rgb = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img2_encoding = face_recognition.face_encodings(img1_to_rgb)[0]

result = face_recognition.face_compare(img_encoding, img2_encoding)
print("Result:", result)
cv2.imshow("Bezos", img1_to_rgb)
cv2.imshow("Lena", img2_to_rgb)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
