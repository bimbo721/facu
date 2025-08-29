def moneda_valida(codigo_orden_pago):
    lista_monedas = ["ARS", "USD", "EUR", "GBP", "JPY"]
    moneda = ""
    hubo_moneda = False
    
    for caracter in lista_monedas:
        if caracter in codigo_orden_pago and hubo_moneda == False:
            moneda = caracter
            hubo_moneda = True
        else:
            if hubo_moneda == True and caracter in codigo_orden_pago:
                moneda = "Moneda incorrecta"
                return moneda
    return moneda



def validez_destinatario(codigo_identificacion_destinatario):
    codigo_identificacion_destinatario = codigo_identificacion_destinatario.strip()
    reglas = ("QWERTYUIOPASDFGHJKLÑZXCVBNM-1234567890")
    bandera_hay_letra = False
    
    for letra in codigo_identificacion_destinatario:
        if letra in reglas:
            if letra != "-":
                bandera_hay_letra = True       
        else:
            return False
    
    if bandera_hay_letra == True:
        return True
    else:
        return False
                
                
    

def calculo_porcentaje(cant_operaciones_invalidas_moneda,cant_operaciones_invalidas_destinatario,contador):
    suma_invalidas = cant_operaciones_invalidas_destinatario + cant_operaciones_invalidas_moneda
    
    return suma_invalidas * 100 // contador
    
    
    
def principal():
    m = open("ordenes25.txt")

    cant_lineas = 0
    moneda = ""
    cant_operaciones_invalidas_moneda = 0
    cant_operaciones_invalidas_destinatario = 0
    cant_operaciones_validas = 0
    suma = 0
    comision = 0
    monto_base = 0
    impuesto = 0
    monto_final = 0
    excedente = 0
    moneditas = ["ARS", "USD", "EUR", "GBP", "JPY"]
    cant_monedas_ars = 0
    cant_monedas_usd = 0
    cant_monedas_eur = 0
    cant_monedas_gbp = 0
    cant_monedas_jpy = 0
    mayor_diferencia = 0
    codigo_orden_pago_mayor = ""
    primer_nombre_destinatario = ""
    primer_nombre = False
    cant_nombre_repetido = 0
    monto_final_ars = 0
    cant_monedas_ars_promedio = 0
    monto_nominal_mayor = 0
    monto_final_mayor = 0
    promedio = 0
    contador = 0
    porcentaje = 0

    for linea in m:
        if contador == 0:
            pass
        elif contador > 0:
            if linea[-1] == "\n":
                if primer_nombre_destinatario == "":
                    primer_nombre_destinatario = linea[0:20].strip()

                linea = linea[0:-1]
                nombre_destinatario = linea[0:20]
                codigo_identificacion_destinatario = linea[20:30]
                codigo_orden_pago = linea[30:40]
                monto_nominal = (linea[40:50])
                identificador_comision = linea[50:52].strip()
                identificador_impositivo = linea[52:54].strip()
                
                monto_nominal = float(monto_nominal.strip())
                
                #llamadas:
                moneda = moneda_valida(codigo_orden_pago)
                destinatario = validez_destinatario(codigo_identificacion_destinatario)
                
                #CALCULO MONTOS BASES:
                if identificador_comision == "1":
                    comision = 9 * monto_nominal / 100

                    
                if identificador_comision == "2":
                    if monto_nominal < 50000:
                        comision = 0
                        
                    elif monto_nominal >= 50000 and monto_nominal < 80000:
                            comision = 5 * monto_nominal / 100
                    
                    elif monto_nominal >= 80000:
                        comision = 7.8 * monto_nominal / 100


                if identificador_comision == "3":
                    if monto_nominal > 25000:
                        comision = 100 + 6 * monto_nominal / 100
                    
                
                if identificador_comision == "4":
                    if monto_nominal <= 100000:
                        comision = 500
                        
                    elif monto_nominal > 100000:
                        comision = 1000
                
                if identificador_comision == "5":
                    if monto_nominal < 500000:
                        comision = 0
                    
                    else:
                        comision = 7 * monto_nominal / 100
                        if comision > 50000:
                            comision = 50000

                
                monto_base = monto_nominal - comision
            
                #CALCULO MONTO FINAL
                if identificador_impositivo == "1":
                    if monto_base <= 300000:
                        impuesto = 0
                    if monto_base > 300000:
                        excedente = monto_base - 300000
                        impuesto = 25 * excedente / 100


                if identificador_impositivo == "2":
                    if monto_base < 50000:
                        impuesto = 50
                    if monto_base >= 50000:
                        impuesto = 100


                if identificador_impositivo == "3":
                    impuesto = 3 * monto_base / 100
                
                
                monto_final = monto_base - impuesto
                
                        
                #r1
                if moneda not in moneditas:
                    cant_operaciones_invalidas_moneda += 1
                        
                #r2
                if destinatario == False:
                    cant_operaciones_invalidas_destinatario += 1
                    
                #r3 y r4
                if moneda in moneditas and destinatario:
                    cant_operaciones_validas += 1
                    suma += monto_final
                
                
                #r5,r6,r7,r8,r9
                if moneda in moneditas:
                    if moneda == "ARS":
                        cant_monedas_ars += 1
                        monto_final_ars += monto_final 
                    if moneda == "USD":
                        cant_monedas_usd += 1
                    if moneda == "EUR":
                        cant_monedas_eur += 1
                    if moneda == "GBP":
                        cant_monedas_gbp += 1
                    if moneda == "JPY":
                        cant_monedas_jpy += 1
                
                

                        
                
                #r10,r11,r12
                diferencia = monto_nominal - monto_final
                
                if diferencia > mayor_diferencia:
                    mayor_diferencia = diferencia
                    codigo_orden_pago_mayor = codigo_orden_pago
                    monto_final_mayor = monto_final
                    monto_nominal_mayor = monto_nominal
                
                #r13
                if primer_nombre == False:
                    primer_nombre_destinatario = nombre_destinatario
                    primer_nombre = True
                
                #r14
                if primer_nombre_destinatario == nombre_destinatario:
                    cant_nombre_repetido += 1
                
                
                if moneda in moneditas and destinatario:
                    if moneda == "ARS":
                        cant_monedas_ars_promedio += 1
                        monto_final_ars += monto_final 
                          
        contador += 1
    #r15
    if (cant_operaciones_invalidas_moneda and cant_operaciones_invalidas_destinatario and cant_lineas) != 0:
        porcentaje = calculo_porcentaje(cant_operaciones_invalidas_moneda,cant_operaciones_invalidas_destinatario,contador)     
    #r16
    if cant_monedas_ars_promedio > 0 and monto_final_ars > 0:
        promedio = monto_final_ars // cant_monedas_ars_promedio
    
    suma = round(suma,2)
    m.close
    print(' (r1) - Cantidad de ordenes invalidas - moneda no autorizada',cant_operaciones_invalidas_moneda)
    print(' (r2) - Cantidad de ordenes invalidas - beneficiario mal identificado',cant_operaciones_invalidas_destinatario)
    print(' (r3) - Cantidad de operaciones validas', cant_operaciones_validas)
    print(' (r4) - Suma de montos finales de operaciones validas',suma)
    print(' (r5) - Cantidad de ordenes para moneda ARS',cant_monedas_ars)
    print(' (r6) - Cantidad de ordenes para moneda USD',cant_monedas_usd)
    print(' (r7) - Cantidad de ordenes para moneda EUR',cant_monedas_eur)
    print(' (r8) - Cantidad de ordenes para moneda GBP',cant_monedas_gbp)
    print(' (r9) - Cantidad de ordenes para moneda JPN',cant_monedas_jpy)
    print('(r10) - Codigo de la orden de pago con mayor diferencia nominal - final:',codigo_orden_pago_mayor)
    print('(r11) - Monto nominal de esa misma orden:',monto_nominal_mayor)
    print('(r12) - Monto final de esa misma orden:',monto_final_mayor)
    print('(r13) - Nombre del primer beneficiario del archivo:',primer_nombre_destinatario)
    print('(r14) - Cantidad de veces que apareció ese mismo nombre:',cant_nombre_repetido)
    print('(r15) - Porcentaje de operaciones inválidas sobre el total:',porcentaje)
    print('(r16) - Monto final promedio de las ordenes validas en moneda ARS:',promedio)
    
principal()