import numpy as np 
import matplotlib.pyplot as plt 


ejercicio1 = np.zeros((3,3,3))
# crea un arreglo de 3 dimensiones con 3 filas, 3 columnas y 3 canales de color (RGB), lleno de unos.



# Pixel 0,0

ejercicio1[0,0,0] = 0 
ejercicio1[0,0,1] = 1 
ejercicio1[0,0,2] = 1 
 
# Pixel 0,1
ejercicio1[0,1,0] = 1
ejercicio1[0,1,1] = 1
ejercicio1[0,1,2] = 1

# Pixel 0,2
ejercicio1[0,2,0] = 1
ejercicio1[0,2,1] = 0
ejercicio1[0,2,2] = 0

# Pixel 1,0
ejercicio1[1,0,0] = 1
ejercicio1[1,0,1] = 0
ejercicio1[1,0,2] = 1

# pixel 1,1
ejercicio1[1,1,0] = 0.5
ejercicio1[1,1,1] = 0.5
ejercicio1[1,1,2] = 0.5

# Pixel 1,2
ejercicio1[1,2,0] = 0
ejercicio1[1,2,1] = 1
ejercicio1[1,2,2] = 0

# Pixel 2,0 Amarillo 
ejercicio1[2,0,0] = 1
ejercicio1[2,0,1] = 1
ejercicio1[2,0,2] = 0

#Pixel 2,1 Negro
ejercicio1[2,1,0] = 0
ejercicio1[2,1,1] = 0
ejercicio1[2,1,2] = 0


# Pixel 2,2 
ejercicio1[2,2,0] = 0
ejercicio1[2,2,1] = 0
ejercicio1[2,2,2] = 1


plt.imshow(ejercicio1)  
plt.axis("off")
plt.title("Ejercicio 1")
plt.show()

#7x11 6x8