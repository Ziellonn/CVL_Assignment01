import cv2

img = cv2.imread('Contrast before.jpg')

if img is None:
    print("Image not found!")
    exit()

print("Image loaded successfully")

lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

l, a, b = cv2.split(lab)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl = clahe.apply(l)

limg = cv2.merge((cl, a, b))

enhanced = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

cv2.imwrite('Contrast after.jpg', enhanced)
