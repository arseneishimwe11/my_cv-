import cv2

# First determine the four coordinates of a ROI
image = cv2.imread('messi5.jpg', -1)
cv2.imshow("Messi", image)


def set_mouse_event(event, x, y, flag, params):
    if event == cv2.EVENT_LBUTTONUP:
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = str(x) + ',' + str(y)
        cv2.putText(image, text, (x, y), font, 1, (0, 0, 255), 3)
        print(x, y)
        cv2.imshow("Messi", image)


ball = image[324:286, 404:340]
image[256:213,  350:265] = ball

cv2.rectangle(image, (324, 286), (404, 340), (0, 0, 255), 2)
cv2.setMouseCallback('Messi', set_mouse_event)
cv2.imshow("Messi", image)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
