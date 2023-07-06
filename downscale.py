import cv2

img = cv2.imread('lena.jpg', cv2.IMREAD_UNCHANGED)
percent = 50 / 100
height = int(img.shape[0] * percent)    # shape at index 0 means the height
width = int(img.shape[1] * percent)  # shape at index one returns the new width
dim = (width, height)
print(img.shape)
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Downscaled image", resized)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
