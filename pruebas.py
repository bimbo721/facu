codigo = input("ingrese el codigo de identificacion de la transferencia:")
monto_nominal = int(input("ingrese el valor a transferir:"))



if "ARS" in codigo:
# aca pondria la operacion matematica con la comision   ars = 5
elif "USD" in codigo:
    usd = 7

else: 
    print("no valido")



importe = 2

monto_base = monto_nominal - importe + ars

    
print(monto_base)