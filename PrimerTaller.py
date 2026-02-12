import math

def puntoUno(h:float):
    """Calcula el tiempo que tarda un objeto en caer desde una altura h"""
    return math.sqrt((2*h)/(9.8))

def puntoDos(v:float, opcion:int):
    """Convierte un valor de velocidad de km/h a m/s y de m/s a km/h"""
    print("Que tipo de conversión desea realizar?")
    print("1. km/h a m/s")
    print("2. m/s a km/h")

    if opcion == 1:
        return v/3.6
    elif opcion == 2:
        return v*3.6
    else:
        print("Opción no válida")
        return None

def puntoTres(v1:float, a:int, t:float):
    """Calcula la posición de un objeto en movimiento rectilíneo uniformemente acelerado"""
    return v1*t + (1/2)*a*(t**2)    

def puntoCuatro(l1:list, l2:list):
    """Suma vectorial de dos vectores"""
    l3 = []
    for i in range(len(l1)):
        l3.append(l1[i] + l2[i])
    return l3

def puntoCinco(v1:list, v2:list):
    """Calula el producto escalar de dos vectores de dos dimenciones y determina el angulo entre ellos"""
    temp = float()

    for i in range(len(v1)):
        temp += v1[i]*v2[i]

    moduloV1 = math.sqrt(v1[0]**2 + v1[1]**2) # Se podria construir una funcion para calcularlo.
    moduloV2 = math.sqrt(v2[0]**2 + v2[1]**2) # Tambien se podria utilizar una libreria.

    coseno = temp/(moduloV1*moduloV2)
    angulo = math.acos(coseno)
    return temp, math.degrees(angulo)       

def puntoSeis(R:float, H:float, v0:float, a:float):
    """Calcula el alcance maximo y la altura maxima alcanzada por un proyectil lanzado con una velocidad inicial v y un angulo de lanzamiento a"""
    alcance = (v0**2)*math.sin(2*math.radians(a))/9.8
    alturaMaxima = (v0**2)*(math.sin(math.radians(a)))**2/(2*9.8)
    return alcance, alturaMaxima

