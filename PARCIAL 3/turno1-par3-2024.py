from modulosturno1par32024 import *


def principal():
    vector = []
    op = 0
    while op != 5:
        print("opciones:")
        print("1)cargar arreglo")
        print("2)mostrar datos")
        print("3)cantidad de servicios")
        print("4)buscar servicio")
        print("5)salir")
        op = int(input("ingrese la opcion a elegir: "))

        if op == 1:
            n = int(input("ingrese la cantidad de productos:"))
            for i in range(n):
                producto = generar_arreglo()
                vector.append(producto)

        if op == 2:
            acomodar_vector(vector)
            suma_calorias = 0

            for i in range(len(vector)):
                print("producto:",vector[i])

            for i in range(len(vector)):
                suma_calorias += vector[i].calorias

            suma_calorias = suma_calorias // len(vector)
            print("promedio: ", suma_calorias)

        if op == 3:
            vector_tipos = conteo(vector)
            vector_mostrar = []

            for i in range(len(vector_tipos)):
                if 0 < vector_tipos[i] < 3:
                    vector_mostrar.append(i+1)

            print("valores entre 0 y 3:",vector_mostrar)

        if op == 4:
            posi = busqueda(vector)

            if posi != -1:
                print("existe,",vector[posi].desc , "precio:", vector[posi].precio)
            else:
                print("no existe")


if __name__ == "__main__":
    principal()