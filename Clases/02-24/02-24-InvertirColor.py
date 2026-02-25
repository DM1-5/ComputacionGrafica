import numpy as np 
import matplotlib.pyplot as plt 
from PIL import Image

ruta = "datos.jpg"

img = plt.imread(ruta)

print("tipo:", type(img)) # Retorna el tipo de dato de la variable img, que es un arreglo de numpy.

print("size:", img.shape) # Retorna el tamaño del arreglo img, que es una tupla con el numero de filas, columnas y canales de color (en este caso, 3 canales para RGB).
# Existe un 4to canal, el canal alfa, que representa la transparencia de la imagen.

print("max/min:", img.max(), img.min()) # Retorna el valor maximo y minimo de los elementos del arreglo img, que son los valores de intensidad de los pixeles de la imagen. El valor maximo es 1.0 y el valor minimo es 0.0, lo que indica que la imagen esta normalizada entre 0 y 1.

print(img.dtype)

plt.subplot(1,2,1)
plt.imshow(img)
plt.title("imagen original")
plt.axis("off")

inv = 255 - img

plt.subplot(1,2,2)
plt.imshow(inv)
plt.title("imagen invertida")
plt.axis("off")

plt.show()