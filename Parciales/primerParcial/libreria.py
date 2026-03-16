import numpy as np 
import matplotlib.pyplot as plt 
import math
from PIL import Image

def color_a_RGB(color):
    """Convierte un color a su representación RGB en el rango de 0 a 1"""
    switch = {
        "negro": (0,0,0),
        "rojo": (1,0,0),
        "verde": (0,1,0),
        "azul": (0,0,1),
        "cyan": (0,1,1),
        "magenta": (1,0,1),
        "amarillo": (1,1,0),
        "blanco": (1,1,1),
        "gris" : (0.5,0.5,0.5)
    }
    color_nombre = switch.get(color, "Color no definido")
    return color_nombre

def pintar_Pixel(imagen, fila, columna, color):
    imagen[fila, columna] = color_a_RGB(color) 
    print(f"Pixel ({fila},{columna}) pintado de color {color}")    

def mostrar_Imagen(imagen, titulo, cmap=None):
    plt.imshow(imagen, cmap=cmap)  
    plt.axis("off")
    plt.title(titulo)
    plt.show()

def invertir_Color(ruta):
    """Invierte los colores de una imagen"""
    img = plt.imread(ruta)
    img_invertida = 255 - img  
    return img_invertida

def canal_Rojo(ruta):
    """Toma una imagen y retorna su canal rojo."""
    img = plt.imread(ruta)
    Capa = np.copy(img) 
    Capa[:,:,1] = Capa[:,:,2] = 0 
    return Capa

def canal_Verde(ruta):
    """Toma una imagen y retorna su canal verde."""
    img = plt.imread(ruta)
    Capa = np.copy(img) 
    Capa[:,:,0] = Capa[:,:,2] = 0 
    return Capa

def canal_Azul(ruta):
    """Toma una imagen y retorna su canal azul."""
    img = plt.imread(ruta)
    Capa = np.copy(img) 
    Capa[:,:,0] = Capa[:,:,1] = 0 
    return Capa

def canal_Magenta(ruta):
    """Toma una imagen y retorna su canal magenta."""
    img = plt.imread(ruta)
    Capa = np.copy(img) 
    Capa[:,:,1] = 0 
    return Capa

def canal_Cyan(ruta):
    """Toma una imagen y retorna su canal cyan."""
    img = plt.imread(ruta)
    Capa = np.copy(img) 
    Capa[:,:,0] = 0 
    return Capa

def canal_Amarillo(ruta):
    """Toma una imagen y retorna su canal amarillo."""
    img = plt.imread(ruta)
    Capa = np.copy(img) 
    Capa[:,:,2] = 0 
    return Capa
    
def combinar_Canales(rutaR, rutaG, rutaB):
    """Toma tres imagenes y retorna una imagen con los tres canales de color combinados.""" 
    imgR = plt.imread(rutaR).astype(np.float32)
    imgG = plt.imread(rutaG).astype(np.float32)
    imgB = plt.imread(rutaB).astype(np.float32)

    imagen_combinada = imgR + imgG + imgB
    fusion = np.clip(imagen_combinada, 0 , 255).astype(np.uint8)
    return fusion 

def sumar_Imagenes(ruta1, ruta2):
    """Toma dos imagenes y retorna una imagen con la suma de las dos imagenes."""
    img1 = plt.imread(ruta1).astype(np.float32)
    img2 = plt.imread(ruta2).astype(np.float32)
    fusion = (img1 + img2)//2
    imagen_suma = np.clip(fusion, 0, 255).astype(np.uint8)
    return imagen_suma

def gris_Average(ruta):
    """Toma una imagen y retorna una imagen en blanco y negro con la tecnica Average."""
    img = plt.imread(ruta)
    img_gris_f = img.astype(np.float32)
    img_gris = ((img_gris_f[:,:,0] + img_gris_f[:,:,1] + img_gris_f[:,:,2])/3)
    img_gris = np.clip(img_gris, 0, 255).astype(np.uint8)
    return img_gris

def gris_Luminosity(ruta):
    """Toma una imagen y retorna una imagen en blanco y negro con la tecnica Luminosity."""
    img = plt.imread(ruta)
    img_gris_f = img.astype(np.float32)
    img_gris = (0.299*img_gris_f[:,:,0] + 0.587*img_gris_f[:,:,1] + 0.114*img_gris_f[:,:,2])
    img_gris = np.clip(img_gris, 0, 255).astype(np.uint8)
    return img_gris

def gris_MidGray(ruta):
    """Toma una imagen y retorna una imagen en blanco y negro con la tecnica MidGray."""
    img = plt.imread(ruta)
    img_gris_f = img.astype(np.float32)
    mx = np.max(img, axis=2)
    mn = np.min(img, axis=2)
    img_gris = (mx + mn) / 2
    img_gris = np.clip(img_gris, 0, 255).astype(np.uint8)
    return img_gris

def main():
    pass

if __name__ == "__main__":
    main()
