import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2

from img_pro import aumentar_brillo

imagen = None
imagen_original = None


def abrir_imagen():
    global imagen, imagen_original

    ruta = filedialog.askopenfilename(
        filetypes=[("Imágenes", "*.jpg *.jpeg *.png")]
    )

    if ruta:
        imagen = cv2.imread(ruta, cv2.IMREAD_UNCHANGED)
        imagen_original = imagen.copy()

        slider.set(0)
        entrada.delete(0, tk.END)
        entrada.insert(0, "0")

        mostrar_imagen()


def mostrar_imagen():
    if imagen is None:
        return

    if len(imagen.shape) == 3:
        img_rgb = cv2.cvtColor(imagen[:, :, :3], cv2.COLOR_BGR2RGB)
    else:
        img_rgb = cv2.cvtColor(imagen, cv2.COLOR_GRAY2RGB)

    img_pil = Image.fromarray(img_rgb)
    img_pil = img_pil.resize((400, 300))

    img_tk = ImageTk.PhotoImage(img_pil)
    lbl_imagen.config(image=img_tk)
    lbl_imagen.image = img_tk


def aplicar_desde_boton():
    global imagen

    if imagen_original is None:
        messagebox.showwarning("Aviso", "Primero abre una imagen")
        return

    try:
        valor = int(entrada.get())  # Se deberá convertir a tipo entero 
        valor = max(-100, min(100, valor)) # Se deberá convertir a tipo entero 

        slider.set(valor)
        imagen = aumentar_brillo(imagen_original.copy(), valor)
        mostrar_imagen()

    except ValueError:
        messagebox.showerror("Error", "Ingresa un número válido")


def aplicar_desde_slider(valor):
    global imagen

    if imagen_original is None:
        return

    valor = int(valor)

    entrada.delete(0, tk.END)
    entrada.insert(0, str(valor))

    imagen = aumentar_brillo(imagen_original.copy(), valor)
    mostrar_imagen()


def resetear():
    global imagen

    if imagen_original is None:
        return

    imagen = imagen_original.copy()
    slider.set(0)
    entrada.delete(0, tk.END)
    entrada.insert(0, "0")
    mostrar_imagen()

# Construccion de la ventana
ventana = tk.Tk()
ventana.title("Brillo de imagen")
ventana.geometry("520x500")

btn_abrir = tk.Button(ventana, text="Abrir imagen", command=abrir_imagen)
btn_abrir.pack(pady=10)

entrada = tk.Entry(ventana, width=10)
entrada.pack()
entrada.insert(0, "0") # Establece el valor predeterminado de la caja de texto en 0 

btn_aplicar = tk.Button(ventana, text="Aplicar brillo", 
                        command=aplicar_desde_boton)
btn_aplicar.pack(pady=5)

btn_reset = tk.Button(ventana, text="Resetear", command=resetear)
btn_reset.pack(pady=5)

slider = tk.Scale(
    ventana,
    from_=-100,
    to=100,
    orient="horizontal",
    length=300,
    label="Brillo",
    command=aplicar_desde_slider
)
slider.pack(pady=10)

lbl_imagen = tk.Label(ventana)
lbl_imagen.pack(pady=10)

ventana.mainloop()




