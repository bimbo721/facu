import random

random.seed(9655)
rango = range(21000)
numero_1 = 0
div_7 = 0
div_3 = 0
cant_numeros_medio = 0
suma_numeros_medio = 0
menor = 99999
cant_num_may = 0


for i in rango:
    numero =random.randint(1000, 29000)
    
    if numero >= 1000 and numero < 9000:
        numero_1 += 1
    if numero >= 9000 and numero < 19000 and (numero % 2 == 1 and numero % 7 == 0):
        div_7 += 1
    if numero >= 19000 and numero % 3 == 0:
        div_3 += 1
#2    
    if numero >= 4000 and numero <= 10000:
        cant_numeros_medio += 1
        suma_numeros_medio += numero
    
#3
    if numero % 5 != 0 and numero < menor:
        menor = numero
    
    if numero >= 15000:
        cant_num_may += 1


        
promedio = suma_numeros_medio // cant_numeros_medio
porcentaje = cant_num_may * 100 // 21000

print(numero_1)
print(div_7)
print(div_3)
print(promedio)
print(menor)
print(porcentaje)







