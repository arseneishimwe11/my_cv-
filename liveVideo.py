import cv2

cap = cv2.VideoCapture(0)

while True:
    ref, frame = cap.read()
    if ref:
        cv2.imshow("Video frame", frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()

