import bisect

vector = []


def buscar(v, x):
    izq = 0
    der = len(v) - 1

    while izq <= der:
        centro = (der + izq) // 2

        if v[centro] == x:
            return True
        else:
            if v[centro] > x:
                der = centro - 1
            else:
                izq = centro + 1
    return False

def hay_repetidos(vector):
    vistos = []

    for obj in vector:
        if obj.id in vistos:
            return True
        vistos.add(obj.id)

    return False

#Buscar repetidos entre DOS vectores de objetos
def repetidos(vector1, vector2):

    # Creamos el conjunto vacío
    ids_vector2 = []

    # Recorremos vector2 para guardar los ids
    for obj in vector2:
        id_actual = obj.id
        ids_vector2.add(id_actual)

    resultado = []

    # Recorremos vector1
    for obj in vector1:

        id_actual = obj.id

        # Verificamos si ese id está en el conjunto
        if id_actual in ids_vector2:
            resultado.append(obj)

    return resultado