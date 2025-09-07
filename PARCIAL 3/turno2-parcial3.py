from modulosturno2 import *

def principal():
    vector = []

    op = 0
    while op != 5:
        input("1)cargar vector")
        input("2)mostrar datos")
        input("3)importe acumulado")
        input("4)buscar un numero de identificacion")
        op = int(input("elija la opcion: "))

        if op == 1:
            n = int(input("ingrese la cantidad de pasajeros:"))
            for i in range(n):
                pasajero = generar_arreglo()
                vector.append(pasajero)

        if op == 2:
            acomodar_codigo_vuelo(vector)
            x = int(input("ingrese el numero de asiento: "))
            vector_ticekts = ticekts_mayores_num(vector,x)

            print("tickets:", vector_ticekts)

        if op == 3:
            importe_cobrado = nose(vector)

            print("importe cobrado: ",importe_cobrado)


        if op == 4:
            id = input("ingrese el numero de identificacion a buscar: ")
            posi = buscar_num_ident(vector,id)

            if posi != -1:
                print("existe el ticket, " + "asiento :" + str(vector[posi].asiento) + "pais: " + str(vector[posi].pais))
            else:
                print("no se encontro")


if __name__ == "__main__":
    principal()