patente = int(input("ingrese los digitos de su patente:"))

import random


sorteo = random.randint(6,7)
tarifa = 90
patente %= 10
print("el numero sorteado fue:", sorteo)



if patente == sorteo:
    tarifa_promocional = 50
else:
    tarifa_promocional = 90


if patente == 7:
    descuento = tarifa * 0.5
else:
    descuento = tarifa * 0.1


monto = tarifa_promocional - descuento

print("valor a pagar:", monto)


