import random

random.seed(95)
rango = range(45000)
cant_numeros_menores = 0
cant_multiplos_6 = 0
cant_multiplos_9 = 0
cant_multiplos_ambos = 0
mayor = 0
mayor_multiplo_4 = 0

for i in rango:
    numero = random.randint(1,95000)
    
    if i == 1:
        mayor = numero
        
    if numero < mayor:
        cant_numeros_menores += 1
    
    if numero % 6 == 0:
        cant_multiplos_6 += 1
        
    if numero % 9 == 0:
        cant_multiplos_9 += 1
        
    if numero % 6 == 0 and numero % 9 == 0:
        cant_multiplos_ambos += 1
    
    if numero % 4 == 0:
        if numero > mayor_multiplo_4:
            mayor_multiplo_4 = numero
        
        

    
print(cant_numeros_menores)
print("multiplos 6: ", cant_multiplos_6)
print("multiplos 9: ", cant_multiplos_9)
print("multiplos ambos: ", cant_multiplos_ambos)
print("la 3:", mayor_multiplo_4)








