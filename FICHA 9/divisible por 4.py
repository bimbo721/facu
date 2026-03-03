import random

random.seed(11)

cont_div_4 = 0
cont_div_4_8 = 0
suma = 0
cant_may = 0
#bandera_primer = False
primer_num = 0 #para que no de fallos en la primer vuelta en el apartado 3
cant_menores = 0
bandera_1 = False
bandera_2500 = False



for i in range(0,1000):
    numero = (random.randint(1, 2500))

    #if bandera_primer is False:
    #    primer_num = numero
    #    bandera_primer = True

    if i == 0:
        primer_num = numero

    if (numero % 4 == 0) and (numero % 8 != 0):
        cont_div_4 += 1

    if (numero % 4 == 0) and (numero % 8 == 0):
        cont_div_4_8 += 1

    if numero > 2000:
        suma += numero
        cant_may +=1

    if numero < primer_num:
        cant_menores += 1

    if numero == 1:
        bandera_1 = True
    if numero == 2500:
        bandera_2500 = True


promedio = suma // cant_may
porcentaje = (cant_menores * 100) // 1000

print("1):", cont_div_4,"---",cont_div_4_8)
print("2):", promedio)
print("3):", cant_menores,"procentaje:", porcentaje)
print("4):aparecio el 1",bandera_1,"aparecio el 2500",bandera_2500)
