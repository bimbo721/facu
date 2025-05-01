import random


palos = ('Espadas', 'Bastos')#, 'Oros', 'Copas')
valores = (1, 2, 3, 4, 5, 6, 7, 10, 11, 12)

carta1 = random.choice(palos), random.choice(valores)
carta2 = random.choice(palos), random.choice(valores)
carta3 = random.choice(palos), random.choice(valores)


if carta2 == carta1:
    carta2 = random.choice(palos), random.choice(valores)

if carta3 == carta1 or carta3 == carta2:
    carta3 = random.choice(palos), random.choice(valores)


if carta1 == (palos[0], valores[0]) or carta2 == (palos[0],valores[0]) or carta3 == (palos[0], valores[0]):
    print("tenes el macho")
else:
    print("no lo tenes")


if carta1[0] == carta2[0] == carta3[0]:
    if carta1[1] > carta2[1] and carta1[1] > carta3[1]:
        print("la carta mas alta es la 1")
    elif carta2 > carta3:
        print("la carta mas alta es la 2")
    elif carta3 > carta2:
        print("la carta mas alta es la 3")

#esto lo podria haber hecho:
#if carta1[1] == carta2[1] and carta1[1] == carta3[1]:
#    mayor = max(carta1[0], carta2[0], carta3[0])


print("tus cartas son:")
print(carta1)
print(carta2)
print(carta3)
