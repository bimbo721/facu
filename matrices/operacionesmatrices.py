#crear matriz
def crear_matriz():
    n = 5
    m = 6

    matriz = [None] * n #cantidad de filas
    for c in range(n):
        matriz[c] = [None] * m #cantidad de columnas


# un recorrido por filas
def recorrer_filas(matriz):
    for f in range(len(matriz)):
        for c in range(len(matriz[f])): #devuelve la cantidad de
            matriz[f][c] = 0            # objetos(de esa fila) como
                                        # si fuera una lista basicamente
    # si quiero poner un valor cargado por
    # teclado solamente cambio el 0 por input


#recorrido por columnas en matriz regulas(n=m) y se sabe m
def recorrer_columnas(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])

    for c in range(columnas):
        for f in range(filas):
            matriz[f][c] = 0


################################# ordenar matrices
def insercion_directa(v):
    n = len(v)

    for j in range(1,n):
        y = v[j]
        k = j-1
        while k >= 0 and y < v[k]:
            v[k+1] = v[k]
            k -= 1
        v[k+1] = y


def shell_sort(v):
    n = len(v)
    h = 1
    while h <= n // 9:
        h = 3 * h + 1
    while h > 0:
        for j in range(h, n):
            y = v[j]
            k = j - h
            while k >= 0 and y < v[k]:
                v[k+h] = v[k]
                k -= h
            v[k+h] = y
        h //= 3