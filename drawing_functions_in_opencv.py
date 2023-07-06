import cv2
import numpy as np

# image = cv2.imread('lena.jpg')
image = np.zeros([700, 700, 3], np.uint8)
line = cv2.arrowedLine(image, (100, 40), (255, 255), (0, 255, 0), 5)  # (image, starting coordinates, ending coordinate)
rectangle = cv2.rectangle(image, (200, 40), (400, 200), (0, 200, 255), 2)
circle = cv2.circle(image, (200, 100), 100, (244, 233, 100), -1)
cv2.putText(image, "Opencv learning", (10, 500), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0, 255, 255), 2, cv2.LINE_AA)
cv2.imshow("Lena", image)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
