def moneda_esvalida(cod_orden_pago):
    monedas_validas = ("USD", "ARS", "EUR", "GBP", "JPY")
    resultado=False
    for moneda in monedas_validas:
        if moneda in cod_orden_pago:
            resultado=True
    return resultado

def destinatario_valido(cod_destinatario):
    destinatariovalidos = ("0123456789", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "")
    resultado=False
    for destinatario in destinatariovalidos:
        if destinatario in cod_destinatario:
            resultado=True
    return (resultado)

def suma(cant_validas, monto):
    for cantidad in cant_validas:
        suma = sum(round(monto,2))
    return suma
    


def principal():
    m = open("c:/Users/joaco/Desktop/codigos.py/FACU/ordenes25.txt")
    contador = 0
    d = 0
    cant_validas = 0
    cant_invalidas = 0
    cant_invalidas_orden = 0
    cantidad_total_invalidas = cant_invalidas_orden + cant_validas
    
    for linea in m:
        if (contador==0):
            pass
        elif (contador>0):
            if linea[-1] == "\n":
                linea = linea[0:-1]
                nombre = linea[0:20]
                cod_destinatario = linea[20:30]
                cod_orden_pago = linea[30:40]
                monto = linea[40:50]
                alg_comisiones = linea[50:52]
                alg_impuestos = linea[52:54]
                
                esvalida_moneda = moneda_esvalida(cod_orden_pago)
                if not esvalida_moneda:
                    cant_invalidas_orden+=1
                    cant_invalidas += 1
                    
                para_sumar = suma(cant_validas, monto)
                cantidad_total_invalidas += para_sumar
                
                esvalido_destinatario= destinatario_valido(cod_destinatario)
                if not esvalido_destinatario:
                    cant_invalidas_destinatario+=1
                    cant_invalidas+=1
                    
        
        contador += 1
        
    print("La cantidad de operaciones invalidas por moneda no valida es: ", cant_invalidas_orden)
    #print("La cantidad de operaciones invalidas por destinatario invalido es: ", cant_invalidas_destinatario)
    print("cant total:",cantidad_total_invalidas)
    m.close()
principal()