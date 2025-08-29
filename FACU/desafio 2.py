def ordenar_ascendente(lista):
    numero = len(lista)
    for i in range(numero - 1):
        for j in range(i + 1, numero):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]


def ordenar_descendente(lista):
    numero = len(lista)
    for i in range(numero - 1):
        for j in range(i + 1, numero):
            if lista[i] < lista[j]:
                lista[i], lista[j] = lista[j], lista[i]


def numero_a_lista(numero):
    lista = []
    while numero > 0:
        lista.insert(0, numero % 10)
        numero //= 10
    return lista


def lista_a_numero(lista):
    num = 0
    for d in lista:
        num = num * 10 + d
    return num


def kaprekar(numero):
    lista = numero_a_lista(numero)
    ordenar_descendente(lista)
    mayor = lista_a_numero(lista)
    ordenar_ascendente(lista)
    menor = lista_a_numero(lista)
    return mayor - menor


def procesar_numero(numero):
    numeros_vistos = []
    pasos = 0
    actual = numero
    while actual not in numeros_vistos:
        numeros_vistos.append(actual)
        pasos += 1
        actual = kaprekar(actual)
    ciclo_len = pasos - numeros_vistos.index(actual)
    return actual, pasos, ciclo_len



cant_6174 = 0
cant_0 = 0
cant_iteraciones = 0
max_ciclo = 0


for num in range(1000, 10000):
    final, pasos, ciclo = procesar_numero(num)
    cant_iteraciones += pasos
    if final == 6174:
        cant_6174 += 1
    elif final == 0:
        cant_0 += 1
    if ciclo > max_ciclo:
        max_ciclo = ciclo


promedio = cant_iteraciones // 9000

print("cantidad de veces que el proceso se detuvo en 6174:", cant_6174)
print("cantidad de veces que se detuvo en 0:", cant_0)
print("longitud del ciclo mas largo:", max_ciclo)
print("promedio de iteraciones:", promedio)