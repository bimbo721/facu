from pruebas import *

def principal():
    vector = []
    op = -1
    while op != 5:
        print("1. Cargar arreglo")
        print("2. Mostrar ordenado")
        print("3. Contar por tipo")
        print("4. Buscar")
        print("5. Salir")
        op = int(input("Ingrese número de opción: "))

        if op == 1:
            n = int(input("ingrese la cantidad a cargar: "))
            for i in range(n):
                tubo = cargar_arreglo()
                vector.append(tubo)


        if op == 2:
            v_igni = ordenar_vector(vector)
            n = len(v_igni)

            for i in range(n):
                print("tubo: ",v_igni[i])
            suma = 0
            for i in v_igni:
                suma += i.cantidad
            if n != 0:
                promedio = suma / n
                print("promedio: ",promedio)

        if op == 3:
            v_acu = conteo(vector)
            a = int(input("ingrese el valor a: "))

            for i in range(len(v_acu)):
                if v_acu[i] > a:
                    print("tipo:", i+1 ," cantidad:",v_acu[i])

        if op == 4:
            posi = busqueda(vector)

            if posi == -1:
                print("no se encontro")
            else:
                print("existe,","tipo:",vector[posi].tipo," diametro:",vector[posi].diametro)

        if op == 5:
            print("bye")

if __name__ == "__main__":
    principal()