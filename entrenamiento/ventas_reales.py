"""
Proyecto: Sistema de Gestión de ventas para tienda de indumentaria
Programador: Joaquín Quinteros
Fecha: 03/03/2026
Descripción:
    Este programa permite leer un archivo de ventas(separado en ";")
    validarlo, y generar un reporte consistente.
"""

from modulo_ventass import *

"""
Aquí se encuentra la funcion principal,a la cual se le puede agregar
un menu de opciones para verificar una cierta informacion/variable/vector si
se desea, y tambien poder seguir añadiendo funciones
"""

def principal():
    print("bienvenido admin!")
    vector = []
    abrir_archivo(vector)


if __name__ == "__main__":
    principal()