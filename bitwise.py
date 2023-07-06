import cv2

chess_image = cv2.imread('chessboard.png')
cv2.imshow("Image", chess_image)
image = cv2.bitwise_not(chess_image)
width = int(image.shape[1] * 0.3)
height = int(image.shape[0] * 0.5)
dim = (height, width)
bitwise_not = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

cv2.imshow("Bitwise Image", image)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
