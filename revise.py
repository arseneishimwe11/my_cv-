# import cv2
# import numpy as np
#
# image = cv2.imread('lena.jpg', -1)
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# gaussian_blur = cv2.GaussianBlur(gray_image, (5, 5), 7)
# kernel = np.ones((5, 5), np.uint8)
# erosion = cv2.erode(image, kernel, iterations=1)
# dilation = cv2.dilate(image, kernel, iterations=1)
# canny = cv2.Canny(image, 100, 200)
# x = 100
# y = 100
# h = 400
# w = 400
# crop = image[x:x+w, y:y+h]
# cv2.imshow("Original Image", image)
# cv2.imshow("Grayscale Image", gray_image)
# cv2.imshow("Gaussian Blur", gaussian_blur)
# cv2.imshow("Eroded", erosion)
# cv2.imshow("Dilated", dilation)
# cv2.imshow("Downscaled", crop)
# cv2.imshow("Canny", canny)
# if cv2.waitKey(0) & 0xFF == ord('q'):
#     cv2.destroyAllWindows()
#


# import cv2
#
# image = cv2.imread("Faces.png", 1)
#
# faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
#
# faces = faceCascade.detectMultiScale(
#     image,
#     scaleFactor=1.2,
#     minNeighbors=2,
#     minSize=(55, 85)
# )
# for(a, b, c, d) in faces:
#     cv2.rectangle(image, (a, b), (a+c, b+d), (0, 255, 0), 2)
# cv2.imshow("Image with faces", image)
# if cv2.waitKey(0) & 0xFF == ord('q'):
#     cv2.destroyAllWindows()


import cv2
import numpy as np

image = np.zeros([512, 512, 3], np.uint8)
text = "You can learn open CV"

cv2.putText(image, text, (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3, cv2.LINE_AA)
cv2.imshow("Image with text", image)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
