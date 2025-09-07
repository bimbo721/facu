from modulosturno3 import *


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
            n = int(input("ingrese la cantidad de servicio: "))

            for i in range(n):
                cliente = generar_arreglo()
                vector.append(cliente)

        if op == 2:
            valor1 = int(input("ingrese el monto minimo: "))
            valor2 = int(input("ingrese el monto maximo: "))
            acomodar_vector(vector)

            vector_2 = generar_vector2(vector,valor1,valor2)

            #datos de servicios que cumplen con la condicion
            for i in vector_2:
                print("servicio ",i)

            #linea final
            print("cantidad de servicios mostrados en este listado: ",len(vector_2))


        if op == 3:
            v_servi = conteo(vector)

            for i in v_servi:
                if v_servi[i] != 0:
                    print("cantidad de servicios de tipo ",i+1 ,": ",v_servi[i])


        if op == 4:
            posi = buscar_servicio(vector)

            if posi != -1:
                print("objeto actualizado: ", vector[posi])
            else:
                print("no existe")

if __name__ == "__main__":
    principal()