#numero_entero = int(input("ingrese le numero:"))
#print(numero_entero)


beneficiario = input("Ingrese el nombre de la persona a transferir:")
codigo = input("ingrese el codigo de identificacion de la transferencia:")
monto_nominal = int(input("ingrese el valor a transferir:"))



if "ARS" in codigo:
    comision=monto_nominal*5/100
    monto_base = int(monto_nominal - comision)
    moneda="ARS"
    if monto_base>5000:
        descuento=monto_base*0.21
        monto_final= int(monto_base-descuento)
    else: monto_final=monto_base
    
print(monto_base)