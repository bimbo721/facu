import pickle
import os.path

def apartado_5(matriz):
    pass


def apartado_4(matriz): #esta mal
    filas = len(matriz)
    mayor_monto = 0
    dia = 0

    for f in range(filas):
        for c in range(len(matriz[f])):
            if matriz[f][c] > mayor_monto:
                mayor_monto = matriz[f][c]
                dia = c

    print("dia con mayor monto:",dia+1, "total:",mayor_monto)


def apartado_3():
    fila = 15
    columna = 31
    matri = [0] * fila

    for c in range(fila):
        matri[c] = [0] * columna

    m = open("archivo de cobros.dat","rb")
    tamaño = os.path.getsize("archivo de cobros.dat")

    while m.tell() < tamaño:
        dia = pickle.load(m)
        tipo = pickle.load(m)
        monto = pickle.load(m)
        cuenta = pickle.load(m)

        for j in range(fila):
            for k in range(columna):
                if tipo-1 == j and dia-1 == k:
                    matri[j][k] += monto
    m.close()
    return matri


def buscar_monto():
    m = open("archivo de cobros.dat","rb")
    x = int(input("determinar monto total de x cuenta: "))
    monto_final = 0
    tamaño = os.path.getsize("archivo de cobros.dat")

    while m.tell() < tamaño:
        dia = pickle.load(m)
        tipo = pickle.load(m)
        monto = pickle.load(m)
        cuenta = pickle.load(m)

        if x == cuenta:
            monto_final += monto

    if monto_final == 0:
        print("no se encontro la cuenta")
    else:
        print("monto final de la cuenta x:",monto_final)

    m.close()


def mostrar_archivo():
    m = open("archivo de cobros.dat","rb")
    dia = pickle.load(m)
    tipo = pickle.load(m)
    monto = pickle.load(m)
    numero_cuenta = pickle.load(m)

    tamaño = os.path.getsize("archivo de cobros.dat")
    while m.tell() < tamaño:
        print("dia:",dia)
        print("tipo:",tipo)
        print("monto:",monto)
        print("numero de cuenta:",numero_cuenta)
    m.close()


def crear_archivo():
    print("ingrese el nuevo cobro al archivo")
    dia = int(input("ingrese el dia que se cobró: "))
    tipo = int(input("ingrese el tipo de servicio: "))
    while tipo >15 or tipo < 0:
        tipo = int(input("error,ingrese el valor correcto: "))

    monto = int(input("ingrese el monto: "))
    numero_cuenta = int(input("ingrese el numero de cuenta: "))

    m = open("archivo de cobros.dat","ab")
    pickle.dump(dia,m)
    pickle.dump(tipo,m)
    pickle.dump(monto,m)
    pickle.dump(numero_cuenta,m)
    m.close()


def principal():
    op = 0
    matriz = None
    while op != 6:
        print("opcion 1)")
        print("opcion 2)")
        print("opcion 3)")
        print("opcion 4)")
        print("opcion 5)")
        print("opcion 6) salir")
        op = int(input("ingrese la opcion a elegir: "))

        if op == 1:
            crear_archivo()

        elif op == 2:
            buscar_monto()

        elif op == 3:
            matriz = apartado_3()
            print("matriz:", matriz)

        elif op == 4:
            if matriz is None:
                matriz = apartado_3()
            apartado_4(matriz)

        elif op == 5:
            if matriz is None:
                matriz = apartado_3()
            apartado_5(matriz)

        elif op == 6:
            print("chau")


principal()