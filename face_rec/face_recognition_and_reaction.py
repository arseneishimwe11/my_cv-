import cv2
import face_recognition
from simple_facerec import SimpleFacerec

live_cap = cv2.VideoCapture(0)

image = cv2.imread("my_face.png")
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

if not live_cap.isOpened():
    print("Failed to livestream the video!")

my_face_encoded = face_recognition.face_encodings(rgb_image)[0]
def do_my_face_detected():
    #interactions with the green LED
    pass


def do_my_face_not_detected():
    #interactions with the red LED
    pass


while live_cap.isOpened():
    ret, frame = live_cap.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    if ret:
        #Face detections
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = faceCascade.detectMultiScale(
            rgb_frame,
            scaleFactor=1.2,
            minNeighbors=2,
            minSize=(50, 50)
        )
        for(a, b, c, d) in faces:
            cv2.rectangle(rgb_frame, (a, b), (a+c, b+d), (0, 255, 255), 3)
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = "Arsene"
            cv2.putText(rgb_frame, name, (a, b), font, 2, (0, 255, 255), 2)



        def is_face_detected_mine():
            frame_face_encodings = face_recognition.face_encodings(rgb_frame)[0]
            result = face_recognition.face_compare([my_face_encoded], frame_face_encodings)

            if result:
                return result
            else:
                return False


        if is_face_detected_mine:
            do_my_face_detected()
            #React the detection of the correct faces by sending some signal to the green LED
        else:
            do_my_face_not_detected()
            #React to the detection of an unknown face by sending some signal to the red LED

        cv2.imshow("Face recognition", rgb_frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    else:
        break

live_cap.release()
cv2.destroyAllWindows()

