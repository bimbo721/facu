from generador import *

class ConteoPalabras():
    def __init__(self, palabra, cantidad):
        self.palabra = palabra
        self.cantidad = cantidad

    def __str__(self):
        cad = 'Palabra: ' + self.palabra + '  ' + 'Cantidad: ' + str(self.cantidad)
        return cad


def recorrer_fila(mat, fila, palabra):
    total = 0
    cadena = ''
    for col in range(len(mat[0])):
        cadena += mat[fila][col]

    tam = len(palabra)
    for j in range(len(cadena) - tam + 1):
        if cadena[j:j + tam] == palabra:
            total += 1
    return total


def recorrer_columna(mat, col, palabra):
    total = 0
    cadena = ''
    for fila in range(len(mat)):
        cadena += mat[fila][col]

    tam = len(palabra)
    for j in range(len(cadena) - tam + 1):
        if cadena[j:j + tam] == palabra:
            total += 1
    return total


def imprimir(lst):
    for i in range(len(lst)):
        print(lst[i])


def main():
    lista = [
        "libro", "ventana", "cielo", "mariposa", "camino", "esperanza",
        "nube", "sol", "luz", "silencio", "noche", "flor"
    ]
    tablero = generar_matriz(lista)

    listado = []

    for palabra in lista:
        cant = 0

        for fila in range(len(tablero)):
            cant += recorrer_fila(tablero, fila, palabra)

        for col in range(len(tablero[0])):
            cant += recorrer_columna(tablero, col, palabra)

        listado.append(ConteoPalabras(palabra, cant))

    imprimir(listado)

if __name__ == "__main__":
    main()