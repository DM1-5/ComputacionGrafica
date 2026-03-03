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

def punto_Uno():
    """Crea una imagen de 3x3 y se le agrega color a cada pixel"""
    img = np.zeros((3,3,3))
    pintar_Pixel(img, 0, 0, "cyan") 
    pintar_Pixel(img, 0, 1, "blanco") 
    pintar_Pixel(img, 0, 2, "rojo") 
    pintar_Pixel(img, 1, 0, "magenta") 
    pintar_Pixel(img, 1, 1, "gris") 
    pintar_Pixel(img, 1, 2, "verde") 
    pintar_Pixel(img, 2, 0, "amarillo")
    pintar_Pixel(img, 2, 1, "negro") 
    pintar_Pixel(img, 2, 2, "azul") 
    return img
    
def punto_Dos():
    """ Crea una imagen de 7x11 se le agrega color"""
    img = np.zeros((7,11,3))

    img[:5,0] = color_a_RGB("amarillo")
    img[:5,1:3] = color_a_RGB("cyan")
    img[:5,3:5] = color_a_RGB("verde")
    img[:5,5:7] = color_a_RGB("magenta")
    img[:5,7:9] = color_a_RGB("rojo")
    img[:5,9:11] = color_a_RGB("azul")

    x = np.linspace(0.9, 0, 11)

    for i in range(img.shape[1]):
        img[5:,i] = x[i]

    return img

def punto_Tres(ruta):
    """Invierte los colores de una imagen"""
    img = plt.imread(ruta)
    img_invertida = 255 - img  
    return img_invertida

def punto_Cuatro(ruta):
    """Toma una imagen y retorna su canal rojo."""
    img = plt.imread(ruta)
    Capa = np.copy(img) 
    Capa[:,:,1] = Capa[:,:,2] = 0 
    return Capa

def punto_Cinco(ruta):
    """Toma una imagen y retorna su canal verde."""
    img = plt.imread(ruta)
    Capa = np.copy(img) 
    Capa[:,:,0] = Capa[:,:,2] = 0 
    return Capa

def punto_Seis(ruta):
    """Toma una imagen y retorna su canal azul."""
    img = plt.imread(ruta)
    Capa = np.copy(img) 
    Capa[:,:,0] = Capa[:,:,1] = 0 
    return Capa

def punto_Siete(ruta):
    """Toma una imagen y retorna su canal magenta."""
    img = plt.imread(ruta)
    Capa = np.copy(img) 
    Capa[:,:,1] = 0 
    return Capa

def punto_Ocho(ruta):
    """Toma una imagen y retorna su canal cyan."""
    img = plt.imread(ruta)
    Capa = np.copy(img) 
    Capa[:,:,0] = 0 
    return Capa

def punto_Nueve(ruta):
    """Toma una imagen y retorna su canal amarillo."""
    img = plt.imread(ruta)
    Capa = np.copy(img) 
    Capa[:,:,2] = 0 
    return Capa
    

def punto_Diez(rutaR, rutaG, rutaB):
    """Toma tres imagenes y retorna una imagen con los tres canales de color combinados.""" 
    imgR = plt.imread(rutaR).astype(np.float32)
    imgG = plt.imread(rutaG).astype(np.float32)
    imgB = plt.imread(rutaB).astype(np.float32)

    imagen_combinada = imgR + imgG + imgB
    fusion = np.clip(imagen_combinada, 0 , 255).astype(np.uint8)
    return fusion 

def punto_Once(ruta1, ruta2):
    """Toma dos imagenes y retorna una imagen con la suma de las dos imagenes."""
    img1 = plt.imread(ruta1).astype(np.float32)
    img2 = plt.imread(ruta2).astype(np.float32)
    fusion = (img1 + img2)//2
    imagen_suma = np.clip(fusion, 0, 255).astype(np.uint8)
    return imagen_suma


def punto_Doce(ruta):
    """Toma una imagen y retorna una imagen en blanco y negro con la tecnica Average."""
    img = plt.imread(ruta)
    img_gris_f = img.astype(np.float32)
    img_gris = ((img_gris_f[:,:,0] + img_gris_f[:,:,1] + img_gris_f[:,:,2])/3)
    img_gris = np.clip(img_gris, 0, 255).astype(np.uint8)
    return img_gris

def punto_Trece(ruta):
    """Toma una imagen y retorna una imagen en blanco y negro con la tecnica Luminosity."""
    img = plt.imread(ruta)
    img_gris_f = img.astype(np.float32)
    img_gris = (0.299*img_gris_f[:,:,0] + 0.587*img_gris_f[:,:,1] + 0.114*img_gris_f[:,:,2])
    img_gris = np.clip(img_gris, 0, 255).astype(np.uint8)
    return img_gris

def punto_Catorce(ruta):
    """Toma una imagen y retorna una imagen en blanco y negro con la tecnica MidGray."""
    img = plt.imread(ruta)
    img_gris_f = img.astype(np.float32)
    mx = np.max(img, axis=2)
    mn = np.min(img, axis=2)
    img_gris = (mx + mn) / 2
    img_gris = np.clip(img_gris, 0, 255).astype(np.uint8)
    return img_gris

def main():
    # mostrar_Imagen(punto_Uno(), "Ejercicio 1")
    # mostrar_Imagen(punto_Dos(), "Ejercicio 2")
    # mostrar_Imagen(punto_Tres("datos.jpg"), "Ejercicio 3")

    # mostrar_Imagen(punto_Cuatro("datos.jpg"), "Canal rojo")
    # mostrar_Imagen(punto_Cinco("datos.jpg"), "Canal verde") 
    # mostrar_Imagen(punto_Seis("datos.jpg"), "Canal azul") 
    # mostrar_Imagen(punto_Siete("datos.jpg"), "Canal magenta") 
    # mostrar_Imagen(punto_Ocho("datos.jpg"), "Canal cyan") 
    # mostrar_Imagen(punto_Nueve("datos.jpg"), "Canal amarillo") 

    # mostrar_Imagen(punto_Diez("datosR.jpg", "datosG.jpg", "datosB.jpg"), "Imagen combinada")
    #  !!! Se guarda como datosRGB.jpg la imagen correctamente combinada.  !!!
    # !!! La imagen datosUnida-Incorrectamente.jpg muestra lo que puede pasar si no se realizan las 
    # conversiones necesarias antes de realizar la suma de arrays. !!!

    # mostrar_Imagen(punto_Once("fondo1.jpg", "fondo2.jpg"), "Union de imagenes")
    # mostrar_Imagen(punto_Doce("nasa.jpg"), "Blanco&Negro (Average)", cmap="gray")
    # mostrar_Imagen(punto_Trece("nasa.jpg"), "Blanco&Negro (Luminosity)", cmap="gray")
    # mostrar_Imagen(punto_Catorce("nasa.jpg"), "Blanco&Negro (MidGray)", cmap="gray")
    pass

if __name__ == "__main__":
    main()
