import numpy as np 
import matplotlib.pyplot as plt 
from PIL import Image
from pathlib import Path

BASE = Path(__file__).parent # Ruta del directorio actual del archivo .py
imagen = "nasa.jpg"

ruta = BASE.parent.parent / "Imagenes" / imagen # Ruta del archivo de imagen, que se encuentra en el directorio "Imagenes" que esta en el mismo nivel que el directorio "Clases".

img = plt.imread(ruta)

img_gris_f = img.astype(np.float32)

img_gris = ((img_gris_f[:,:,0] + img_gris_f[:,:,1] + img_gris_f[:,:,2])/3).astype(np.uint8)


plt.subplot(1,3,1)
plt.imshow(img)
plt.title("Original")
plt.axis("off")


plt.subplot(1,3,2)
plt.imshow(img_gris, cmap="gray")
plt.title("Gris promedio")
plt.axis("off")


plt.subplot(1,3,3)
plt.imshow(img_gris)
plt.title("Gris promedio (sin cmap)")
plt.axis("off")
plt.show()
