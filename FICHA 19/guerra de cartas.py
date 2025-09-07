from funcionescartas import *


def principal():
    puntos_j1 = 0
    puntos_j2 = 0

    for i in range(3):
        cj1 = generar_carta()
        cj2 = generar_carta()

        print("carta jugador 1: ",cj1)
        print("carta jugador 2: ",cj2)

        if cj1.numero == cj2.numero:
            if cj1.palo == "oro":
                puntos_j1 += 1
            else:
                if cj2.palo == "oro":
                    puntos_j2 += 1
        else:
            if cj1.numero > cj2.numero:
                puntos_j1 += 1
            else:
                puntos_j2 += 1

    print("puntos jugador 1: ",puntos_j1)
    print("puntos jugador 2: ",puntos_j2)

principal()



