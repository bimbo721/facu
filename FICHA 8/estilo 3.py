import random
random.seed(37)
rango = range(27000)
numero_1 = 0
numero_2 = 0
numero_3 = 0
cant_del_apartado_2 = 0
suma_del_apartado_2 = 0
mayor = 0
cant_multiplos_7 = 0

for i in rango:
    numero = random.randint(-20000, 30000)
    
    if numero >= -20000 and numero < -5000:
        numero_1 += 1
        
    if numero >= -5000 and numero < 15000:
        numero_2 += 1
    
    if numero >= 15000 and numero % 9 ==0:
        numero_3 += 1
#apartado 2:

    if numero >= 1000 and (numero % 10 == 4 or numero % 10 == 6):
        cant_del_apartado_2 += 1
        suma_del_apartado_2 += numero
        
#apartado 3:
    ultimo_digito = numero % 10
    if numero > 0 and ultimo_digito == 4 or ultimo_digito == 6:
        if numero > mayor:
            mayor = numero
    
        
    if numero % 7 == 0:
        cant_multiplos_7 += 1


porcentaje = cant_multiplos_7 * 100 // 27000
promedio = suma_del_apartado_2 // cant_del_apartado_2

print("cantidad 1: ",numero_1)
print("cantidad 2: ",numero_2)
print("cantidad 3: ",numero_3)
print()
print("promedio del apartado 2: ",promedio)
print("el mayor: ",mayor)
print("porcentaje: ", porcentaje,"%")


