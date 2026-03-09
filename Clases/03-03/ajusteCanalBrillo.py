import numpy as np 
import matplotlib.pyplot as plt 


img = plt.imread("nasa.jpg")
#img = plt.imread("datos.png")

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

