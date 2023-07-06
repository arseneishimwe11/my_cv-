import cv2
import numpy as np

# events = [a for a in dir(cv2) if 'EVENT' in a] This is to show all events available in the cv2.package
image = np.zeros((712, 600, 3), np.uint8)

img = cv2.imread('lena.png')
cv2.imshow("Mouse Events use", img)


def click_handle(event, x, y, flag, param):
    font = cv2.FONT_HERSHEY_SIMPLEX
    if event == cv2.EVENT_LBUTTONUP:
        text = str(x) + ',' + str(y)
        cv2.putText(img, text, (x, y), font, 2, (255, 255, 255), 3)
        cv2.imshow("Mouse Events use", img)
    if event == cv2.EVENT_RBUTTONUP:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        color_text = str(blue) + ',' + str(green) + ',' + str(blue)
        cv2.putText(img, color_text, (x, y), font, 1, (0, 255, 255), 2)
        cv2.imshow("Mouse Events use", img)


cv2.setMouseCallback("Mouse Events use", click_handle)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
