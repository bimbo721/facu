import random
random.seed(49)

sumatotal=0
cant_numeros= range(20000)
cant_multiplos_5=0
cant_multiplos_7=0
cant_multiplos_9=0
cant_numeros_pares_menores_15000=0
mayornumero=0


for i in cant_numeros:
    numero = random.randint(1, 45000)
    ultimo_digito = numero % 10
    
    if numero % 5 == 0:
        cant_multiplos_5 += 1
    if numero % 7 == 0:
        cant_multiplos_7 += 1
    if numero % 9 == 0:
        cant_multiplos_9 += 1
        
    if ultimo_digito >= 5 and ultimo_digito <= 8:
        if numero > mayornumero:
            mayornumero = numero
        else:
            mayornumero = mayornumero
        
    if numero % 2 == 0 and numero < 15000:
        cant_numeros_pares_menores_15000 += 1
        
porcentaje= int(cant_numeros_pares_menores_15000*100/20000)
        
print()        
        
    

    
    



