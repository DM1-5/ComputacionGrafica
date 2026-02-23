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
CapaC =np.copy(img)
CapaM =np.copy(img)
CapaA =np.copy(img)

# Capa Cyan
CapaC[:,:,0] = 0 # Elimino el canal rojo
# Capa Magenta  
CapaM[:,:,1]= 0 # Elimino el canal verde
# Capa Amarilla
CapaA[:,:,2]= 0 # Elimino el canal Azul



# Muestra las imagenes 
plt.subplot(2,2,1) 
plt.imshow(img)
plt.axis("off")
plt.title("Imagen original")

# Mostrar la capa roja
plt.subplot(2,2,2)
plt.imshow(CapaC)
plt.axis("off")
plt.title("Capa Cyan")

# Mostrar la capa roja
plt.subplot(2,2,3)
plt.imshow(CapaM)
plt.axis("off")
plt.title("Capa Magenta")

# Mostrar la capa roja
plt.subplot(2,2,4)
plt.imshow(CapaA)
plt.axis("off")
plt.title("Capa Amarilla")


# Mostrar todas las figuras en una ventana 
plt.show()
