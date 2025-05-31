import random

random.seed(7633)
rango = range(18000)
numero_menor_4000 = 0
numero_2 = 0
numeros_mayores_10000 = 0
suma_numeros_2 = 0
cant_numeros_2 = 0
cant_numeros_8 = 0
menor = 999999

for i in rango:
    numero = random.randint(500, 13500)
    
    if numero <= 4000:
        numero_menor_4000 += 1
        
    if numero > 4000 and (numero < 10000 and numero % 4 == 0):
        numero_2 += 1

    if numero >= 10000:
        numeros_mayores_10000 += 1
#2
    if numero % 2 == 0 and numero % 6 == 0:
        suma_numeros_2 += numero
        cant_numeros_2 += 1
#3        
    if numero <= 12000:
        if numero < menor:
            menor = numero

    if numero % 8 == 0:
        cant_numeros_8 += 1


promedio = suma_numeros_2 // cant_numeros_2

porcentaje = cant_numeros_8 * 100 // 18000

print(numero_menor_4000)
print(numero_2)
print(numeros_mayores_10000)
print(promedio)
print(menor)
print(porcentaje)