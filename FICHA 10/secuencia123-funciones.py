def mayor_impares(numero,mayor):
    if numero % 2 != 0:
        if numero > mayor:
            return numero
        else:
            return mayor

def divisibles(numero):
    if numero % 4 == 0:
        return 1
    else:
        return 0
       
        
def principal():
    cant_divisib = 0
    mayor = 0
    numero = int(input("ingrese los numeros:"))
    
    while numero > 0:
        
        numeros_divisibles = divisibles(numero)
        cant_divisib += numeros_divisibles
        
        impar_mayor = mayor_impares(numero,mayor)
        mayor = impar_mayor
        numero = int(input("ingrese los numeros:"))
        
    print("divisibles: ", cant_divisib)
    print("impar: ", mayor)
               
principal()