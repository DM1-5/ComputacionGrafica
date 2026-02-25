import numpy as np 
import matplotlib.pyplot as plt 
from PIL import Image

img_fondo = plt.imread("fondo.jpg")
img_personaje = plt.imread("per.jpg")

print("Fondo:")
print(img_fondo.dtype )
print(img_fondo.shape)

print("personaje")
print(img_personaje.dtype)
print(img_personaje.shape)

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

