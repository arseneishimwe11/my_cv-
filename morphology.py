import cv2
import numpy as np

image = cv2.imread("lena.jpg")
kernel = np.ones((5, 5), np.uint8)
# This line created a 2-D array of 5 rows and 5 columns and the np.uint8 is assigning
# the integers to unsigned 8-bit integer datatype
erosion = cv2.erode(image, kernel, iterations=1)
dilation = cv2.dilate(image, kernel, iterations=1)
cropped_lena = cv2.Canny(image, 100, 200)
cv2.imshow("Eroded Image", erosion)
cv2.imshow("Dilated Image", dilation)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
