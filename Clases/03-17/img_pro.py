import numpy as np 
import matplotlib.pyplot as plt 
from pathlib import Path

BASE = Path(__file__).parent # Ruta del directorio actual del archivo .py
imagen = "nasa.jpg"

ruta = BASE.parent.parent / "Imagenes" / imagen # Ruta del archivo de imagen, que se encuentra en el directorio "Imagenes" que esta en el mismo nivel que el directorio "Clases".

def aumentar_brillo(imagen, valor):
    if imagen.dtype == np.uint8:
        #print(f"La imagen es de tipo {imagen.dtype}")
        imgf = imagen.astype(np.float32)
        img_clip = (np.clip(imgf + valor, 0 , 255)).astype(np.uint8)
    else:  
        #print(f"La imagen es de tipo {imagen.dtype}")
        img_clip = np.clip(imagen + valor/255.0, 0 , 1) 

    return img_clip

img = plt.imread(ruta)

if __name__ == "__main__":
    valor = 50 # Valor de brillo a aumentar (puede ser positivo o negativo)
    img_clip = aumentar_brillo(img, valor)
    plt.subplot(1,2,1)
    plt.imshow(img)
    plt.axis("off")
    plt.title("Imagen Original")

    plt.subplot(1,2,2)
    plt.imshow(img_clip)
    plt.axis("off")
    plt.title("Imagen con Brillo Ajustado")

    plt.show()


