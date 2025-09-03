import random

def acomodar_vector(v,n):
    
    for i in range(0,n-1):
        for j in range(i+1,n):
            if v[i] > v[j]:
                v[i] , v[j] = v[j] , v[i]
                
def buscar(v,x):
    izq = 0
    der = len(v) - 1
    bandera = False
    
    while izq <= der :
        centro = (der + izq) // 2
        
        if v[centro] == x:
            return True
        else:
            if v[centro] > x:
                der = centro - 1
            else:
                izq = centro + 1
                
    return bandera


def principal():
    n = int(input("ingrese la cantidad de alumnos: "))
    x = int(input("ingrese el legajo a buscar: "))
    
    vector = []
    
    for i in range(0,n):
        legajo = random.randint(1000,10000)
        vector.append(legajo)
        
    print("vector: ", vector)
    
    acomodar_vector(vector,n)

    print("vector acomodado: ", vector)

    bandera_x = buscar(vector,x)
    
    if bandera_x == True:
        print("se encontro el legajo: ", x)
    else:
        print("no se encontro el legajo")

principal()