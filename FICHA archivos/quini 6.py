import pickle

def acomodar_vector(v):
    n = len(v)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if v[i] > v[j]:
                v[i] , v[j] = v[j] , v[i]


def principal():
    numeros_sorteados = []
    for i in range(6):
        numero = int(input("ingrese el numero sorteado:"))

        while numero > 36 or numero < 0:
            numero = int(input("error,por favor que este dentro del rango:"))
        numeros_sorteados.append(numero)

    acomodar_vector(numeros_sorteados)

    m = open("extracto.dat","wb")
    pickle.dump(numeros_sorteados,m)
    m.close()

    m = open("extracto.dat","rb")
    lista = pickle.load(m)
    m.close()

    print("archivos recuperados:",lista)

principal()