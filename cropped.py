import cv2

image = cv2.imread('lena.jpg')
x = 100  # This is where you want to start from but in x-axis direction
y = 40    # This is where you want to start from but in y-axis direction
l = 400
w = 400
cropped_img = image[x:x+w, y:y+l]  # Specifying the range of rows and columns you want to extract
cv2.imwrite('Cropped_lena.png', cropped_img)
cv2.imshow("Original Image", image)
cv2.imshow("Cropped image", cropped_img)
print(cropped_img.shape)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
    