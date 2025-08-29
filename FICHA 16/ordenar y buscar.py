import random

def impares_mayores(vector,x):
    cantidad = 0
    
    for i in vector:
        if i % 2 != 0 and i > x:
            cantidad += 1
    return cantidad
    

def principal():
    n = int(input("ingrese la cantidad de elementos: "))
    
    vector = [0] * n
    
    for i in range(n):
        vector[i] = random.randint(1,100)
    
    
    for i in range(n-1):
        for j in range(i+1,n):
            if vector[i] > vector[j]:
                vector[j], vector[i] = vector[i], vector[j]
            
    
    x = int(input("que numero quiere buscar: "))
    bandera = False
    izq = 0
    der = n-1
    
    while izq <= der:
        centro = (izq + der) // 2

        if x == vector[centro]:
            bandera = True
            break
        else:
            if vector[centro] > x:
                der = centro - 1
            else:
                izq = centro + 1


    print("vector acomodado:",vector)
    if bandera == True:
        cant_valores = impares_mayores(vector,x)
        print("encontro")      
        print("2: ", cant_valores)  
    else:
        print("no encontro")

principal()