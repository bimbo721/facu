def calcular_promedio(vector):
    suma = 0
    cant = len(vector)
    for i in vector:
        suma += i
    return suma // cant

def calcular_cant(vector,promedio):
    cantidad = 0
    for i in vector:
        if i > promedio:
            cantidad += 1
    return cantidad


def principal():
    n = int(input("ingrese el tamaño del vector: "))

    vector = []

    for i in range(n):
        a = int(input(("ingrese los numeros: ")))
        vector.append(a)

    promedio = calcular_promedio(vector)
    cant_mayores_promedio = calcular_cant(vector,promedio)

    print("1: ", promedio)
    print("2: ", cant_mayores_promedio)
principal()