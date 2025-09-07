import random

def generar_carta():
    palos = ["basto", "espada", "oro", "copa"]
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    pal = random.choice(palos)
    numeritos = random.choice(numeros)

    carta = Carta(numeritos,pal)

    return carta



class Carta():
    def __init__(self,num,palo):
        self.numero = int(num)
        self.palo = str(palo)

    def __str__(self):
        cadena = str(self.numero) + str(self.palo)
        return cadena