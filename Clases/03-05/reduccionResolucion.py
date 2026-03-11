import numpy as np 
import matplotlib.pyplot as plt 
from pathlib import Path

BASE = Path(__file__).parent # Ruta del directorio actual del archivo .py
imagen = "nasa.jpg"

ruta = BASE.parent.parent / "Imagenes" / imagen # Ruta del archivo de imagen, que se encuentra en el directorio "Imagenes" que esta en el mismo nivel que el directorio "Clases".

img = plt.imread(ruta)

f = 100

img_reducida = img[::f, ::f]

print("Tamaño Original:" )


#plt.figure(figsize=(8,6)) # Modifica el tamaño de la ventana que crea el subplot

#plt.figure(figsize=(21,18))
plt.subplot(2,1,1)
plt.imshow(img)
plt.title("Imagen Original")
plt.axis("off")

plt.subplot(2,1,2)
plt.title("Imagen Reducida")
plt.imshow(img_reducida)
plt.axis("off")
plt.show()