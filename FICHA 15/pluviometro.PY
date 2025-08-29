def promedio_lluvia_anual(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma / 12

def promedio_trimestral(trimestre):
    suma = 0
    for i in trimestre:
        suma += i
    return suma / 3

def meses_muy_lluviosos(mes,lista,prom_anual):
    lista_meses_llovieron_mas = []

    for i in range (1,13):
        if lista[i] >= prom_anual:
            lista_meses_llovieron_mas.append(mes[i])
    return lista_meses_llovieron_mas




def principal():
    lista = []
    mes = ["enero", "febrero", "marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]

    for i in mes:
        a = int(input("ingrese el promedio de lluvias de " + i + ":"))
        lista.append(a)

    seco = lista[0]
    n = len(lista)
    for i in range(1,n):
        if lista[i] < seco:
            seco = lista[i]
            mes_seco = mes[i]


    trimestre = []
    for i in range(0,3):
        b = int(input("ingrese los numeros de los meses del trimestre:"))

        for j in range (1,13):
            if b == j:
                trimestre.append(j)



    promedio_tri = promedio_trimestral(trimestre)
    prom_anual = promedio_lluvia_anual(lista)
    meses_que_llovio_mas = meses_muy_lluviosos(mes,lista,prom_anual)
    print(lista)
    print("1: ", prom_anual)
    print("2: ",mes_seco,"con: ",seco)
    print("3: ",promedio_tri)
    if meses_que_llovio_mas == []:
        print("ningun mes llovio mas que el anual")
    else:
        print("4: ",meses_que_llovio_mas)


principal()