import numpy as np 
import matplotlib.pyplot as plt 


print("Escala de grises")

ruta="nasa.jpg"

img = plt.imread(ruta)

img_gris_f = img.astype(np.float32)

img_gris = 0.299*img_gris_f[:,:,0] + 0.587*img_gris_f[:,:,1] + 0.114*img_gris_f[:,:,2]

img_gris = np.clip(img_gris, 0 , 255).astype(np.uint8)

plt.subplot(1,3,1)
plt.imshow(img)
plt.title("Original")
plt.axis("off")


plt.subplot(1,3,2)
plt.imshow(img_gris, cmap="gray")
plt.title("Gris Luminosity")
plt.axis("off")


plt.subplot(1,3,3)
plt.imshow(img_gris)
plt.title("Gris Luminosity (sin cmap)")
plt.axis("off")
plt.show()
