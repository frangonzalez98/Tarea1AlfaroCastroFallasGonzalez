# Flake 8: Pruebas de fallo
# Instituto Tecnológico de Costa Rica
# Microcontroladores y microprocesadores
#
# Alfaro Cordero Randall
# Castro Hidalgo Ignacio
# Fallas Martinez Jasson
# Gonzalez Rosabal Francisco
#
# Flake 8 combina los tres siguientes plugins:
# 1) PyFlakes
# 2) PyCodeStyle
# 3) McCabe
#
# En este archivo de prueba, se provocara al menos un error
# para cada caso.

import random
import math


# Se removio la variable sin usar
def flakes_unused_variable(a):
    usada = 10
    return usada+a


# Se agrego la linea faltante
def useful_function(a, b):
    return a+b


# Ya no hay una linea excesivamente larga
# y se arreglo al complejidad de la funcion
def funcion_atroz():
    randNumber = random.random()
    return math.ceil(randNumber*10)


# Se creó la variable
def not_found_variable():
    variableInexistente = 4
    return variableInexistente
