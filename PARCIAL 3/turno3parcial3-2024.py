from moduloturno3par3 import *

def principal():
    vector = []
    op = 0
    while op != 5:
        print("opciones:")
        print("1)cargar arreglo")
        print("2)mostrar datos")
        print("3)cantidad taxis")
        print("4)buscar dni")
        print("5)para salir")
        op = int(input("ingrese la opcion a elegir: "))

        if op == 1:
            n = int(input("ingrese la cantidad de taxis: "))

            for i in range(n):
                elemento = generar_arreglo()
                vector.append(elemento)

        if op == 2:
            vector_tarifa = ordenar_arreglo(vector)
            for i in vector_tarifa:
                print("datos taxis que cumplen con la condicion: ",vector_tarifa[i])

            print("cantidad de taxis mostrados: ",len(vector_tarifa))


        if op == 3:
            v_acu = conteo(vector)
            v_mostrar = []

            for i in v_acu:
                if i != 0:
                    v_mostrar.append(i)
            print("contadores distintos de cero: ", v_mostrar)


        if op == 4:
            posi = buscar_dni(vector)

            if posi == -1:
                print("no se encontro")
            else:
                vector[posi].tarifa = vector[posi].tarifa - (vector[posi].tarifa * 15 // 100)

                print("datos del objeto modificado: ",vector[posi])


        if op == 5:
            print("adios")



if __name__ == "__main__":
    principal()