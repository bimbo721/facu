import random

def calcular_promedio(vector):
    cant = len(vector)
    suma = 0
    for i in vector:
        suma += i
    
    return suma // cant


def principal():
    
    n = int(input("ingrese la cantidad de elementos: "))
    c = int(input("ingrese cual es el numero maximo que quiere comprobar: "))
    
    vector = [0] * n
    print("")

    print("vector antes del random: ", vector)

    for i in range(len(vector)):
        vector[i] = (random.randint(1, c))

    print("vector despues random: ", vector)
    primos = []
    
    for i in vector:
        if i > 1:
            if i // i == 1 and i // 1 == i:
                primos.append(i)

    
    promedio = calcular_promedio(vector)

    print("1: ",primos)
    print("2: ",promedio)
                    

principal()
