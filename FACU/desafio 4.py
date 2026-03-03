import os.path
abiertos = "([{"
cierres = ")]}"
opuesto_cierre_apertura = {')': '(', ']': '[', '}': '{'}


def es_apertura(c):
    return c in abiertos


def es_cierre(c):
    return c in cierres


def analizar_expresion(expr):
    pila = []
    profundidad_max = 0
    pares_formados = 0

    for i in range(len(expr)):
        c = expr[i]
        pos = i + 1

        if es_apertura(c):
            pila.append((c, pos))
            if len(pila) > profundidad_max:
                profundidad_max = len(pila)

        elif es_cierre(c):
            if len(pila) == 0:
                return "Sobran cierres", 0, 0, pos

            tope, posi_tope = pila.pop()

            if opuesto_cierre_apertura[c] != tope:
                return "Desequilibrio interno", 0, 0, pos
            pares_formados += 1


    if len(pila) != 0:
        simbolo , pos_pendiente = pila[-1]
        return "Sobran aperturas", 0, 0, pos_pendiente

    return "Ok", profundidad_max, pares_formados, 0


def procesar_archivo(archivo):
    m = open(archivo, 'rt')
    numero_linea = 1

    for linea in m:
        if len(linea) > 0 and linea[-1] == '\n':
            expr = linea[:-1]
        else:
            expr = linea

        estado, profundidad, pares, posi_error = analizar_expresion(expr)

        if estado == "Ok":
            print("Línea " + str(numero_linea) + ": " + estado + ". Posición del conflicto: " + str(posi_error) + ".")
        else:
            print("Línea", numero_linea, ":", estado, ". Posición del conflicto:", posi_error, ".")

        numero_linea += 1

    m.close()


def principal():
    archivo = "expresiones.txt"
    if not os.path.exists(archivo):
        print("no se encontro el archivo ")
    else:
        procesar_archivo(archivo)


if __name__ == "__main__":
    principal()