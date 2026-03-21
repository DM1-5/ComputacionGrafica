import customtkinter
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2

from img_pro import aumentar_brillo


customtkinter.set_default_color_theme("blue")
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
        entrada.delete(0, "end")
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

    entrada.delete(0, "end")
    entrada.insert(0, str(valor))

    imagen = aumentar_brillo(imagen_original.copy(), valor)
    mostrar_imagen()


def resetear():
    global imagen

    if imagen_original is None:
        return

    imagen = imagen_original.copy()
    slider.set(0)
    entrada.delete(0, "end")
    entrada.insert(0, "0")
    mostrar_imagen()


ventana = customtkinter.CTk()
ventana.title("Brillo de imagen")
ventana.geometry("520x500")

btn_abrir = customtkinter.CTkButton(ventana, text="Abrir imagen", command=abrir_imagen)
btn_abrir.pack(pady=10)

entrada = customtkinter.CTkEntry(ventana, width=100)
entrada.pack()
entrada.insert(0, "0") # Establece el valor predeterminado de la caja de texto en 0 

btn_aplicar = customtkinter.CTkButton(ventana, text="Aplicar brillo", command=aplicar_desde_boton)
btn_aplicar.pack(pady=5)

btn_reset = customtkinter.CTkButton(ventana, text="Resetear", command=resetear)
btn_reset.pack(pady=5)

slider = customtkinter.CTkSlider(
    ventana,
    from_=-100,
    to=100,
    number_of_steps=201,
    command=aplicar_desde_slider
)
slider.set(0)
slider.pack(pady=10, padx=20)

lbl_imagen = customtkinter.CTkLabel(ventana, text="")
lbl_imagen.pack(pady=10)

ventana.mainloop()




