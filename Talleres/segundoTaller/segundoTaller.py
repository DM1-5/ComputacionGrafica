import numpy as np 
import matplotlib.pyplot as plt 
import math

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
    imagen[fila, columna] = color_a_RGB(color) # El color es una tupla con los valores de intensidad de los canales de color (R,G,B) en el rango de 0 a 1.
    print(f"Pixel ({fila},{columna}) pintado de color {color}")    

def punto_Uno():
    """Crea una imagen de 3x3"""
    ejercicio1 = np.zeros((3,3,3))
    # crea un arreglo de 3 dimensiones con 3 filas, 3 columnas y 3 canales de color (RGB), lleno de unos.

    # Pixel 0,0

    #ejercicio1[0,0,0] = 0 
    #ejercicio1[0,0,1] = 1 
    #ejercicio1[0,0,2] = 1 
    pintar_Pixel(ejercicio1, 0, 0, "cyan") # Pinta el pixel (0,0) de color cyan (R=0,G=1,B=1)

    # Pixel 0,1
    #ejercicio1[0,1,0] = 1
    #ejercicio1[0,1,1] = 1
    #ejercicio1[0,1,2] = 1

    pintar_Pixel(ejercicio1, 0, 1, "blanco") # Pinta el pixel (0,1) de color blanco (R=1,G=1,B=1)
    
    # Pixel 0,2
    #ejercicio1[0,2,0] = 1
    #ejercicio1[0,2,1] = 0
    #ejercicio1[0,2,2] = 0

    pintar_Pixel(ejercicio1, 0, 2, "rojo") # Pinta el pixel (0,2) de color rojo (R=1,G=0,B=0)

    # Pixel 1,0
    #ejercicio1[1,0,0] = 1
    #ejercicio1[1,0,1] = 0
    #ejercicio1[1,0,2] = 1

    pintar_Pixel(ejercicio1, 1, 0, "magenta") # Pinta el pixel (1,0) de color magenta (R=1,G=0,B=1)

    # pixel 1,1
    #ejercicio1[1,1,0] = 0.5
    #ejercicio1[1,1,1] = 0.5
    #ejercicio1[1,1,2] = 0.5

    pintar_Pixel(ejercicio1, 1, 1, "gris") # Pinta el pixel (1,1) de color gris (R=0.5,G=0.5,B=0.5)
    # Pixel 1,2
    #ejercicio1[1,2,0] = 0
    #ejercicio1[1,2,1] = 1
    #ejercicio1[1,2,2] = 0

    pintar_Pixel(ejercicio1, 1, 2, "verde") # Pinta el pixel (1,2) de color verde (R=0,G=1,B=0)

    # Pixel 2,0 Amarillo 
    # ejercicio1[2,0,0] = 1
    # ejercicio1[2,0,1] = 1
    # ejercicio1[2,0,2] = 0

    pintar_Pixel(ejercicio1, 2, 0, "amarillo") # Pinta el pixel (2,0) de color amarillo (R=1,G=1,B=0)


    # #Pixel 2,1 Negro
    # ejercicio1[2,1,0] = 0
    # ejercicio1[2,1,1] = 0
    # ejercicio1[2,1,2] = 0

    pintar_Pixel(ejercicio1, 2, 1, "negro") # Pinta el pixel (2,1) de color negro (R=0,G=0,B=0)


    # # Pixel 2,2 
    # ejercicio1[2,2,0] = 0
    # ejercicio1[2,2,1] = 0
    # ejercicio1[2,2,2] = 1

    pintar_Pixel(ejercicio1, 2, 2, "azul") # Pinta el pixel (2,2) de color azul (R=0,G=0,B=1)

    plt.imshow(ejercicio1)  
    plt.axis("off")
    plt.title("Ejercicio 1")
    plt.show()



def punto_Dos():
    """ Crea una imagen de 7x11"""
    ejercicio2 = np.zeros((7,11,3))
    # crea un arreglo de 3 dimensiones con 7 filas, 11 columnas y 3 canales de color (RGB), lleno de ceros.
    
    ejercicio2[:5,0] = color_a_RGB("amarillo") # Amarillo de la fila 0 a la 4 en la columna 0.

    ejercicio2[:5,1:3] = color_a_RGB("cyan")

    ejercicio2[:5,3:5] = color_a_RGB("verde")

    ejercicio2[:5,5:7] = color_a_RGB("magenta")

    ejercicio2[:5,7:9] = color_a_RGB("rojo")

    ejercicio2[:5,9:11] = color_a_RGB("azul")

    x = np.linspace(0.9, 0, 11)

    for i in range(ejercicio2.shape[1]):
        ejercicio2[5:,i] = x[i]

    plt.imshow(ejercicio2)  
    plt.axis("off")
    plt.title("Ejercicio 2")
    plt.show()




punto_Dos()
#punto_Uno()
#7x11 6x8