beneficiario = input("Ingrese el nombre de la persona a transferir:")
codigo = input("ingrese el codigo de identificacion de la transferencia:")
monto_nominal = int(input("ingrese el valor a transferir:"))



if "ARS" in codigo:
    moneda = "Peso argentino"
    if (monto_nominal>1) and (monto_nominal<50000):
        comision= monto_nominal*5/100
        if (monto_nominal>=30000):
            comision+=4000
    if (monto_nominal>50000) and (monto_nominal<=200000):
        comision=monto_nominal*3.71/100
        comision += 4000
    if (monto_nominal>200000) and (monto_nominal<=500000):
        comision= monto_nominal*2.25/100
        comision += 4000
    if(monto_nominal>500000):
        comision=monto_nominal*1.80/100
        comision += 4000


    if (comision > 300000):
        comision = 300000
        print("ENTRO a la comision>30000")

    monto_base = round((monto_nominal - comision), 2)

    if monto_base > 500000:
        descuento = monto_base * 0.21
        monto_final = monto_base - descuento
    else:
     monto_final = monto_base

else:
    if "USD" in codigo:
        comision = monto_nominal * 7 / 100
        monto_base = round((monto_nominal - comision), 2)
        moneda= "Dolares"
        if monto_base >  500000:
            descuento = monto_base * 0.21
            monto_final = monto_base - descuento
        else:
            monto_final = monto_base
    else:
        if "EUR" in codigo:
            comision = ( monto_nominal * 7 / 100)
            monto_base = round((monto_nominal - comision), 2)
            moneda= "Euro"
            if monto_base >  500000:
                descuento = monto_base * 0.21
                monto_final = monto_base - descuento
            else:
                monto_final = monto_base
        else:
            if "JPY" in codigo:
                comision = monto_nominal * 9 / 100
                monto_base = round((monto_nominal - comision), 2)
                moneda= "Yen"
                if monto_base >  500000:
                    descuento = monto_base * 0.21
                    monto_final = monto_base - descuento
                else:
                    monto_final = monto_base
            else:
                 if "GPB" in codigo:
                     comision = monto_nominal * 9 / 100
                     monto_base = round((monto_nominal - comision), 2)
                     moneda = "Libra"
                     if monto_base >  500000:
                         descuento = monto_base * 0.21
                         monto_final = monto_base - descuento
                     else:
                         monto_final = monto_base
                 else:
                     monto_base= 0
                     moneda= "No es valida"
                     monto_final= 0



print("Beneficiario:", beneficiario)
print("Moneda:", moneda)
print("Monto base (descontadas las comisiones):", monto_base)
print("Monto final (descontados los impuestos):", monto_final)