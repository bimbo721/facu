import bisect
from clase_ventas import *

#compara 2 objetos,en este caso se compara cada objeto del vector con
#el objeto (venta) actual para comprobar si tienen los mismos datos en los atributos
def comprar_objetos(vec,venta):
    for i in vec:
        if vars(venta) == vars(i):
            return True
    return False


def mostrar_resultados(cant_validas,cant_invalidas,duplicados_igual,duplicado_conflictivo,
                       dinero_ok,v_dia,v_sku,cliente_top):
    print("VALIDAS:", cant_validas)
    print("INVALIDAS:", cant_invalidas)
    print("DUPLICADO_IGUAL:", duplicados_igual)
    print("DUPLICADO_CONFLICTIVO:", duplicado_conflictivo)
    print("TOTAL_OK: $",dinero_ok)
    print("POR_DIA:")
    for fila in v_dia:
        print("fecha:",fila)
    print("TOP_SKU:")
    for i in range(len(v_sku)):
        print("top",i+1,":",v_sku[i])
    print("TOP_CLIENTE:", cliente_top[0])


#busqueda binaria para comprobar la existencia de un pedido_id repetido
def buscar(v, x):
    izq = 0
    der = len(v) - 1

    while izq <= der:
        centro = (der + izq) // 2

        if v[centro].id == x:
            return True
        else:
            if v[centro].id > x:
                der = centro - 1
            else:
                izq = centro + 1
    return False



def validar_linea(venta):
    talles = ["M","L","S","XL","XXL"]
    colores = ["AZUL","NEGRO","BLANCO","ROJO","VERDE","GRIS"]


    if venta.fecha[0:4] != "2026":
        return False

    if venta.talle not in talles:
        return False

    if venta.color not in colores:
        return False

    if venta.estado != "OK" and venta.estado != "CANCELADO":
        return False

    if venta.cant < 0:
        return False

    if venta.precio < 0:
        return False

    return True


#determina el cliente que mas compro, devolviendo el nombre y el monto
def top_c(v_cliente):
    maximo = v_cliente[0][1]
    fila_maxima = v_cliente[0]

    for i in range(1, len(v_cliente)):
        fila_actual = v_cliente[i]
        valor_actual = fila_actual[1]

        if valor_actual > maximo:
            maximo = valor_actual
            fila_maxima = fila_actual

    return fila_maxima



def abrir_archivo(vector):
    arch = open("ventass.txt","rt")
    duplicados_igual = 0
    duplicado_conflictivo = 0
    cant_validas = 0
    cant_invalidas = 0
    dinero_ok = 0
    v_dia = []
    v_cliente = []
    v_sku = []
    cant_vueltas = 0


    for linea in arch:
        linea = linea.strip("\n")
        lista = linea.split(";")

        fecha = str(lista[0])
        id_pedido = lista[1]
        cliente = str(lista[2])
        sku = lista[3]
        talle = lista[4]
        color = lista[5]
        cantidad = int(lista[6])
        precio = int(lista[7])
        estado = lista[8]


        venta = Ticket(fecha,id_pedido,cliente,sku,talle,color,cantidad,precio,estado)


        if validar_linea(venta) is True:


            if buscar(vector,venta.id) is True:
                #si existe el id repetido entonces:
                if comprar_objetos(vector,venta) is True:
                    duplicados_igual += 1
                    continue
                else:
                    duplicado_conflictivo += 1
                    cant_invalidas += 1
                    continue


            if venta.estado == "OK":
                dinero_ok += venta.precio

            #estas son banderas para comprobar la existencia de un elemento en los correspondientes vectores
            band_dia = False
            band_cliente = False
            band_sku = False


            fecha = venta.fecha[0:10]
            if not vector:
                v_dia.append([fecha, venta.precio])
                v_cliente.append([venta.cliente, venta.precio])
                v_sku.append([venta.sku, venta.cant])
                cant_validas += 1
                bisect.insort(vector,venta)
                continue


            #a continuacion respectivamente:dia y dinero recaudado, cliente y dinero recaudado,
            #cantidad de unidades por sku
            for i in range(len(v_dia)):
                if fecha == v_dia[i][0]:
                    v_dia[i][1] += venta.precio
                    band_dia = True
                    break

            for i in range(len(v_cliente)):
                if venta.cliente == v_cliente[i][0]:
                    v_cliente[i][1] += venta.precio
                    band_cliente = True
                    break

            for i in range(len(v_sku)):
                if venta.sku == v_sku[i][0]:
                    v_sku[i][1] += venta.cant
                    band_sku = True
                    break


            if not band_dia:
                v_dia.append([fecha, venta.precio])
            if not band_cliente:
                v_cliente.append([venta.cliente, venta.precio])
            if not band_sku:
                v_sku.append([venta.sku, venta.cant])


            cant_validas += 1
            bisect.insort(vector, venta)

    #acomoda el v_sku de forma descendente segun la columna[1]
    v_sku.sort(key=lambda fila: fila[1], reverse=True)

    cliente_top = top_c(v_cliente)

    mostrar_resultados(cant_validas,cant_invalidas,duplicados_igual,duplicado_conflictivo,
                       dinero_ok,v_dia,v_sku,cliente_top)


    #si tuviera que mejorar algo seria de la linea 140 a 181
    #debido a que no me enseñaron el manejo de diccionarios
