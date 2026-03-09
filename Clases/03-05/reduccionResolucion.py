import numpy as np 
import matplotlib.pyplot as plt 

img = plt.imread("nasa.jpg")

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