import numpy as np 
import matplotlib.pyplot as plt 
from pathlib import Path

BASE = Path(__file__).parent # Ruta del directorio actual del archivo .py
imagen = "nasa.jpg"

ruta = BASE.parent.parent / "Imagenes" / imagen # Ruta del archivo de imagen, que se encuentra en el directorio "Imagenes" que esta en el mismo nivel que el directorio "Clases".

img = plt.imread(ruta)

# verificar el shape.

if img.dtype == np.uint8:
    print(f"La imagen es de tipo {img.dtype}")
    imgf = img.astype(np.float32)
    img_clipR = img.copy()
    img_clipR[:,:,0] = (np.clip(imgf[:,:,0] + 50, 0 , 255)).astype(np.uint8)
else:  
    print(f"La imagen es de tipo {img.dtype}")
    img_clipR = img.copy()
    img_clipR[:,:,0] = np.clip(img[:,:,0] + 0.6, 0 , 1)

plt.subplot(1,2,1)
plt.imshow(img)
plt.axis("off")
plt.title("Imagen Original")

plt.subplot(1,2,2)
plt.imshow(img_clipR)
plt.axis("off")
plt.title("Imagen con Brillo Ajustado en el canal rojo")

plt.show()

