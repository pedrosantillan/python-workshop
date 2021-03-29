from math import pi,pow
global areaCirculo, areaCuadrado, areaTriangulo

def circle(radio):
    try:
        areaCirculo = pi*(pow(radio, 2))
        return areaCirculo
    except TypeError:
        print("no se aceptan valores str")
        return 0

def cuadrado(lado):
    try:
        areaCuadrado = pow(lado, 2)
        return areaCuadrado
    except TypeError:
        print("no se aceptan valores str")
        return 0

def triangulo(area, base):
    try:
        areaTriangulo = 2*(area/base)
        return areaTriangulo
    except TypeError:
        print("no se aceptan valore str")
        return 0
    except ZeroDivisionError:
        print("la base no puede tener valor de 0")
        return 0