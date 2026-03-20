import libreria as lib
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path


BASE = Path(__file__).parent # Ruta del directorio actual del archivo .py
imagenJPG = "datos.jpg"
imagenPNG = "datos.png"
ruta_jpg = BASE.parent.parent / "Imagenes" / imagenJPG # Ruta del archivo de imagen, que se encuentra en el directorio "Imagenes" que esta en el mismo nivel que el directorio "Clases".
ruta_png = BASE.parent.parent / "Imagenes" / imagenPNG # Ruta del archivo de imagen, que se encuentra en el directorio "Imagenes" que esta en el mismo nivel que el directorio "Clases".

resultado_jpg = lib.gris_MidGray(ruta_jpg)
resultado_png = lib.gris_MidGray(ruta_png)

plt.subplot(1, 2, 1)
plt.imshow(resultado_jpg, cmap="gray")
plt.axis("off")
plt.title("jpg")

plt.subplot(1, 2, 2)
plt.imshow(resultado_png, cmap="gray")
plt.axis("off")
plt.title("png")

plt.show()
