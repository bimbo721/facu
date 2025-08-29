nombre_beneficiario = str(input("ingrese el nombre del beneficiario: "))
codigo_orden_pago = input("ingrese el codigo de identifiacion: ")
monto_nominal = int(input("ingrese la cantidad de dinero a transferir: "))

lista_monedas = ["ARS", "USD", "EUR", "GBP", "JPY"]

moneda = "moneda no autorizada"

for caracter in lista_monedas:
    if caracter in codigo_orden_pago:
        moneda = caracter
        if moneda == "ARS":
            comision = 5
        if moneda == "USD":
            comision = 7
        if moneda == "EUR":
            comision = 7
        if moneda == "GBP":
            comision = 9
        if moneda == "JPY":
            comision = 9


monto_base = monto_nominal - round(comision * monto_nominal / 100 , 2)
descuento = monto_base * 21 // 100



if monto_base > 500000:
    monto_final = monto_base - descuento
    
if monto_base <= 500000:
    monto_final = monto_base



if moneda == "ARS" and (monto_nominal >= 1 and monto_nominal <= 50000):
    comision = monto_nominal * 5 / 100

    
if moneda == "ARS" and (monto_nominal > 50000 and monto_nominal <= 200000):
    comision = monto_nominal * 3.71 / 100
    
    
if moneda == "ARS" and (monto_nominal > 200000 and monto_nominal <= 500000):
    comision = monto_nominal * 2.25 / 100


if moneda == "ARS" and monto_nominal > 500000:
    comision = monto_nominal * 1.80 / 100
    
    
if monto_nominal >= 30000:
    comision += 4000


monto_final = monto_base - comision


print("Beneficiario:", nombre_beneficiario)
print("Moneda:", moneda)
print("Monto base (descontadas las comisiones):", monto_base)
print("Monto final (descontados los impuestos):", monto_final)