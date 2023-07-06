import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
if not cap.isOpened():
    print("The video was not opened!")
while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        out.write(frame)
        cv2.imshow("Video Stream", frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
out.release()
cap.release()
cv2.destroyAllWindows()
