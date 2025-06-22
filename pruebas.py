def moneda_esvalida(cod_orden_pago):
    monedas_validas = ("USD", "ARS", "EUR", "GBP", "JPY")
    resultado = False
    for moneda in monedas_validas:
        if moneda in cod_orden_pago:
            resultado = True
    return resultado


def destinatario_valido(cod_destinatario):
    caracteres_validos = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ-"
    resultado = True
    for caracter in cod_destinatario:
        if caracter not in caracteres_validos:
            resultado = False
    return resultado


def porcentaje_operaciones_invalidas(cant_invalidas, cant_ordenes_totales):
    return cant_invalidas * 100 // cant_ordenes_totales


def promedio_final(suma_final_ars, cant_final_ars):
    return suma_final_ars // cant_final_ars


def principal():
    texto = open("ordenes25.txt")
    contador_lineas = 0
    cant_invalidas_moneda = 0
    cant_invalidas_destinatario = 0
    cant_ordenes_validas = 0
    suma_monto_final_validas = 0
    cant_usd = 0
    cant_ars = 0
    cant_eur = 0
    cant_gbp = 0
    cant_jpy = 0
    mayor_diferencia = -1
    cod_orden_mayor = ""
    monto_nominal_mayor = 0
    monto_final_mayor = 0
    primer_beneficiario = ""
    contador_beneficiario = 0
    suma_final_ars = 0
    cant_final_ars = 0

    for linea in texto:
        if contador_lineas == 0:
            contador_lineas += 1
            continue

        if linea[-1] == "\n":
            linea = linea[:-1]

        nombre = linea[0:20]
        cod_destinatario = linea[20:30]
        cod_orden_pago = linea[30:40]
        monto = linea[40:50]
        comisiones = linea[50:52]
        impuestos = linea[52:54]

        if primer_beneficiario == "":
            primer_beneficiario = nombre.strip()

        if nombre.strip() == primer_beneficiario:
            contador_beneficiario += 1

        esvalida_moneda = moneda_esvalida(cod_orden_pago)
        esvalido_destinatario = destinatario_valido(cod_destinatario.strip())

        if not esvalida_moneda:
            cant_invalidas_moneda += 1
        elif not esvalido_destinatario:
            cant_invalidas_destinatario += 1
            
        #aca no va un if para "si una orden es inválida por ambos motivos, debe contarse como moneda no autorizada".


        # la 3) contar por tipo de moneda
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

        #la 4)
        monto_nominal = float(monto.strip())
        comision = int(comisiones.strip())
        impuesto = int(impuestos.strip())
        monto_final = monto_nominal * (1 - (comision + impuesto) / 100)

        # diferencia
        diferencia = monto_nominal - monto_final
        if diferencia > mayor_diferencia:
            mayor_diferencia = diferencia
            cod_orden_mayor = cod_orden_pago
            monto_nominal_mayor = monto_nominal
            monto_final_mayor = monto_final

        #la 2)
        if esvalida_moneda and esvalido_destinatario:
            cant_ordenes_validas += 1
            suma_monto_final_validas += monto_final
            if "ARS" in cod_orden_pago:
                suma_final_ars += monto_final
                cant_final_ars += 1

        contador_lineas += 1

    cant_total_ordenes = contador_lineas - 1 
    cant_invalidas_totales = cant_invalidas_moneda + cant_invalidas_destinatario
    porcentaje = porcentaje_operaciones_invalidas(cant_invalidas_totales, cant_total_ordenes)

    if cant_final_ars > 0:
        promedio_ars = promedio_final(int(suma_final_ars), cant_final_ars)
    else:
        promedio_ars = 0

    print("La cantidad de operaciones inválidas por moneda no válida es:", cant_invalidas_moneda)
    print("La cantidad de operaciones inválidas por destinatario inválido es:", cant_invalidas_destinatario)
    print("La cantidad de operaciones válidas en total son:", cant_ordenes_validas)
    print("La suma de montos finales de operaciones válidas:", round(suma_monto_final_validas, 2))
    print("Cantidad de operaciones por moneda válida USD:", cant_usd)
    print("Cantidad de operaciones por moneda válida ARS:", cant_ars)
    print("Cantidad de operaciones por moneda válida EUR:", cant_eur)
    print("Cantidad de operaciones por moneda válida GBP:", cant_gbp)
    print("Cantidad de operaciones por moneda válida JPY:", cant_jpy)
    print("Código de orden de pago:", cod_orden_mayor)
    print("Monto nominal:", round(monto_nominal_mayor, 2))
    print("Monto final:", round(monto_final_mayor, 2))
    print("Nombre del primer beneficiario encontrado:", primer_beneficiario)
    print("Cantidad de veces que ese beneficiario aparece:", contador_beneficiario)
    print("Porcentaje de operaciones inválidas sobre el total:", porcentaje, "%")
    print("Promedio de monto final en ARS entre órdenes válidas:", promedio_ars)

    texto.close()


principal()
