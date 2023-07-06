import cv2

x1 = int(input("x1:"))
y1 = int(input("y1:"))

image = cv2.imread('lena.jpg', -1)

cv2.circle(image, (x1, y1), 20, (0, 0, 255), -1)
print(image.size)
print(image.shape)
cv2.imshow("Lena", image)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
