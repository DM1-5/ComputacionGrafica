import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def abrir_imagen():
    ruta = filedialog.askopenfilename(
    title="Seleccionar imagen", 
     filetypes=[("Archivos de imagen", "*.jpg;*.jpeg;*.png;*.bmp")]
     )
    if ruta:

        img = Image.open(ruta)
        img.thumbnail((400, 400))
        img_tk = ImageTk.PhotoImage(img)

        etiqueta_imagen.config(image=img_tk)
        etiqueta_imagen.image = img_tk

ventana = tk.Tk()
ventana.title("Abrir Imagen con Tkinter")
ventana.geometry("500x500")

boton = tk.Button(
        ventana,
        text="Abrir Imagen",
        command=abrir_imagen
    )
boton.pack(pady=20)

etiqueta_imagen = tk.Label(ventana)
etiqueta_imagen.pack()

ventana.mainloop()
