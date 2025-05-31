import random

rango = range(5000)
random.seed(76)
cant_num_pares_6 = 0
cant_num_mayores_primer_numero = 0
cant_millar = 0


for i in rango:
    numero = random.randint(1,65000)
    
    if numero % 2 == 0 and numero % 6 == 0:
        cant_num_pares_6 += 1

    if i == 0:
        mayor = numero
    elif numero > mayor:
        cant_num_mayores_primer_numero += 1
    
    if numero > 1001 and numero < 2000:
        cant_millar += 1
    
    
porcentaje = cant_num_mayores_primer_numero * 100 // 5000
#1001 hasta el 2000
print("1: ",cant_num_pares_6)
print("2: ",cant_num_mayores_primer_numero)
print("3: ",cant_millar)
print("porcentaje: ",porcentaje)
