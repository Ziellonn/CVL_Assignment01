import cv2

img = cv2.imread('reduce before.jpg')

if img is None:
    print("Image not found!")
    exit()

darker = cv2.convertScaleAbs(img, alpha=1, beta=-50)

cv2.imwrite('reduce after.jpg', darker)

