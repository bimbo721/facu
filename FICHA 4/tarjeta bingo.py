primero = int(input("Adivina el número del bingo (1-100): "))
segundo = int(input("Adivina el número del bingo (1-100): "))
tercer = int(input("Adivina el número del bingo (1-100): "))


import random

numeros = random.randrange(1,101), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), 
random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), 
random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), 
random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)

print('La tarjeta del usuario es: ', numeros)


if primero in numeros or segundo in numeros or tercer in numeros:
    print("el jugador marco algun numero de la tarjeta")
else:
    print("el jugador tiene mala suerte")











