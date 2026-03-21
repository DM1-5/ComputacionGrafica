import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi ventana")
ventana.geometry("400x300+400+400")

ventana.configure(bg="red")
ventana.resizable(False, False)
ventana.minsize(200, 150)
ventana.maxsize(600, 450)

texto= tk.Label (ventana, text="Hola, soy un texto")
texto.pack()
texto.place(x=50, y=50)

etiqueta = tk.Label(
    ventana,
    text="Soy una etiqueta",
    font=("Arial", 16, "bold"),
    fg="white",
    bg="blue",
    width=10,
    height=2
)

etiqueta.place(x=200, y=100)

boton = tk.Button(ventana, text="mi boton")
boton.pack()
ventana.mainloop()