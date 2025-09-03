def acomodar_vector(v, n):
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if v[i] > v[j]:
                v[i], v[j] = v[j], v[i]


def notas_mayores_x(v, x):
    notas = []

    for i in v:
        if i > x:
            notas.append(i)
    return notas


def busqueda_binaria(v, n, x):
    izq = 0
    der = n - 1

    while izq <= der:
        centro = (izq + der) // 2

        if v[centro] == x:
            return True
        else:
            if v[centro] > x:
                der = centro - 1
            else:
                izq = centro + 1
    return False


def promedio_final(v):
    copia = v[:]
    suma = 0

    del copia[-1]
    del copia[0]

    for i in v:
        suma += i

    n = len(v)

    return suma / n