import random
import string


def insertar_horizontal(palabra, matriz):
    n = len(matriz)
    intentos = 0
    while intentos < 100:
        f = random.randint(0, n - 1)
        c = random.randint(0, n - len(palabra))

        if all(matriz[f][c + i] in string.ascii_lowercase for i in range(len(palabra))):
            for i, letra in enumerate(palabra):
                matriz[f][c + i] = letra
            return True
        intentos += 1
    return False


def insertar_vertical(palabra, matriz):
    n = len(matriz)
    intentos = 0
    while intentos < 100:
        fila = random.randint(0, n - len(palabra))
        col = random.randint(0, n - 1)


        if all(matriz[fila + i][col] in string.ascii_lowercase for i in range(len(palabra))):
            for i, letra in enumerate(palabra):
                matriz[fila + i][col] = letra
            return True
        intentos += 1
    return False



def generar_matriz(palabras, semilla=159733):
    n = 64

    random.seed(semilla)
    matriz = [[random.choice(string.ascii_lowercase) for c in range(n)] for f in range(n)]


    for palabra in palabras:

        repeticiones = random.randint(0, 8)
        for i in range(repeticiones):
            if random.choice([True, False]):
                insertar_horizontal(palabra, matriz)
            else:
                insertar_vertical(palabra, matriz)

    return matriz


def mostrar_matriz(mat):
    print("Contenido de la matriz:\n", "[")
    for f in range(len(mat)):
        print("\t", mat[f])
    print("]")


def prueba():
    palabras = [
                   "libro", "ventana", "cielo", "mariposa", "camino", "esperanza",
                   "nube", "sol", "luz", "silencio", "noche", "flor"
    ]

    mat = generar_matriz(palabras)
    mostrar_matriz(mat)
    palabra_horizontal = mat[5][5:15]
    print(palabra_horizontal)

    fila = 3
    palabra_vertical = []
    for i in range(10):
        palabra_vertical.append(mat[fila + i][3])
    print(palabra_vertical)


if __name__ == '__main__':
    prueba()

