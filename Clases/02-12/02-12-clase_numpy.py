import numpy as np 

lista = [31,28,2,9]

arr = np.array(lista)

lista_2d = [[2,3,4],
            [5,6,7],
            [8,9,10]]

arr_2d = np.array(lista_2d)

# Metodos de numpy

print("Tamanio: ", arr_2d.shape) 
print("Dimension: ", arr_2d.ndim) # Para un arreglo de dos dimensiones, el numero de filas es igual al numero de elementos del arreglo y el numero de columnas es igual al numero de elementos del primer elemento del arreglo.
print("Dimension: ", arr.ndim) # Para un arreglo de una dimension, el numero de filas es igual a 1 y el numero de columnas es igual al numero de elementos del arreglo.
print("Tipo de dato: ", arr_2d.dtype) # Tipo de dato de los elementos del arreglo
print("Tamanio en bytes: ", arr_2d.itemsize) # Tamanio en bytes de cada elemento
print("Numero de elementos: ", arr_2d.size) # Cantidad de elementos 

arr_2d_int16 = np.array(lista_2d, dtype=np.int16) # Cambiar el tipo de dato de los elementos del arreglo

arr_1d = np.arange(10) # Crear un arreglo de una dimension con valores del 0 al 9
print(arr_1d)

arr_2d= np.arange(10).reshape(2,5)  # Crear un arreglo de una dimension con valores del 0 al 9
print(arr_2d)

arr_range = np.arange(10,21,2) # Crear un arreglo de una dimension con valores del 0 al 9 con un paso de 2 
#inicio, fin, paso
print(arr_range)  

arr_lins = np.linspace(10,15,11) # Crear un arreglo de una dimension con valores del 0 al 10 con 5 elementos
print(arr_lins)


a = np.linspace(10,20,6)
b = np.linspace(5,25,6)

print("A: ", a)
print("B: ", b)

# Estas operaciones se realizan de componente a componente.

suma = a + b
print("Suma: ", suma)

resta = a - b
print("Resta: ", resta)

multiplicacion = a * b
print("Multiplicacion: ", multiplicacion)

division = a / b
print("Division: ", division)

print("Suma total:", np.sum(arr_2d)) # Suma total de los elementos del arreglo
print("Suma columnas: ", np.sum(arr_2d, axis=0)) # Suma de las columnas del arreglo
print("Suma filas: ", np.sum(arr_2d, axis=1)) # Suma de las filas del arreglo

print("Maximo: ", np.max(arr_2d)) # Maximo valor del arreglo
print("Minimo: ", np.min(arr_2d)) # Minimo valor del arreglo
print("Promedio: ", np.mean(arr_2d)) # Promedio de los elementos del arreglo


# img[fila, columna]

# fila completa img[2,:]

# columna completa img[:,2]

# submatriz img[1:3, 1:3] # Desde la fila 1 hasta la fila 2 y desde la columna 1 hasta la columna 2 (sin incluir la fila 3 ni la columna 3)

listas_2d=[[2,3,4,8],
           [5,6,7,11],
           [8,9,10,20],
           [11,12,14,10]]

arr_2d = np.array(listas_2d)

print(arr_2d[:2,:2]) # Desde la fila 0 hasta la fila 1 y desde la columna 0 hasta la columna 1 (sin incluir la fila 2 ni la columna 2)
