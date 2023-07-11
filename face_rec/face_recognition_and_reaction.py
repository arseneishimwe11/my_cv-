import cv2
import face_recognition
import serial
import time

if __name__ == "__main__":
    ser = serial.Serial(
        port="COM3",
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )
    ser.flush()

live_cap = cv2.VideoCapture(0)

my_face = face_recognition.load_image_file("my_face.png")
my_face_encoded = face_recognition.face_encodings(my_face)[0]

if not live_cap.isOpened():
    print("Failed to livestream the video!")


def do_my_face_detected():
    # interactions with the green LED
    ser.write(b"ON\n")


def do_my_face_not_detected():
    # interactions with the red LED
    ser.write(b"OFF\n")


# Start the live video stream
while live_cap.isOpened():
    ret, frame = live_cap.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    if ret:
        # Face detections
        face_location = face_recognition.face_locations(rgb_frame)
        frame_face_encodings = face_recognition.face_encodings(rgb_frame, face_location)
        for (top, right, bottom, left), frame_face_encoding in zip(face_location, frame_face_encodings):
            if len(face_location) == 0:
                do_my_face_not_detected()
            else:
                # Faces comparison
                distances = face_recognition.face_distance([my_face_encoded], frame_face_encoding)
                min_distance = min(distances)

                cv2.rectangle(rgb_frame, (left, top), (right, bottom), (0, 255, 255), 3)
                font = cv2.FONT_HERSHEY_SIMPLEX
                name = "Arsene"
                cv2.putText(rgb_frame, name, (left, top), font, 2, (0, 255, 255), 2, cv2.LINE_AA)

                if min_distance < 0.6:
                    # React the detection of my face by sending some signal to the green LED
                    do_my_face_detected()
                else:
                    # React to the detection of an unknown face by sending some signal to the red LED
                    do_my_face_not_detected()

        cv2.imshow("Face recognition", rgb_frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

    time.sleep(0.5)

live_cap.release()
cv2.destroyAllWindows()

