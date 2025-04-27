import random


# Ingreso de datos
digitos_patente = int(input('Ingrese dígitos:'))

# Sorteo del dígito
sorteo = random.randint(6, 7)
print('Sorteo: ', sorteo)

# Extracción del último dígito de la patente
ultimo_digito = digitos_patente % 10

# Cálculo de la tarifa
if sorteo == ultimo_digito:
    print('Tarifa Promocional')
    # Si coincide el último dígito con lo sorteado, es precio promocional
    tarifa = 50
else:
    print('Tarifa Completa')
    # Si no coincide, es precio completo
    tarifa = 90

# Cálculo del descuento
if ultimo_digito == 7:
    print('Descuento del 50%')
    # Si la patente termina en 7, el descuento es de 50%
    descuento = tarifa * 0.5
else:
    print('Descuento del 10%')
    # Si la patente NO termina en 7, el descuento es del 10%
    descuento = tarifa * 0.1

# Monto final a pagar
monto = tarifa - descuento

# Resultados

print('Debe abonar: $', monto)

#ingrese los digitos de su patente:6
#el numero sorteado fue: 6
#valor a pagar: 41.0