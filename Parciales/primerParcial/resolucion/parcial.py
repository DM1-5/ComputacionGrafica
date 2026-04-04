import libreria as lib
import numpy as np 
import matplotlib.pyplot as plt 
import math
from PIL import Image


def color_a_RGB_Parcial(color):
      """Convierte un color a su representación RGB."""
      colores = {
          "blanco": [255, 255, 255],
          "negro": [0, 0, 0],
          "rojo": [207, 52, 50],
          "amarillo": [254, 235, 53],
          "cyan": [0, 255, 255],
          "azul": [36, 168, 243],
          "verde"  : [80, 174, 77],
          "morado"   : [154, 42, 178],
          "naranja"    : [246, 169, 37],
          "beige"  : [254, 224, 188]
      }
      return colores.get(color.lower(), "Color no definido")

def mostrar_Imagen(imagen, titulo, cmap=None):
    """Muestra una imagen con un título específico."""
    #plt.imsave(f"{titulo}.png", imagen)
    plt.imshow(imagen, cmap=cmap)
    plt.title(titulo)
    plt.show()

def puntoUno():
    x = 17 
    y = 17
    imagen = np.full((y, x, 3), (255, 255, 255), dtype=np.uint8)
    imagen[1,5:8] = color_a_RGB_Parcial("rojo")
    imagen[2,4:6] = color_a_RGB_Parcial("rojo")
    imagen[2:7,8] = color_a_RGB_Parcial("rojo")
    imagen[7:10,5:7] = color_a_RGB_Parcial("rojo")
    imagen[5:8,7:10] = color_a_RGB_Parcial("rojo")
    imagen[10:12,6:8] = color_a_RGB_Parcial("rojo")
    imagen[12,7:9] = color_a_RGB_Parcial("rojo")
    imagen[14:16,12] = color_a_RGB_Parcial("rojo")
    imagen[7,10] = color_a_RGB_Parcial("rojo")
    imagen[2,6:8] = color_a_RGB_Parcial("beige")
    imagen[2:5,7] = color_a_RGB_Parcial("beige")
    imagen[4:6,6] = color_a_RGB_Parcial("beige")
    imagen[3,6] = color_a_RGB_Parcial("negro")
    imagen[6,5] = color_a_RGB_Parcial("beige")
    imagen[6,6] = color_a_RGB_Parcial("rojo")
    imagen[3:6,4:6] = color_a_RGB_Parcial("naranja")
    imagen[13,6:9] = color_a_RGB_Parcial("naranja")
    imagen[5,5] = color_a_RGB_Parcial("negro")
    imagen[7:10,8:10] = color_a_RGB_Parcial("amarillo")
    imagen[8:10,10] = color_a_RGB_Parcial("amarillo")
    imagen[9,11] = color_a_RGB_Parcial("amarillo")
    imagen[8,7] = color_a_RGB_Parcial("amarillo")
    imagen[9,7] = color_a_RGB_Parcial("azul")
    imagen[10:12,8] = color_a_RGB_Parcial("azul")
    imagen[12,9] = color_a_RGB_Parcial("azul")
    imagen[12:14,10:13] = color_a_RGB_Parcial("azul")
    imagen[14,11] = color_a_RGB_Parcial("azul")
    imagen[10,9:12] = color_a_RGB_Parcial("verde")
    imagen[11,11:13] = color_a_RGB_Parcial("verde")
    imagen[11,9:11] = color_a_RGB_Parcial("morado")
    imagen[12,11:13] = color_a_RGB_Parcial("morado")
    mostrar_Imagen(imagen, "PrimerPunto")

def puntoDos():
  ruta = "imagen_1.jpg"
  ruta2 = "imagen_2.png"

  img1 = plt.imread(ruta)
  img2 = plt.imread(ruta2)

  brillo1 = lib.aumentar_brillo(ruta, 50)
  mostrar_Imagen(brillo1, "Brillo aumentado +50 Imagen 1")

  brillo2 = lib.aumentar_brillo(ruta, -50)
  mostrar_Imagen(brillo2, "Brillo disminuido -50 Imagen 1")

  brillo3 = lib.aumentar_brillo(ruta2, 50)
  mostrar_Imagen(brillo3, "Brillo aumentado +50 Imagen 2")

  brillo4 = lib.aumentar_brillo(ruta2, -50)
  mostrar_Imagen(brillo4, "Brillo disminuido -50 Imagen 2")

  capaR1 = lib.canal_Rojo(ruta)
  mostrar_Imagen(capaR1, "Canal Rojo Imagen 1")

  capaR2 = lib.canal_Rojo(ruta2)
  mostrar_Imagen(capaR2, "Canal Rojo Imagen 2")

  capaM1 = lib.canal_Magenta(ruta)
  mostrar_Imagen(capaM1, "Canal Magenta Imagen 1")

  capaM2 = lib.canal_Magenta(ruta2)
  mostrar_Imagen(capaM2, "Canal Magenta Imagen 2")

  capaC1 = lib.canal_Cyan(ruta)
  mostrar_Imagen(capaC1, "Canal Cyan Imagen 1")

  capaC2 = lib.canal_Cyan(ruta2)
  mostrar_Imagen(capaC2, "Canal Cyan Imagen 2")

  gris1 = lib.gris_Luminosity(ruta)
  mostrar_Imagen(gris1, "Gris Luminosity Imagen 1", cmap="gray")
  
  gris2 = lib.gris_Luminosity(ruta2)
  mostrar_Imagen(gris2, "Gris Luminosity Imagen 2", cmap="gray")


puntoUno()
#puntoDos()