import numpy as np 
import matplotlib.pyplot as plt 
import math
from PIL import Image
from pathlib import Path

def es_jpg(img):
    """Verifica si una imagen es del tipo JPG. Retorna True si es JPG, False si no lo es."""
    #print(f"La imagen es de tipo {img.dtype}, tiene una longitud de {len(img.shape)} y su forma es {img.shape}")
    if img.dtype == np.uint8 and img.shape[2] == 3:
        print("La imagen es del tipo JPG")
        return True
    else:  
        print("La imagen es del tipo JPG")
        return False

def es_png(img):
    """Verifica si una imagen es del tipo PNG. Retorna True si es PNG, False si no lo es."""
    #print(f"La imagen es de tipo {img.dtype}, tiene una longitud de {len(img.shape)} y su forma es {img.shape}")
    if img.dtype == np.float32 and img.shape[2] == 4:
        print("La imagen es del tipo PNG")
        return True
    else:  
        print("La imagen no es del tipo PNG")
        return False

def es_igual(img1, img2):
    """Verifica si dos imágenes son iguales en formato y tamaño. retorna una tupla (formato, tamaño)"""
    print(f"La imagen 1 es de tipo {img1.dtype}, tiene una longitud de {len(img1.shape)} y su forma es {img1.shape}")
    print(f"La imagen 2 es de tipo {img2.dtype}, tiene una longitud de {len(img2.shape)} y su forma es {img2.shape}")
    formato = False 
    tamaño = False
    # Agregar una respuesta en forma de tupla
    if img1.dtype == img2.dtype:
        formato = True
    if img1.shape == img2.shape:
        tamaño = True
    print(f"Formato: {formato}, Tamaño: {tamaño}")
    return (formato, tamaño)

def color_a_RGB(color, img):
    """Convierte un color a su representación RGB en el rango de 0 a 1"""
    switch_png = {
        "negro":    (0,0,0),
        "rojo":     (1,0,0),
        "verde":    (0,1,0),
        "azul":     (0,0,1),
        "cyan":     (0,1,1),
        "magenta":  (1,0,1),
        "amarillo": (1,1,0),
        "blanco":   (1,1,1),
        "gris" :    (0.5,0.5,0.5)
    }
    
    switch_jpg = {
        "rojo":     [255, 0, 0],
        "verde":    [0, 255, 0],
        "azul":     [0, 0, 255],
        "magenta":  [255, 0, 255],
        "cyan":     [0, 255, 255],
        "amarillo": [255, 255, 0],
        "blanco"  : [255, 255, 255],
        "negro"   : [0, 0, 0],
        "gris"    : [128, 128, 128],
        "piel"  :   [255, 204, 153],
        "cafe"  :   [139, 69, 19]
    }

    if es_jpg(img):
        color_nombre = switch_jpg.get(color.lower(), "Color no definido")
    elif es_png(img):
        color_nombre = switch_png.get(color.lower(), "Color no definido")
    else:
        color_nombre = "Formato de imagen no soportado"
        return None

    return color_nombre

def pintar_Pixel(imagen, fila, columna, color):
    """Pinta un pixel de una imagen con un color dado"""
    imagen[fila, columna] = color_a_RGB(color, imagen) 
    print(f"Pixel ({fila},{columna}) pintado de color {color}")    

def mostrar_Imagen(imagen, titulo, cmap=None):
    """Muestra una imagen con un título dado."""
    plt.imshow(imagen, cmap=cmap)  
    plt.axis("off")
    plt.title(titulo)
    plt.show()

def guardar_Imagen(imagen, ruta):
    """Guarda una imagen en la ruta especificada."""
    plt.imsave(ruta, imagen)

def aumentar_brillo(ruta, valor):
    """Toma una ruta de imagen y un valor de brillo a aumentar, retorna la imagen con el brillo aumentado."""
    imagen = plt.imread(ruta)
    if es_jpg(imagen):
        imgf = imagen.astype(np.float32)
        img_clip = (np.clip(imgf + valor, 0 , 255)).astype(np.uint8) 
    else:  
        img_clip = np.clip(imagen + valor/255.0, 0 , 1) 
    return img_clip 

# Mas adelante se podria implementar una funcion que traduzca el canal de un string a su indice.
def aumentar_brillo_Canal(ruta, valor, canal):
    """Toma una ruta de imagen, un valor de brillo a aumentar y un canal, retorna la imagen con el brillo aumentado en ese canal."""
    img = plt.imread(ruta)
    canal = int(canal) # Convertir el canal a entero, ya que se recibe como string desde la interfaz de gradio.
    if es_jpg(img):
        imgf = img.astype(np.float32)
        img_clip = img.copy()
        img_clip[:,:,canal] = (np.clip(imgf[:,:,canal] + valor, 0 , 255)).astype(np.uint8)
    elif es_png(img):  
        img_clip = img.copy()
        img_clip[:,:,canal] = np.clip(img[:,:,canal] + valor/255.0, 0 , 1)
    return img_clip 

def invertir_Color(ruta):
    """Toma una ruta de imagen y retorna la imagen invertida."""
    img = plt.imread(ruta)
    if es_jpg(img):
        img_invertida = 255 - img  
    else:
        img_invertida = 1 - img[:,:,:3] # pilas con el canal alpha.
    return img_invertida

def canal_Rojo(ruta):
    """Toma una ruta de imagen y retorna su canal rojo."""
    img = plt.imread(ruta)
    Capa = np.copy(img) 
    Capa[:,:,1] = Capa[:,:,2] = 0 
    return Capa

def canal_Verde(ruta):
    """Toma una ruta de imagen y retorna su canal verde."""
    img = plt.imread(ruta)
    Capa = np.copy(img) 
    Capa[:,:,0] = Capa[:,:,2] = 0 
    return Capa

def canal_Azul(ruta):
    """Toma una ruta de imagen y retorna su canal azul."""
    img = plt.imread(ruta)
    Capa = np.copy(img) 
    Capa[:,:,0] = Capa[:,:,1] = 0 
    return Capa

def canal_Magenta(ruta):
    """Toma una ruta de imagen y retorna su canal magenta."""
    img = plt.imread(ruta)
    Capa = np.copy(img) 
    Capa[:,:,1] = 0 
    return Capa

def canal_Cyan(ruta):
    """Toma una ruta de imagen y retorna su canal cyan."""
    img = plt.imread(ruta)
    Capa = np.copy(img) 
    Capa[:,:,0] = 0 
    return Capa

def canal_Amarillo(ruta):
    """Toma una ruta de imagen y retorna su canal amarillo."""
    img = plt.imread(ruta)
    Capa = np.copy(img) 
    Capa[:,:,2] = 0 
    return Capa

# verificar si las imagenes son del mismo tipo.
def combinar_Canales(rutaR, rutaG, rutaB):
    """Toma tres imagenes y retorna una imagen con los tres canales de color combinados.""" 

    imgR = plt.imread(rutaR)
    imgG = plt.imread(rutaG)
    imgB = plt.imread(rutaB)

    formato_rg, tamaño_rg = es_igual(imgR, imgG)
    formato_rb, tamaño_rb = es_igual(imgR, imgB)
    formato_gb, tamaño_gb = es_igual(imgG, imgB)

    if not (formato_rg and formato_rb and formato_gb):
        print("Las imagenes no son del mismo formato, no se pueden combinar.")
        return None

    if not (tamaño_rg and tamaño_rb and tamaño_gb):
        print("Las imagenes no son del mismo tamaño, no se pueden combinar.")
        return None

    if es_jpg(imgR) and es_jpg(imgG) and es_jpg(imgB):
        print("Todas las imagenes son de tipo uint8")
        imgR = imgR.astype(np.float32)
        imgG = imgG.astype(np.float32)
        imgB = imgB.astype(np.float32)

        imagen_combinada = imgR + imgG + imgB
        fusion = np.clip(imagen_combinada, 0 , 255).astype(np.uint8)
    else:
        print("Las imagenes son de tipo float32") 
        imagen_combinada = imgR + imgG + imgB
        fusion = np.clip(imagen_combinada, 0 , 1).astype(np.float32)

    return fusion

# Helper: asegurar que la imagen sea RGB uint8 (PIL requiere tipos manejables)
def to_rgb_uint8(img):
    # Si la imagen es 2D (escala de grises), replicar canales a RGB
    if img.ndim == 2:
        img = np.stack([img] * 3, axis=2)

    # Si tiene más de 3 canales (ej. RGBA), descartar canales extras (mantener RGB)
    if img.shape[2] > 3:
        img = img[:, :, :3]

    # Si el array es de punto flotante, convertir a uint8 en rango [0,255]
    if img.dtype.kind == "f":
        # Si los valores están en [0,1], escalarlos; si ya están en [0,255], recortarlos
        if img.max() <= 1.0:
            img = (np.clip(img, 0, 1) * 255).astype(np.uint8)
        else:
            img = np.clip(img, 0, 255).astype(np.uint8)
    else:
        # Si no es float, castear a uint8 (por ejemplo uint16 -> uint8)
        img = img.astype(np.uint8)

    return img

# Verificar si las imagenes son del mismo tipo.
def sumar_Imagenes_nofunciona(ruta1, ruta2):
    """Toma dos imagenes y retorna una imagen con la suma de las dos imagenes."""

    img1 = plt.imread(ruta1)
    img2 = plt.imread(ruta2)

    formato, tamaño = es_igual(img1, img2)
    img1 = to_rgb_uint8(img1)
    img2 = to_rgb_uint8(img2)

    h,w, _ = img2.shape
    print("Las imagenes no son del mismo tamaño, se redimensionará la imagen mas grande a la imagen mas pequeña para poder sumarlas.")
    print(f"Imagen2 = h: {h}, w: {w}")
    # Esta funcion al parecer solo redimensiona si las dos son jpg. 
    img1 = np.array(Image.fromarray(img1).resize((w,h))) 
    h,w, _ = img1.shape
    print(f"Imagen1 = h: {h}, w: {w}")

    formato, tamaño = es_igual(img1, img2)
    print(f"Formato: {formato}, Tamaño: {tamaño}")

    # if not formato:
    #     print("Las imagenes no son del mismo formato, no se pueden sumar.")
    #     return None
    # if not tamaño:
    #     h,w, _ = img2.shape
    #     print("Las imagenes no son del mismo tamaño, se redimensionará la imagen mas grande a la imagen mas pequeña para poder sumarlas.")
    #     img1 = np.array(Image.fromarray(img1).resize((w,h))) 
    #     formato, tamaño = es_igual(img1, img2)
    #     print(f"Formato: {formato}, Tamaño: {tamaño}")

    fusion = (img1.astype(np.float32) + img2.astype(np.float32))//2

    print("Las imagenes se exportarán de tipo uint8")
    imagen_suma = np.clip(fusion, 0, 255).astype(np.uint8)
    # if es_jpg(img1) and es_jpg(img2):
    #     print("Las imagenes son de tipo uint8")
    #     imagen_suma = np.clip(fusion, 0, 255).astype(np.uint8)
    # else:
    #     print("Las imagenes son de tipo float32")
    #     imagen_suma = np.clip(fusion, 0, 1).astype(np.float32)

    return imagen_suma

def sumar_Imagenes(ruta1, ruta2, alpha):
    """Toma dos imagenes y retorna una imagen con la suma de las dos imagenes."""
    
    # Cargar imágenes con matplotlib (puede devolver float32 en [0,1] o uint8 en [0,255])
    img1 = plt.imread(ruta1)
    img2 = plt.imread(ruta2)

    # Normalizar ambas imágenes a RGB uint8
    a = to_rgb_uint8(img1)
    b = to_rgb_uint8(img2)

    # Redimensionar 'a' para que coincida con el tamaño de 'b'
    h, w = b.shape[:2]

    # Esta funcion al parecer solo redimensiona si las dos son jpg.
    a_resized = np.array(Image.fromarray(a).resize((w, h)))

    fusion_f = alpha * a_resized.astype(np.float32) + (1 - alpha) * b.astype(np.float32)
    imagen_suma = np.clip(fusion_f, 0, 255).astype(np.uint8)

    return imagen_suma

def sumar_Imagenes_Ponderada(ruta1, ruta2, alpha):
    """Toma dos imagenes y retorna una imagen con la suma de las dos imagenes."""

    img1 = plt.imread(ruta1)
    img2 = plt.imread(ruta2)

    formato, tamaño = es_igual(img1, img2)

    if not formato:
        print("Las imagenes no son del mismo formato, no se pueden sumar.")
        return None
    if not tamaño:
        print("Las imagenes no son del mismo tamaño, no se pueden sumar.") # Luego de verificar el formato, se podria redimensionar la imagen mas grande a la imagen mas pequeña para poder sumarlas.
        return None

    fusion = alpha * img1.astype(np.float32) + (1 - alpha) * img2.astype(np.float32)

    if es_jpg(img1) and es_jpg(img2):
        print("Las imagenes son de tipo uint8")
        imagen_suma = np.clip(fusion, 0, 255).astype(np.uint8)
    else:
        print("Las imagenes son de tipo float32")
        imagen_suma = np.clip(fusion, 0, 1).astype(np.float32)

    return imagen_suma


def gris_Average(ruta):
    """Toma una imagen y retorna una imagen en blanco y negro con la tecnica Average."""
    img = plt.imread(ruta)
    img_gris_f = img.astype(np.float32)
    img_gris = ((img_gris_f[:,:,0] + img_gris_f[:,:,1] + img_gris_f[:,:,2])/3)
    if es_jpg(img):
        img_gris = np.clip(img_gris, 0, 255).astype(np.uint8)
    else:
        img_gris = np.clip(img_gris, 0, 1).astype(np.float32)
    return img_gris

def gris_Luminosity(ruta):
    """Toma una imagen y retorna una imagen en blanco y negro con la tecnica Luminosity."""
    img = plt.imread(ruta)
    img_gris_f = img.astype(np.float32)
    img_gris = (0.299*img_gris_f[:,:,0] + 0.587*img_gris_f[:,:,1] + 0.114*img_gris_f[:,:,2])
    if es_jpg(img):
        img_gris = np.clip(img_gris, 0, 255).astype(np.uint8)
    else:
        img_gris = np.clip(img_gris, 0, 1).astype(np.float32)
    return img_gris

def gris_MidGray(ruta):
    """Toma una imagen y retorna una imagen en blanco y negro con la tecnica MidGray."""
    img = plt.imread(ruta)
    img_gris_f = img.astype(np.float32)
    mx = np.max(img, axis=2)
    mn = np.min(img, axis=2)
    img_gris = (mx + mn) / 2

    if es_jpg(img):
        img_gris = np.clip(img_gris, 0, 255).astype(np.uint8)
    else:
        img_gris = np.clip(img_gris, 0, 1).astype(np.float32)
    return img_gris


# el umbral está dado en el rango de 0 a 255 para imágenes JPG, 
# para calcular el umbral para imágenes PNG, se divide el umbral entre 255.
def binarizar(ruta, umbral): 
    """Toma una ruta de imagen y un umbral, retorna la imagen binarizada."""
    img_gris = gris_Luminosity(ruta)
    if img_gris.dtype == np.uint8:
        imgf = img_gris.astype(np.float32)
        img_binaria = np.where(imgf >= umbral, 255, 0).astype(np.uint8)
    elif img_gris.dtype == np.float32:
        img_binaria = np.where(img_gris >= umbral/255.0, 1, 0).astype(np.float32)
    else:
        print("Formato de imagen no reconocido") # Implementar un try-catch para manejar errores.
        exit(1)
    return img_binaria

def traslacion(ruta, dx, dy):
    """Toma una ruta de imagen y desplazamientos dx y dy, retorna la imagen trasladada."""
    img = plt.imread(ruta)
    h, w = img.shape[:2]
    trasladada = np.zeros_like(img)
    x1d = max(0, dx)
    y1d = max(0, dy)
    x2d = min(w, w + dx)
    y2d = min(h, h + dy)

    x1s = max(0, -dx)
    y1s = max(0,-dy)
    x2s = x1s + (x2d - x1d)
    y2s = y1s + (y2d - y1d)
    
    if x2d > x1d and y2d > y1d: 
        trasladada[y1d:y2d, x1d:x2d] = img[y1s:y2s, x1s:x2s]

    return trasladada

def recorte(ruta, xini, xfin, yini, yfin):
    """Toma una ruta de imagen y coordenadas de recorte, retorna la imagen recortada."""
    img = plt.imread(ruta)
    recorte = img[yini:yfin, xini:xfin]
    return recorte

def reduccion_Resolucion(ruta, factor):
    """Toma una ruta de imagen y un factor de reducción, retorna la imagen con resolución reducida."""
    img = plt.imread(ruta)
    reducida = img[::factor, ::factor]
    return reducida

def rotar(ruta, angulo):
    """Toma una ruta de imagen y un ángulo en grados, retorna la imagen rotada."""
    img = Image.open(ruta)
    rotada = img.rotate(angulo, expand=True)  # usa PIL
    return np.array(rotada)

def zoom(ruta, zoom, zoom_factor):
    """Toma una ruta de imagen, un tamaño de zoom y un factor de zoom, retorna la imagen con zoom aplicado."""
    img = plt.imread(ruta)
    h, w = img.shape[:2]
    start_row = h // 2 - zoom // 2
    end_row = h // 2 + zoom // 2
    start_col = w // 2 - zoom // 2
    end_col = w // 2 + zoom // 2
    recorte = img[start_row:end_row, start_col:end_col]
    
    zoomed = np.kron(recorte, np.ones((zoom_factor, zoom_factor, 1)))
    zoomed = zoomed.astype(img.dtype)
    return zoomed

def histograma(ruta, canal):
    from io import BytesIO
    ruta = Path(ruta)
    img = plt.imread(ruta)
    if img.ndim == 2:
        img = np.stack([img]*3, axis=2)
    if img.shape[2] > 3:
        img = img[:, :, :3]
    if img.max() <= 1.0:
        img_u8 = (img * 255).astype(np.uint8)
    else:
        img_u8 = img.astype(np.uint8)

    idx = {"rojo":0, "verde":1, "azul":2}.get(canal)
    if idx is None:
        raise ValueError('canal debe ser "rojo","verde" o "azul"')

    data = img_u8[:,:,idx].ravel()
    color = {"rojo":"red","verde":"green","azul":"blue"}[canal]

    fig, ax = plt.subplots(figsize=(4,2), dpi=360)
    ax.hist(data, bins=256, color=color, range=(0,255))
    ax.set_xlim(0,255)
    fig.tight_layout(pad=0)

    buf = BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight", pad_inches=0)
    buf.seek(0)
    arr = np.array(Image.open(buf).convert("RGB"))
    plt.close(fig)
    return arr

def main():
    BASE = Path(__file__).parent # Ruta del directorio actual del archivo .py
    #imagen = "datos.png"
    imagen = "1080.png"
    imagen2 = "720.png"

    ruta = BASE.parent.parent / "Imagenes" / imagen # Ruta del archivo de imagen, que se encuentra en el directorio "Imagenes" que esta en el mismo nivel que el directorio "Clases".
    ruta2 = BASE.parent.parent / "Imagenes" / imagen2
    img = plt.imread(ruta)

    
    #img2 = plt.imread(ruta2)
    
    res = sumar_Imagenes(ruta, ruta2, 0.5)
    mostrar_Imagen(res, "Suma")
    #histograma(ruta, "rojo")


if __name__ == "__main__":
    main()
