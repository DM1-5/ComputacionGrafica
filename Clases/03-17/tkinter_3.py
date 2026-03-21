import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np

from img_pro import capa_r, capa_g, capa_b, capa_c, capa_m, capa_y

imagen = None
img_tk = None


def abrir_imagen():
    global imagen

    ruta = filedialog.askopenfilename(
        filetypes=[("Imagenes", "*.jpg *.png *.jpeg")]
    )

    if ruta:
        imagen = Image.open(ruta).convert("RGB")
        mostrar(imagen)


def mostrar(img):
    global img_tk

    copia = img.copy()
    copia.thumbnail((300, 300))

    img_tk = ImageTk.PhotoImage(copia)
    label_imagen.config(image=img_tk)


def procesar():
    if imagen is None:
        return

    img = np.array(imagen)

    if var_r.get():
        resultado = capa_r(img)
    elif var_g.get():
        resultado = capa_g(img)
    elif var_b.get():
        resultado = capa_b(img)
    elif var_c.get():
        resultado = capa_c(img)
    elif var_m.get():
        resultado = capa_m(img)
    elif var_y.get():
        resultado = capa_y(img)
    else:
        return

    mostrar(Image.fromarray(resultado))


root = tk.Tk()
root.title("Capas RGB y CMY")
root.geometry("400x450")

boton_abrir = tk.Button(root, text="Abrir imagen", command=abrir_imagen)
boton_abrir.pack(pady=10)

label_imagen = tk.Label(root)
label_imagen.pack(pady=10)

var_r = tk.BooleanVar()
var_g = tk.BooleanVar()
var_b = tk.BooleanVar()
var_c = tk.BooleanVar()
var_m = tk.BooleanVar()
var_y = tk.BooleanVar()

tk.Checkbutton(root, text="R", variable=var_r).pack()
tk.Checkbutton(root, text="G", variable=var_g).pack()
tk.Checkbutton(root, text="B", variable=var_b).pack()
tk.Checkbutton(root, text="C", variable=var_c).pack()
tk.Checkbutton(root, text="M", variable=var_m).pack()
tk.Checkbutton(root, text="Y", variable=var_y).pack()

boton_mostrar = tk.Button(root, text="Mostrar capa", command=procesar)
boton_mostrar.pack(pady=15)

root.mainloop()