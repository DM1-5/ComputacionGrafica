import numpy as np
import matplotlib.pyplot as plt

def color_a_RGB(color):
    """Convierte un color a su representación RGB."""
    colores = {
        "rojo": [255, 0, 0],
        "verde": [0, 255, 0],
        "azul": [0, 0, 255],
        "magenta": [255, 0, 255],
        "cyan": [0, 255, 255],
        "amarillo": [255, 255, 0],
        "blanco"  : [255, 255, 255],
        "negro"   : [0, 0, 0],
        "gris"    : [128, 128, 128],
        "piel"  : [255, 204, 153],
        "cafe"  : [139, 69, 19],
    }
    return colores.get(color.lower(), "Color no definido")

def mostrar_Imagen(imagen, titulo, cmap=None):
    """Muestra una imagen con un título específico."""
    plt.imsave("resultado.png", imagen)
    plt.imshow(imagen, cmap=cmap)
    plt.title(titulo)
    plt.show()

def main():
    x = 15 
    y = 18
    imagen = np.full((y, x, 3), (255, 255, 255), dtype=np.uint8)
    # sombrero
    imagen[1,4:10] = color_a_RGB("rojo")
    imagen[2,3:13] = color_a_RGB("rojo")
    #cara
    imagen[3,3:6] = color_a_RGB("cafe")
    imagen[4:7,2] = color_a_RGB("cafe")
    imagen[3:6,4] = color_a_RGB("cafe")
    imagen[5,4:6] = color_a_RGB("cafe")
    imagen[6,2:4] = color_a_RGB("cafe")
    imagen[4:6,3] = color_a_RGB("piel")
    imagen[4,5] = color_a_RGB("piel")
    imagen[6:8,4:6] = color_a_RGB("piel")
    imagen[3:8,6:11] = color_a_RGB("piel")
    imagen[4:6,10:13] = color_a_RGB("piel")
    imagen[5,13] = color_a_RGB("piel")
    imagen[7,9:12] = color_a_RGB("piel")
    #ojos
    imagen[3:5,9] = color_a_RGB("negro")
    imagen[5,10] = color_a_RGB("negro")
    imagen[6,9:13] = color_a_RGB("negro")
    imagen[11:14,1:13] = color_a_RGB("piel")
    #camiza
    imagen[8,3:10] = color_a_RGB("rojo")
    imagen[10,1] = color_a_RGB("rojo")
    imagen[10,12] = color_a_RGB("rojo")
    imagen[11,3] = color_a_RGB("rojo")
    imagen[11,10] = color_a_RGB("rojo")
    imagen[9:11,2:12] = color_a_RGB("rojo")
    # pantalon
    imagen[11:14,4:10 ] = color_a_RGB("azul")
    imagen[13:15,3:6 ] = color_a_RGB("azul")
    imagen[13:15,8:11 ] = color_a_RGB("azul")
    imagen[13:15,8:11 ] = color_a_RGB("azul")
    imagen[10,5:9 ] = color_a_RGB("azul")
    imagen[8:11,5] = color_a_RGB("azul")
    imagen[9:11,8] = color_a_RGB("azul")
    imagen[11,5] = color_a_RGB("amarillo")
    imagen[11,8] = color_a_RGB("amarillo")
    #zapatos
    imagen[15:17,2:5] = color_a_RGB("cafe")
    imagen[15:17,9:12] = color_a_RGB("cafe")
    imagen[16,1] = color_a_RGB("cafe")
    imagen[16,12] = color_a_RGB("cafe")
    mostrar_Imagen(imagen, "MARIOOO")

main()