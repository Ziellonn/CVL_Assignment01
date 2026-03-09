import cv2
import matplotlib.pyplot as plt

img = cv2.imread('roject4.jpg')

if img is None:
    print("Image not found!")
    exit()

lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

l, a, b = cv2.split(lab)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl = clahe.apply(l)

limg = cv2.merge((cl, a, b))

enhanced = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.title("Original")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(1,2,2)
plt.title("CLAHE Result")
plt.imshow(cv2.cvtColor(enhanced, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.show()