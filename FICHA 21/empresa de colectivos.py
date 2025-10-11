def apartado_1(matriz,n,m):
    for f in range(n):
        suma = 0
        for c in range(len(matriz[f])):
            suma += matriz[f][c]
        print("total de pasajeros en la linea "+ str(f+1) + " es de:" + str(suma))


def apartado_2(matriz,n,m):
    x = int(input("ingrese la parada que quiere saber el promedio:"))
    x = x-1
    suma = 0
    for f in range(n):
        for c in range(len(matriz[f])):
            if x == c:
                suma += matriz[f][c]

    promedio = suma / n
    print(promedio)


def apartado_3(matriz,n,m):
    x = int(input("ingrese la linea de la que quiere saber la menor cantidad:"))
    x = x-1
    menor = 9999999999999

    for i in matriz[x]:
        if i < menor:
            menor = i

    print("menor cantidad de pasajeros de una linea:",menor)


def apartado_4(matriz,n,m):
    cant_pasajeros = 0

    for f in range(n):
        for c in range(len(matriz[f])):
            cant_pasajeros += matriz[f][c]

    recaudacion = cant_pasajeros * 8.5
    print("recaudacion: ",recaudacion)


def principal():
    n = int(input("ingrese la cantidad de lineas(filas):"))
    m = int(input("ingrese la cantidad de paradas(columnas):"))


    matriz = [0] * n
    for c in range(n):
        matriz[c] = [0] * m


    for f in range(n):
        for c in range(len(matriz[f])):
            matriz[f][c] = int(input("ingrese la cantidad de pasajeros que se subieron de la linea "+ str(f+1) + " en la parada " +str(c+1) + ":"))


    apartado_1(matriz,n,m)
    apartado_2(matriz,n,m)
    apartado_3(matriz,n,m)
    apartado_4(matriz,n,m)


principal()