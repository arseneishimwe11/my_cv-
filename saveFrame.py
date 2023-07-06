import cv2

stream = cv2.VideoCapture('test.mp4')
frame_count = int(stream.get(cv2.CAP_PROP_FRAME_COUNT))
count = 1
if not stream.isOpened():
    print("The video not opened!")
while stream.isOpened():
    ret, frame = stream.read()
    if not ret:
        break
    cv2.imwrite(str(count) + '.jpg', frame)
    count += 1
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()

