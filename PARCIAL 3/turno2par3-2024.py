from moduloturno2par32024 import *

def principal():
    vector = []
    op = 0

    while op != 5:
        print("opciones:")
        print("1)cargar arreglo")
        print("2)acomodar")
        print("3)cantidad")
        print("4)buscar")
        print("5)para salir")
        op = int(input("ingrese la opcion a elegir: "))

        if op == 1:
            n = int(input("ingrese la cantidad de tubos: "))

            for i in range(n):
                elemento = generar_arreglo()
                vector.append(elemento)


        if op == 2:
            vector_igni = acomodar_arreglo(vector)

            for i in range(len(vector_igni)):
                print("tubito: ", vector_igni[i])

            promedio = cant_gramos(vector_igni)
            print("cantidad gramos de pvc: ", promedio)

        if op == 3:
            acumulador = conteo(vector)
            a = int(input("ingrese el valor: "))
            acu_mayores_a = []

            for i in acumulador:
                if i > a:
                    acu_mayores_a.append(i)

            print("acumuladores mayores: ",acu_mayores_a )

        if op == 4:
            posi = busqueda(vector)

            if posi == -1:
                print("no se encontro")
            else:
                print("tipo: ",vector[posi].tipo ,"diametro: ", vector[posi].diametro)


if __name__ == "__main__":
    principal()

