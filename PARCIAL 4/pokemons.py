import os.path
import pickle
import random
from mod_pokemos import *



# Muestra las opciones, y carga y retorna la que elija el usuario.
def menu():
    print("1. Cargar (con inserción ordenada")
    print("2. Mostrar (de acuerdo a lo requerido")
    print("3. Conteo o Búsqueda (según sea requerido)")
    print("4. Generar archivo binario (de acuerdo a lo requerido")
    print("5. Mostrar archivo binario (de acuerdo a lo requerido")
    print("6. Salir del programa.")
    return int(input("Ingrese la opción: "))


def principal():
    random.seed(13715)
    fd = "archivopokemon.dat"
    vector = []
    op = -1
    while op != 6:
        op = menu()

        if op == 1:
            vector = cargar_arreglo()

        elif op == 2:
            if vector:
                mostrar_vector(vector)

            else:
                print("el vector no fue cargado todavía...")

        elif op == 3:
            if vector:
                generar_matriz(vector)
            else:
                print("El vector no fue cargado todavía...")

        elif op == 4:
            if vector:
                generar_archivo(fd,vector)
            else:
                print("El vector no fue cargado todavía...")

        elif op == 5:
            if os.path.exists(fd):
                mostrar_archivo(fd)
            else:
                print("El archivo", fd, "no existe...")

        elif op == 6:
            print()
            print("Programa terminado... Hasta la vista baby...")
            print()


if __name__ == "__main__":
    principal()
