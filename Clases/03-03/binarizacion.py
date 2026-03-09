import numpy as np 
import matplotlib.pyplot as plt 

img = plt.imread("nasa.jpg")

img_gris_f = img.astype(np.float32)

mx = np.max(img, axis=2)
mn = np.min(img, axis=2)

img_gris = (mx + mn) / 2 

img_gris = np.clip(img_gris, 0, 255).astype(np.uint8)

T = 50

img_bin = img_gris.copy()
img_bin =  np.where(img_bin >= T, 255, 0)

# plt.subplot(1,3,1)
# plt.imshow(img)
# plt.axis("off")
# plt.title("Imagen Original")

# plt.subplot(1,3,2)
# plt.imshow(img_gris, cmap="gray")
# plt.axis("off")
# plt.title("Imagen en Escala de Grises")

# plt.subplot(1,3,3)
# plt.imshow(img_bin, cmap="gray")
# plt.axis("off")
# plt.title("Imagen Binarizada")
# plt.show()

plt.imshow(img_bin, cmap="gray")
plt.axis("off")
plt.show()