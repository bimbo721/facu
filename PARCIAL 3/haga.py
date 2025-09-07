from modulosturno1 import *

def principal():
    vector = []

    op = 0
    while op != 5:
        print("1. Cargar arreglo")
        print("2. Mostrar ordenado")
        print("3. Conteo por tipo")
        print("4. BUscar")
        print("5. Salir")
        op = int(input("Ingrese número de opción: "))

        if op == 1:
            n = int(input("ingrese la cantidad de empleados a cargar: "))

            for i in range(n):
                empleado = cargar_arreglo(n)
                vector.append(empleado)

        if op == 2:
            acomodar_vector(vector)
            suma = 0
            for i in range(len(vector)):
                print(str(vector[i].num_ident) + " | " + vector[i].desc + " | " + str(vector[i].tipo) + " | " + str(vector[i].monto))
                suma += vector[i].monto

            print("sueldos a pagar: ", suma)

        if op == 3:
            cant_empleos = conteo(vector)
            print("cantidad: ",cant_empleos)

        if op == 4:
            x = int(input("ingrese el numero a buscar: "))

            posi = buscar_empleado(vector,x)

            if posi != -1:
                print("descripcion: " + vector[posi].desc + "sueldo: " + vector[posi].monto)
            else:
                print("no se encontro")

principal()