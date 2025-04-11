beneficiario = input("Ingrese el nombre de la persona a transferir:")
codigo = input("ingrese el codigo de identificacion de la transferencia:")
monto_nominal = int(input("ingrese el valor a transferir:"))



if "ARS" in codigo:
    comision=monto_nominal*5/100
    monto_base = monto_nominal - comision
    moneda="ARS"
    if monto_base>5000:
        descuento=monto_base*0.21
        monto_final= int(monto_base-descuento)
    else: monto_final=monto_base

else:
    if "USD" in codigo:
        comision = monto_nominal * 7 / 100
        monto_base = int(monto_nominal - comision)
        moneda= "USD"
        if monto_base > 5000:
            descuento = monto_base * 0.21
            monto_final = monto_base - descuento
        else:
            monto_final = monto_base
    else:
        if "EUR" in codigo:
            comision = monto_nominal * 7 / 100
            monto_base = monto_nominal - comision
            moneda= "EUR"
            if monto_base > 5000:
                descuento = monto_base * 0.21
                monto_final = monto_base - descuento
            else:
                monto_final = monto_base
        else:
            if "JPY" in codigo:
                comision = monto_nominal * 9 / 100
                monto_base= monto_nominal - comision
                moneda= "JPY"
                if monto_base > 5000:
                    descuento = monto_base * 0.21
                    monto_final = monto_base - descuento
                else:
                    monto_final = monto_base
            else:
                 if "GPB" in codigo:
                     comision = monto_nominal * 9 / 100
                     monto_base= monto_nominal - comision
                     moneda = "GPB"
                     if monto_base > 5000:
                         descuento = monto_base * 0.21
                         monto_final = monto_base - descuento
                     else:
                         monto_final = monto_base
                 else: print("No es valido")



print("Beneficiario:", beneficiario)
print("Moneda:", moneda)
print("Monto base (descontadas las comisiones):", monto_base)
print("Monto final (descontados los impuestos):", monto_final)