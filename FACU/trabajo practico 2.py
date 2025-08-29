def moneesvalida(cod_orden_pago):
    monedas_validas = ("USD", "ARS", "EUR", "GBP", "JPY")
    resultado = False
    cont_monedas = 0
    es_usd= es_ars= es_eur= es_gbp= es_jpy=False
    for moneda in monedas_validas:
        if moneda in cod_orden_pago:
            #resultado=True
            #esto esta agregado
            if moneda == "USD":
                es_usd=True
            if moneda == "ARS":
                es_ars=True
            if moneda == "EUR":
                es_eur=True
            if moneda == "GBP":
                es_gbp=True
            if moneda == "JPY":
                es_jpy=True

    if es_usd and not (es_jpy or es_gbp or es_ars or es_eur):
        resultado = True
    elif es_jpy and not (es_usd or es_gbp or es_ars or es_eur):
        resultado = True
    elif es_gbp and not (es_jpy or es_usd or es_ars or es_eur):
        resultado = True
    elif es_ars and not (es_jpy or es_gbp or es_usd or es_eur):
        resultado = True
    elif es_eur and not (es_jpy or es_gbp or es_ars or es_usd):
        resultado = True
    else:
        resultado= False
        #termina lo agregado
    return resultado


def destinatario_valido(cod_destinatario):
    caracteres_validos = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ-"
    cod_destinatario = cod_destinatario.strip()
    resultado = True
    for caracter in cod_destinatario:
        if caracter not in caracteres_validos:
            resultado = False
    return resultado


def calculo_monto_final(mon_base, num):
    impuesto = 0
    if num == '1':
        if mon_base <= 300000:
            impuesto = 0
        else:
            excedente = mon_base - 300000
            impuesto = 25 * excedente // 100
    elif num == "2":
        if mon_base < 50000:
            impuesto = 50
        else:
            impuesto = 100
    elif num == "3":
        impuesto = mon_base * 3 // 100
    elif num == "4" or num == "5":
        impuesto = 0
    return mon_base - impuesto


def porcentaje_invalidas(cont_inv, cont_total):
    return cont_inv * 100 // cont_total

def calculo_monto_base(monto_nominal,alg_com):
    monto_base = 0
    if alg_com == "1":
        monto_base = monto_nominal - (monto_nominal * 9 // 100)
    elif alg_com == "2":
        if monto_nominal < 50000:
            comision_USD = 0
        elif monto_nominal < 80000:
            comision_USD = 5 * monto_nominal // 100
        else:
            comision_USD = 7.8 * monto_nominal // 100
        monto_base = monto_nominal - comision_USD
    elif alg_com == "3":
        if monto_nominal > 25000:
            comision_EUR = 6 * monto_nominal // 100
        monto_base = monto_nominal - (100 + comision_EUR)
    elif alg_com == "4":
        if monto_nominal <= 100000:
            comision_JPY = 500
        else:
            comision_JPY = 1000
        monto_base = monto_nominal - comision_JPY
    elif alg_com == "5":
        if monto_nominal < 500000:
            comision_ARS = 0
        else:
            comision_ARS = 7 * monto_nominal // 100
        if comision_ARS > 50000:
            comision_ARS = 50000
        monto_base = monto_nominal - comision_ARS
    elif alg_com == "6":
        if monto_nominal <= 10000:
            comision_USD = 0
        elif monto_nominal <= 20000:
            comision_USD = 300
        else:
            comision_USD = monto_nominal * 3 // 100
        monto_base = monto_nominal - comision_USD
    elif alg_com == "7" or alg_com == "8":
        monto_base = monto_nominal

    return monto_base



def principal():
    m = open("ordenes25.txt")
    contador = contador_invalidas = 0
    r1 = r2 = r3 = r4 = r5 = r6 = r7 = r8 = r9 = r10 = r11 = r12 = r14 = r15 = r16 = 0
    mayor_diferencia = -1
    cod_orden_pago_mayor = ""
    monto_nominal_mayor = 0
    monto_final_mayor = 0
    comision_USD = 0
    comision_EUR = 0
    comision_ARS = 0
    comision_GBP = 0
    comision_JPY = 0
    monto_final = 0
    acum_monto_final_ARS = cont_ARS = 0
    r13 = ""

    for linea in m:
        if contador == 0:
            pass
        elif contador > 0:
            if linea[-1] == "\n":
                if r13 == "":
                    r13 = linea[0:20].strip()
                linea = linea[0:-1]
                nombre = linea[0:20]
                cod_destinatario = linea[20:30]
                cod_orden_pago = linea[30:40]
                monto = linea[40:50]
                alg_comisiones = linea[50:52]
                alg_impuestos = linea[52:54]

                moneda_es_valida = moneesvalida(cod_orden_pago)
                destinatario_es_valido = destinatario_valido(cod_destinatario)
                if not moneda_es_valida:
                    r1 += 1
                if not destinatario_es_valido and moneda_es_valida:
                    r2 += 1
                if moneda_es_valida and destinatario_es_valido:
                    r3 += 1

                monto_nominal = float(monto.strip())

                if moneda_es_valida:
                    if "USD" in cod_orden_pago:
                        r6 += 1

                    elif "ARS" in cod_orden_pago:
                        r5 += 1



                    elif "EUR" in cod_orden_pago:
                        r7 += 1

                    elif "GBP" in cod_orden_pago:
                        r8 += 1

                    elif "JPY" in cod_orden_pago:
                        r9 += 1


                    monto_base = calculo_monto_base(monto_nominal,alg_comisiones.strip())
                    monto_final = calculo_monto_final(monto_base,alg_impuestos.strip())

                if moneda_es_valida and destinatario_es_valido and "ARS" in cod_orden_pago:
                    acum_monto_final_ARS += monto_final
                    cont_ARS += 1

                if not moneda_es_valida:
                    monto_nominal=0
                    monto_final=0

                diferencia = monto_nominal - monto_final



                if diferencia > mayor_diferencia:

                    mayor_diferencia = diferencia
                    r10 = cod_orden_pago
                    r11 = monto_nominal
                    r12 = monto_final


                if nombre.strip() == r13:
                    r14 += 1
                if moneda_es_valida and destinatario_es_valido:
                    r4 += monto_final

                if not moneda_es_valida or not destinatario_es_valido:
                    contador_invalidas += 1
        contador += 1

    r4 = round(r4, 2)
    r15 = porcentaje_invalidas(contador_invalidas, contador - 1)
    r16 = acum_monto_final_ARS // cont_ARS if cont_ARS else 0
    m.close()


    print(' (r1) - Cantidad de ordenes invalidas - moneda no autorizada:', r1)
    print(' (r2) - Cantidad de ordenes invalidas - beneficiario mal identificado:', r2)
    print(' (r3) - Cantidad de operaciones validas:', r3)
    print(' (r4) - Suma de montos finales de operaciones validas:', r4)
    print(' (r5) - Cantidad de ordenes para moneda ARS:', r5)
    print(' (r6) - Cantidad de ordenes para moneda USD:', r6)
    print(' (r7) - Cantidad de ordenes para moneda EUR:', r7)
    print(' (r8) - Cantidad de ordenes para moneda GBP:', r8)
    print(' (r9) - Cantidad de ordenes para moneda JPN:', r9)
    print('(r10) - Codigo de la orden de pago con mayor diferencia nominal - final:', r10)
    print('(r11) - Monto nominal de esa misma orden:', r11)
    print('(r12) - Monto final de esa misma orden:', r12)
    print('(r13) - Nombre del primer beneficiario del archivo:', r13)
    print('(r14) - Cantidad de veces que apareció ese mismo nombre:', r14)
    print('(r15) - Porcentaje de operaciones inválidas sobre el total:', r15)
    print('(r16) - Monto final promedio de las ordenes validas en moneda ARS:', r16)

principal()