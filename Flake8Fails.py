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


# PyFlakes puede detectar cuando una variable
# no esta siendo usada.
# El error reportado debe iniciar con una F
def flakes_unused_variable(a):
    sinUsar = 5
    usada = 10
    return usada+a

# Aquí se producirá otro error por problemas de
# formato según PEP8.
# El plugin pycodestyle interviene, y el error
# detectado inicia con E o W.
# En este caso particular, el def debió tener
# dos espacios vacíos en la parte superior
# pero solo tiene uno (antes del comentario)
def useful_function(a, b):
    return a+b


# Aqui hay otro error adicional, debido a que esta linea es muy larga y por lo tanto estorba en la lectura del código.
# Esta funcion es innecesariamente complicada
# McCabe incorporado en Flake8 lo detecta
def funcion_atroz():
    # Bien se conoce que el uso excesivo de elif no es bienvenido
    # Note entonces como McCabe detecta este error
    randNumber = random.random()
    if randNumber <= 0.1:
        return 1
    elif randNumber <= 0.2:
        return 2
    elif randNumber <= 0.3:
        return 3
    elif randNumber <= 0.4:
        return 4
    elif randNumber <= 0.5:
        return 5
    elif randNumber <= 0.6:
        return 6
    elif randNumber <= 0.7:
        return 7
    elif randNumber <= 0.8:
        return 8
    elif randNumber <= 0.9:
        return 9
    elif randNumber <= 10:
        return 10


# Ya que el error anterior no se nota si no se especifica la
# complejidad de McCabe deseada, entonces se presenta un error
# alternativo final
# Si se desea detectar, utilice --max-complexity 10


# Otro error es el de una variable inexistente
def not_found_variable():
    return variableInexistente
