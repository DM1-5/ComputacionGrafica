import numpy as np 
import matplotlib.pyplot as plt 

ruta = "datos.jpg"

img = plt.imread(ruta)

print("tipo:", type(img)) # Retorna el tipo de dato de la variable img, que es un arreglo de numpy.

print("size:", img.shape) # Retorna el tamaño del arreglo img, que es una tupla con el numero de filas, columnas y canales de color (en este caso, 3 canales para RGB).
# Existe un 4to canal, el canal alfa, que representa la transparencia de la imagen.

print("max/min:", img.max(), img.min()) # Retorna el valor maximo y minimo de los elementos del arreglo img, que son los valores de intensidad de los pixeles de la imagen. El valor maximo es 1.0 y el valor minimo es 0.0, lo que indica que la imagen esta normalizada entre 0 y 1.

# Para imagenes en jpg el valor maximo es 255 y el valor minimo es 0, lo que indica que la imagen esta en formato de 8 bits por canal.
# Para imagenes en png el valor maximo es 1.0 y el valor minimo es 0.0, lo que indica que la imagen esta normalizada entre 0 y 1.

# Crea una copia de las capas.
CapaR =np.copy(img)
CapaG =np.copy(img)
CapaB =np.copy(img)

# Capa roja
CapaR[:,:,1] = CapaR[:,:,2] = 0 
# Capa verde
CapaG[:,:,0] = CapaG[:,:, 2] = 0
# Capa azul
CapaB[:,:,0] = CapaB[:,:,1] = 0



# Muestra las imagenes 
plt.subplot(2,2,1) 
plt.imshow(img)
plt.axis("off")
plt.title("Imagen original")

# Mostrar la capa roja
plt.subplot(2,2,2)
plt.imshow(CapaR)
plt.axis("off")
plt.title("Capa roja")

# Mostrar la capa roja
plt.subplot(2,2,3)
plt.imshow(CapaG)
plt.axis("off")
plt.title("Capa verde")

# Mostrar la capa roja
plt.subplot(2,2,4)
plt.imshow(CapaB)
plt.axis("off")
plt.title("Capa azul")


# Mostrar todas las figuras en una ventana 
plt.show()
