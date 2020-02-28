# -*- coding: cp1252 -*-
# INSTITUTO TECNOLÓGICO DE COSTA RICA
# MICROCONTROLADORES Y MICROPROCESADORES
# INGENIERÍA MECATRÓNICA
# Tarea 1 --
#
# Alfaro Cordero Randall
# Castro Hidalgo Ignacio
# Fallas Martinez Jasson
# Gonzalez Rosabal Francisco


# Función que  recibe un string de caracteres en
# minúscula y retorna el mismo string pero en mayúscula
def capitalizar(palabra):
    if not isinstance(palabra, str):
        print("No ingresó el tipo de dato correcto.")
        return -1

    if not palabra.islower():
        print("El texto ingresado no está en minúscula")
        return -2

    palabraCap = palabra.upper()
    return palabraCap


# Función que  toma un string de caracteres y detecta
# la presencia de la letra “w” en minúscula
def tieneW(palabra):
    if not isinstance(palabra, str):
        print("No ingresó el tipo de dato correcto")
        return -3

    return "w" in palabra


# Función que  recibe dos números naturales y devuelve
# la resta
def resta(num1, num2):
    if not (isinstance(num1, int) and isinstance(num2, int)):
        print("No ingresó el tipo de dato correcto")
        return -4

    res = num1 - num2
    if res < 0:
        print("El resultado es un número no natural")
        return -5
    else:
        return res
