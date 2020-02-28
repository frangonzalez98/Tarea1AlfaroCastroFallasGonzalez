# -*- coding: cp1252 -*-
# INSTITUTO TECNOL�GICO DE COSTA RICA
# MICROCONTROLADORES Y MICROPROCESADORES
# INGENIER�A MECATR�NICA
# Tarea 1 --
#
# Alfaro Cordero Randall
# Castro Hidalgo Ignacio
# Fallas Martinez Jasson
# Gonzalez Rosabal Francisco


# Funci�n que  recibe un string de caracteres en
# min�scula y retorna el mismo string pero en may�scula
def capitalizar(palabra):
    if not isinstance(palabra, str):
        print("No ingres� el tipo de dato correcto.")
        return -1

    if not palabra.islower():
        print("El texto ingresado no est� en min�scula")
        return -2

    palabraCap = palabra.upper()
    return palabraCap


# Funci�n que  toma un string de caracteres y detecta
# la presencia de la letra �w� en min�scula
def tieneW(palabra):
    if not isinstance(palabra, str):
        print("No ingres� el tipo de dato correcto")
        return -3

    return "w" in palabra


# Funci�n que  recibe dos n�meros naturales y devuelve
# la resta
def resta(num1, num2):
    if not (isinstance(num1, int) and isinstance(num2, int)):
        print("No ingres� el tipo de dato correcto")
        return -4

    res = num1 - num2
    if res < 0:
        print("El resultado es un n�mero no natural")
        return -5
    else:
        return res
