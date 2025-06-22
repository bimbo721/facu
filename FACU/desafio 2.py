def moneda_esvalida(cod_orden_pago):
    monedas_validas = ("USD", "ARS", "EUR", "GBP", "JPY")
    resultado=False
    for moneda in monedas_validas:
        if moneda in cod_orden_pago:
            resultado=True

    return resultado


def destinatario_valido(cod_destinatario):
    caracteres_validos = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ-"
    cod_destinatario = cod_destinatario.strip()
    resultado=True
    for caracter in cod_destinatario:
        if caracter not in caracteres_validos:
            resultado=False
    return resultado


def porcentaje_operaciones_invalidas(cant_invalidas, cant_ordenes_totales):
    return cant_invalidas * 100 // cant_ordenes_totales
#7
def promedio_final(a,b):#a: total ordenes validas en ARS, b: total de ordenes validas
    return a // b




def principal():
    m = open("C:\Users\joaco\Desktop\codigos.py\FACU\ordenes25.txt")
    texto = m.read()
    contador = 0
    cant_invalidas = 0 #?
    #cant_ordenes_totales = 0
    #hay que poner un contador para contar todas las ordenes,ya sean invalidas o validas
    cant_invalidas_moneda = 0 #?
    cant_invalidas_destinatario = 0
    cant_validas = 0
    suma_monto_final = 0
    cant_usd = 0
    cant_ars = 0
    cant_eur = 0
    cant_gbp = 0
    cant_jpy = 0
    mayor_diferencia = -1
    cod_orden_pago_mayor = ""
    monto_nominal_mayor = 0
    monto_final_mayor = 0
    primer_beneficiario = ""
    contador_beneficiario = 0

    for linea in texto:
        if contador == 0:
            pass
        else:
            if linea[-1] == "\n":
                if primer_beneficiario == "":
                    primer_beneficiario = linea[0:20].strip()

                linea = linea[0:-1]
                nombre = linea[0:20]
                cod_destinatario = linea[20:30]
                cod_orden_pago = linea[30:40]
                monto = linea[40:50]
                alg_comisiones = linea[50:52]
                alg_impuestos = linea[52:54]

                esvalida_moneda = moneda_esvalida(cod_orden_pago)
                esvalido_destinatario = destinatario_valido(cod_destinatario)

                #moneda
                if  not esvalida_moneda :
                   cant_invalidas_moneda+=1
                   
                #tipo de moneda
                if esvalida_moneda:
                    if "USD" in cod_orden_pago:
                        cant_usd += 1
                    elif "ARS" in cod_orden_pago:
                        cant_ars += 1
                    elif "EUR" in cod_orden_pago:
                        cant_eur += 1
                    elif "GBP" in cod_orden_pago:
                        cant_gbp += 1
                    elif "JPY" in cod_orden_pago:
                        cant_jpy += 1

                #destinatario
                if  not esvalido_destinatario and esvalida_moneda:
                    cant_invalidas_destinatario+=1

                #validas
                if esvalida_moneda and esvalido_destinatario:
                    cant_validas+=1
                    #monto mal calculado!!!!!
                    monto_float = float(monto.strip())
                    suma_monto_final = suma_monto_final + monto_float

                monto_nominal = float(monto.strip())
                comision = int(alg_comisiones)
                impuesto = int(alg_impuestos)
                monto_final = monto_nominal * (1 - (comision + impuesto)/100)

                diferencia = monto_nominal - monto_final

                if diferencia > mayor_diferencia:
                    mayor_diferencia = diferencia
                    cod_orden_pago_mayor = cod_orden_pago
                    monto_nominal_mayor = monto_nominal
                    monto_final_mayor = monto_final
                #4
                if linea[0:20].strip() == primer_beneficiario:
                    contador_beneficiario += 1

        contador += 1
    print("La cantidad de operaciones inválidas por moneda no válida es:", cant_invalidas_moneda)
    print("La cantidad de operaciones inválidas por destinatario inválido es:", cant_invalidas_destinatario)
    print("La cantidad de operaciones válidas en total son:", cant_validas)
    print("La suma de montos finales de operaciones válidas:", round(suma_monto_final, 2))
    print("Cantidad de operaciones por moneda válida USD:", cant_usd)
    print("Cantidad de operaciones por moneda válida ARS:", cant_ars)
    print("Cantidad de operaciones por moneda válida EUR:", cant_eur)
    print("Cantidad de operaciones por moneda válida GBP:", cant_gbp)
    print("Cantidad de operaciones por moneda válida JPY:", cant_jpy)
    print("Código de orden de pago:", cod_orden_pago_mayor)
    print("Monto nominal:", round(monto_nominal_mayor, 2))
    print("Monto final:", round(monto_final_mayor, 2))
    print("Diferencia:", round(mayor_diferencia, 2))
    print("Nombre del primer beneficiario encontrado:", primer_beneficiario)
    print("Cantidad de veces que ese beneficiario aparece:", contador_beneficiario)



    m.close()
principal()