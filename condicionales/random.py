import random


#Su propósito es generar un número FLOTANTE aleatorio entre 0.0 y 1.0 (incluyendo 0 pero sin incluir 1)
x = random.random()
print(x)


#Si quieres generar números aleatorios ENTEROS en un rango específico:

# número aleatorio entero,NO incluye al limite derecho
y = random.randrange(2, 10)
print(y)

# número aleatorio entero,SI incluye al limite derecho
z = random.randint(2, 10)
print(z)




#trabaja con una secuencia de datos(tuplas,strings,listas,etc)

sec1 = (2, 10, 7, 9, 3, 4) #esto es una tupla
r1 = random.choice(sec1)
print(r1)

sec2 = 'ABCDEFGHI' #un string,secuencia de caracteres
r2 = random.choice(sec2)
print(r2)
