import numpy as np 
import matplotlib.pyplot as plt 
from PIL import Image
from pathlib import Path

BASE = Path(__file__).parent # Ruta del directorio actual del archivo .py
imagen = "fondo.jpg"

ruta = BASE.parent.parent / "Imagenes" / imagen # Ruta del archivo de imagen, que se encuentra en el directorio "Imagenes" que esta en el mismo nivel que el directorio "Clases".

img_fondo = plt.imread(ruta)

imagen = "per.jpg"
ruta = BASE.parent.parent / "Imagenes" / imagen
img_personaje = plt.imread(ruta)

print("Fondo:")
print(img_fondo.dtype )
print(img_fondo.shape)

print("personaje")
print(img_personaje.dtype)
print(img_personaje.shape)

# Cambia el tamaño de las imagenes para unirlas.
  #h,w,_ = img_fondo.shape
  #img_fondo = np.array(Image.fromarray(img_personaje).resize((w, h)))

A = img_fondo.astype(np.float32)
B = img_personaje.astype(np.float32)

fusion = (A + B)//2
fusion = np.clip(fusion, 0 , 255).astype(np.uint8)

plt.subplot(1,3,1)
plt.imshow(img_fondo)
plt.title("fondo jpg")
plt.axis("off")

plt.subplot(1,3,2)
plt.imshow(img_personaje)
plt.title("otra foto jpg")
plt.axis("off")

plt.subplot(1,3,3)
plt.imshow(fusion)
plt.title("suma")
plt.axis("off")

plt.show()

