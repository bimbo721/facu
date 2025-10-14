from mod_servi import *

def principal():
    op = 0
    vector = []
    while op != 6:
        print("opcion 1")
        print("opcion 2")
        print("opcion 3")
        print("opcion 4")
        print("opcion 5")
        print("opcion 6")
        op = int(input("opcion a elegir:"))

        if op == 1:
            vector = cargar_arreglo()

        if op == 2:
            c = int(input("ingrese la cantidad de reporducciones mayor:"))

            for i in range(len(vector)):
                if vector[i].cantidad > c:
                    print(vector[i])

        if op == 3:
            generar_matriz(vector)


        if op == 6:
            print("bye")

principal()
