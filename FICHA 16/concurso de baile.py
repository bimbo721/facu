import random

from moduloconcurso import *


def principal():
    vector = [0] * 7
    total = 0
    n = len(vector)
    for i in range(n):
        vector[i] = random.randint(-1,10)

    acomodar_vector(vector,n)

    print("vector:",vector)

    #2
    x = int(input("ingrese el puntaje a buscar: "))
    busqueda = busqueda_binaria(vector,n,x)
    
    
    #3
    menor = vector[0]
    mayor = vector[-1]
    
    diferencia = mayor - menor
    
    #4
    for i in vector:
        total += i
    
    #1
    print("los mejores puntajes fueron: ", vector[-1], vector[-2], vector[-3])
    if busqueda == True:
        print("encontro el puntaje ",x)
        notas = notas_mayores_x(vector,x)

        if notas == []:
            print("no hay notas mayores a:",x)
        else:
            print("las notas mayores son: ",notas)
        
    else:
        print("no encontro puntajes mayores a ",x)
    
    print("diferencia: ",diferencia)
    
    if total < 20:
        print("descalificados")
    else:
        promedio = promedio_final(vector)
        print("promedio total final:", promedio)
    
principal()


