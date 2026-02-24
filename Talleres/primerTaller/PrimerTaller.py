# Taller de Python - Primer Taller
# Uso de funciones, listas, operaciones matematicas, e interaccion con el usuario
# Autor: DM1-5
# 10-02-2026

import math
import typer

app = typer.Typer()


def crearLista():
    """Crea una lista de dos elementos ingresados por el usuario"""
    lista = []
    for i in range(2):
        elemento = float(typer.prompt(f"Ingrese el elemento {i+1}: "))
        lista.append(elemento)
    return lista


@app.command()
def punto_Uno(altura: float):
    """Calcula el tiempo que tarda un objeto en caer desde una altura"""
    tiempo = math.sqrt((2*altura)/(9.8))
    print(
        f"El tiempo que tarda un objeto en caer desde una altura {altura} es: {tiempo} segundos")
    return tiempo


@app.command()
def punto_Dos(v: float, opcion: int):
    """Convierte un valor de velocidad de km/h a m/s y de m/s a km/h
    1. km/h a m/s
    2. m/s a km/h 
    """
    if opcion == 1:
        resultado = v/3.6
        print(f"{v} km/h son {resultado} m/s")
        return resultado
    elif opcion == 2:
        resultado = v*3.6
        print(f"{v} m/s son {resultado} km/h")
        return resultado
    else:
        print("Opción no válida")
        return None


@app.command()
def punto_Tres(v1: float, a: float, t: float):
    """Calcula el desplazamiento de un objeto en movimiento rectilíneo uniformemente acelerado"""
    Desplazamiento = v1*t + (1/2)*a*(t**2)
    print(
        f"El desplazamiento del objeto en el tiempo {t} es: {Desplazamiento}")
    return Desplazamiento


@app.command()
def punto_Cuatro():
    """Suma vectorial de dos vectores"""
    l1 = crearLista()  # Preguntar al profesor que dimenciones debe tener la lista.
    l2 = crearLista()
    l3 = []
    for i in range(len(l1)):
        l3.append(l1[i] + l2[i])
    print(f"La suma vectorial de {l1} y {l2} es: {l3}")
    return l3


@app.command()
def punto_Cinco():
    """Calula el producto escalar de dos vectores de dos dimenciones y determina el angulo entre ellos"""
    v1 = crearLista()
    v2 = crearLista()
    temp = float()

    for i in range(len(v1)):
        temp += v1[i]*v2[i]

    # Se podria construir una funcion para calcularlo.
    moduloV1 = math.sqrt(v1[0]**2 + v1[1]**2)
    # Tambien se podria utilizar una libreria.
    moduloV2 = math.sqrt(v2[0]**2 + v2[1]**2)

    coseno = temp/(moduloV1*moduloV2)
    angulo = math.acos(coseno)
    print(f"El producto escalar de {v1} y {v2} es: {temp}")
    print(f"El angulo entre {v1} y {v2} es: {math.degrees(angulo)} grados")
    return temp, math.degrees(angulo)


@app.command()
def punto_Seis(R: float, H: float, v0: float, a: float):
    """Calcula el alcance maximo y la altura maxima alcanzada por un proyectil lanzado con una velocidad inicial v y un angulo de lanzamiento a"""
    alcance = (v0**2)*math.sin(2*math.radians(a))/9.8
    alturaMaxima = (v0**2)*(math.sin(math.radians(a)))**2/(2*9.8)
    print(f"El alcance maximo del proyectil es: {alcance} metros")
    print(
        f"La altura maxima alcanzada por el proyectil es: {alturaMaxima} metros")
    return alcance, alturaMaxima


if __name__ == "__main__":
    app()
