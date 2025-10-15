from mod_videojuegos import *

def principal():
    vector = []
    arch_existe = False
    op = -1

    while op != 6:
        print("")
        print("opcion 1: cargar juegos")
        print("opcion 2: mostrar lista de juegos")
        print("opcion 3: determinar la cantidad de juegos por pais y tipo")
        print("opcion 4: crear archivo")
        print("opcion 5: mostrar archivo")
        print("opcion 6: salir")
        print("")
        op = int(input("ingrese la opcion a elegir: "))

        if op == 1:
            vector = cargar_arreglo()

        elif op == 2:
            if not vector:
                print("error,primero cargue el vector con la opcion 1")
            else:
                p = int(input("ingrese el pais de origen(0,29): "))

                for i in range(len(vector)):
                    if vector[i].pais == p:
                        print("juego: ",vector[i])

        elif op == 3:
            if not vector:
                print("error,primero cargue el vector con la opcion 1")
            else:
                generar_matriz(vector)

        elif op == 4:
            if not vector:
                print("error,primero cargue el vector con la opcion 1")
            else:
                crear_archivo(vector)
                arch_existe = True

        elif op == 5:
            if not arch_existe:
                print("error,primero cree el archivo con la opcion 4")
            else:
                mostrar_archivo()

        elif op == 6:
            print("adios")

if __name__ == "__main__":
    principal()