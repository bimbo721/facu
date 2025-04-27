apuesta = int(input("ingrese 1 para elegir cara o 2 para elegir cruz:"))

import random

moneda = random.randrange(1,3)

if apuesta == moneda:
    print("acerto")
else:
    print("no acerto")



