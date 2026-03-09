import cv2
import matplotlib.pyplot as plt

img = cv2.imread('reduced.jpg')

if img is None:
    print("Image not found!")
    exit()

darker = cv2.convertScaleAbs(img, alpha=1, beta=-50)

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.title("Original")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(1,2,2)
plt.title("Reduced Brightness")
plt.imshow(cv2.cvtColor(darker, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.show()