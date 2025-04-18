#beneficiario = input("ingrese el nombre y apellido del beneficiario:")
codigo = input("ingrese el codigo de identificacion de la transferencia:")
monto_nominal = int(input("ingrese el valor a transferir:"))



if "ARS" in codigo:
    print("es valido")
elif "USD" in codigo:
    print("es valido")
elif "EUR" in codigo:
    print("es valido")
elif "JPY" in codigo:
    print("es valido")
elif "GPB" in codigo:
    print("es valido")

else: 
    print("no es valido")


importe = 12

monto_base = monto_nominal - importe
    
impuesto_indicado = ...
#4
if monto_base > 500000:
    monto_base // 21


#print("Beneficiario:", beneficiario)
#print("Moneda:", moneda)
#print("Monto base (descontadas las comisiones):", monto_base)
#print("Monto final (descontados los impuestos):", monto_final)























