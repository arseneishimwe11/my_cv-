import cv2

stream = cv2.VideoCapture('test.mp4')
if not stream.isOpened():
    print("The video failed to open!")
while stream.isOpened():
    ref, frame = stream.read()
    if ref:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Streamed Video", frame)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    else:
        break

stream.release()
cv2.destroyAllWindows()

