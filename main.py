# importing the cv2
import cv2

# image reading
img = cv2.imread('lena.jpg', 1)
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur_image = cv2.GaussianBlur(gray_image, (7, 7), 5)
img_edges = cv2.Canny(img, 100, 200)
cv2.imshow("Lena Image", img)
cv2.imshow("Gray Lena Image", gray_image)
cv2.imshow("Blurred Gray Image", blur_image)
cv2.imshow("Image edges", img_edges)
# cv2.imwrite("Lena gray_copy.png", gray_image)
# cv2.imwrite("Lena blurred image.png", blur_image)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()

