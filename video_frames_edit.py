import cv2
import datetime

cap = cv2.VideoCapture('test.mp4')
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# cap.set(3, 1024)
# cap.set(4, 720)
# print(cap.get(3))
# print(cap.get(4))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
if not cap.isOpened():
    print("The video opening failed!")
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        font = cv2.FONT_HERSHEY_SIMPLEX
        date_time = str(datetime.datetime.now())
        text = "Width: " + str(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) + " Height: " + str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        frame = cv2.putText(frame, date_time + text, (10, 20), font, 0.6, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow("Video_frames", frame)
    else:
        break
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
