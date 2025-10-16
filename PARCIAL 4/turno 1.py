from mod_turno1 import *

def principal():
    vector = []
    op = -1
    arch_existe = False

    while op != 6:
        print("opcion 1)")
        print("opcion 2)")
        print("opcion 3)")
        print("opcion 4)")
        print("opcion 5)")
        print("opcion 6)")

        op = int(input("ingrese la opcion a elegir: "))

        if op == 1:
            vector = generar_arreglo()

        if op == 2:
            if not vector:
                print("error,primero cargue el vector con la opcion 1")
            else:
                mostrar_vector(vector)

        if op == 3:
            if not vector:
                print("error,primero cargue el vector con la opcion 1")
            else:
                generar_matriz(vector)

        if op == 4:
            if not vector:
                print("error,primero cargue el vector con la opcion 1")
            else:
                generar_archivo(vector)
                arch_existe = True

        if op == 5:
            if not arch_existe:
                print("error,primero cree el archivo con la opcion 4")
            else:
                mostrar_archivo()

        if op == 6:
            print("adios")

if __name__ == "__main__":
    principal()