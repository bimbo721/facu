import random

random.seed(20220512)

rango = range(1, 25000)
numeros_multiplos_3 = 0
numeros_multiplos_5 = 0 #(y no de 3)
numeros_que_no_cumplen = 0
numero_mayor = 0
suma_multiplos_pares = 0
cantidad_multiplos_pares = 0


for i in rango:
    numero = random.randint(1, 45000)
    if numero % 3 == 0:
        numeros_multiplos_3 += 1
    elif numero % 5 == 0 and numero % 3 != 0:
        numeros_multiplos_5 += 1
    else:
        numeros_que_no_cumplen += 1
        
    numero_str = str(numero)
    #2
    if numero_str[0] == "1":
        if numero > numero_mayor:
            numero_mayor = numero
        else:
            numero_mayor = numero_mayor
        
    #3
    if numero % 11 == 0 and numero % 2 == 0:
        cantidad_multiplos_pares += 1
        suma_multiplos_pares += numero
        
promedio_pares = suma_multiplos_pares // cantidad_multiplos_pares

porcentaje_3 = numeros_multiplos_3 * 100 // 25000
porcentaje_5 = numeros_multiplos_5 * 100 // 25000
porcentaje_no_cumplen = numeros_que_no_cumplen * 100 // 25000

print("multiplos de 3: ", numeros_multiplos_3)
print("multiplos de 5: ", numeros_multiplos_5)
print("nuemros que no cumplen: ", numeros_que_no_cumplen)
print("numero mayor: ",numero_mayor)
print("promedio pares: ", promedio_pares)
print("porcentaje 3:",porcentaje_3)
print("porcentaje 5:",porcentaje_5)
print("porcentaje no cumple:",porcentaje_no_cumplen)










