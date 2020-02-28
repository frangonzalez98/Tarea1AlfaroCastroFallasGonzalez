# INSTITUTO TECNOLÓGICO DE COSTA RICA
# MICROCONTROLADORES Y MICROPROCESADORES
# INGENIERÍA MECATRÓNICA
# Tarea 1 --
#
# Alfaro Cordero Randall
# Castro Hidalgo Ignacio
# Fallas Martinez Jasson
# Gonzalez Rosabal Francisco

import Funciones


# PARTE 1: PRUEBAS DE EXITO


# Prueba la función de capitalizar
def test_exitocapitalizar():
    capitalizarRes = Funciones.capitalizar("hola")
    assert capitalizarRes == "HOLA"


# Prueba la función de revisión de W minúscula
def test_exitotieneW():
    tieneWRes = Funciones.tieneW("walter")
    assert tieneWRes is True


# Revisa la resta
def test_exitoresta():
    restaRes = Funciones.resta(10, 5)
    assert restaRes == 5


# PARTE 2: PRUEBAS DE FALLO


# Prueba que el código de error al pasar un parámetro inválido
# sea el esperado para capitalizar
def test_errorcapitalizar():
    capitalizarRes = Funciones.capitalizar(8)
    assert capitalizarRes == -1


# Prueba que el código de error al pasar un parámetro inválido
# sea el esperado para tieneW
def test_errortieneW():
    tieneWRes = Funciones.tieneW(10)
    assert tieneWRes == -3


# Revisa que ante una salida no natural, el resultado sea el código
# de error otorgado -5
def test_errorresta():
    restaRes = Funciones.resta(5, 20)
    assert restaRes == -5
