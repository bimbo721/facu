import os.path
import pickle
from clase import *


def validar(op):
    permitidos = ['0', '1', '2', '3', '4']
    while True:
        op = op.strip()
        if len(op) == 1 and op in permitidos:
            return op
        op = input('Error: se pidio que cargue un numero entre 0 y 2: ')


# -------------------------------r1------------------------------
def procesar_archivo_csv(v):
    m = open("envios.csv", "rt")

    for linea in m:
        obj = generar_envio(linea)
        inserccion_ordenada(v, obj)

    m.close()


def inserccion_ordenada(v, o):
    n = len(v)
    pos = n
    izq, der = 0, n - 1
    while izq <= der:
        c = (izq + der) // 2
        if v[c].identificacion_destinatario == o.identificacion_destinatario:
            pos = c
            break
        if o.identificacion_destinatario > v[c].identificacion_destinatario:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq
    v[pos:pos] = [o]


##################
def buscar_valor(v, i):
    n = len(v)
    nuevo_indice = 0

    if i >= n or i < 0:
        print("indice fuera de rango")
        return

    print("r1.1:", v[i].obtener_identificador_pago())

    if i % 2 == 0:
        nuevo_indice = i // 2

    elif i % 2 != 0:
        nuevo_indice = 3 * i + 1

    if nuevo_indice >= n:  # mostrar ultimo
        nuevo_indice = n - 1

    print("r1.2:", v[nuevo_indice].obtener_identificador_pago())


# -------------------------r2------------------------------
def comisiones(vector):
    matriz_comi = []

    for i in vector:
        monto_n = i.monto_nominal
        comision = 0

        if i.algoritmo_comision == 1:
            comision = 9 * monto_n / 100
            monto_base = monto_n - comision

        elif i.algoritmo_comision == 2:
            if monto_n < 50000:
                comision = 0
            elif monto_n < 80000:
                comision = 5 * monto_n / 100
            else:
                comision = 7.8 * monto_n / 100
            monto_base = monto_n - comision

        elif i.algoritmo_comision == 3:
            if monto_n > 25000:
                comision = 6 * monto_n / 100
            comision += 100
            monto_base = monto_n - comision

        elif i.algoritmo_comision == 4:
            if monto_n <= 100000:
                comision = 500
            else:
                comision = 1000
            monto_base = monto_n - comision

        elif i.algoritmo_comision == 5:
            if monto_n < 500000:
                comision = 0
            else:
                comision = 7 * monto_n / 100

                if comision > 50000:
                    comision = 50000
            monto_base = monto_n - comision

        else:
            monto_base = monto_n

        matriz_comi.append([comision, monto_base])

    return matriz_comi


def generar_nuevo_archivo(v, m_comisiones, arc):
    n = len(v)

    matriz_acumulador = []

    for i in range(n):
        objeto = v[i]
        comision = m_comisiones[i][0]  # columna de las comisiones
        moneda_origen = objeto.obtener_codigo_moneda_origen()

        pos = -1
        for fila in range(len(matriz_acumulador)):
            if matriz_acumulador[fila][0] == moneda_origen:
                pos = fila
                break

        if pos == -1:
            matriz_acumulador.append([moneda_origen, comision, 1])
        else:
            matriz_acumulador[pos][1] += comision
            matriz_acumulador[pos][2] += 1

    promedio = [0.0] * 6
    for k in range(len(matriz_acumulador)):
        moneda = matriz_acumulador[k][0]
        suma_comision = matriz_acumulador[k][1]
        cant_objetos = matriz_acumulador[k][2]

        if cant_objetos != 0:
            promedio[moneda] = suma_comision / cant_objetos

    m = open(arc, "wb")
    for i in range(n):
        comision = m_comisiones[i][0]
        moneda = v[i].obtener_codigo_moneda_origen()

        if comision > promedio[moneda]:
            pickle.dump(v[i], m)

    m.close()


# r21
def mostrar_archivo(arc):
    m = open(arc, 'rb')

    tam = os.path.getsize(arc)
    while m.tell() < tam:
        obj = pickle.load(m)
        print(obj)

    m.close()


# r22
def mostrar_envios_mayorcomision(arc):
    m = open(arc, 'rb')
    tam = os.path.getsize(arc)
    envios = []
    while m.tell() < tam:
        obj = pickle.load(m)
        envios.append(obj)
    m.close()

    matriz_comi = comisiones(envios)  # [comision, monto_base]

    if not envios:
        print("El archivo no contiene envíos.")
        return

    ordenar_por_comision_descendente(envios, matriz_comi)

    n = len(envios)
    if n < 3:
        for i in range(n):
            print(envios[i])
    else:
        for i in range(3):
            print(envios[i])


def ordenar_por_comision_descendente(envios, matriz_comi):
    # metodo de la burbuja
    n = len(envios)
    for i in range(n - 1):
        for j in range(n - i - 1):
            comision_actual = matriz_comi[j][0]
            comision_siguiente = matriz_comi[j + 1][0]

            if comision_actual < comision_siguiente:
                matriz_comi[j], matriz_comi[j + 1] = matriz_comi[j + 1], matriz_comi[j]

                envios[j], envios[j + 1] = envios[j + 1], envios[j]


# -------------------------r3-----------------------------
# r31
def redondear_centena(monto):
    return int(round(monto / 100.0)) * 100


# r32
def buscar_modificar_por_id(vector, id_dest):
    for envio in vector:
        if envio.identificacion_destinatario == id_dest:
            antes = envio.monto_nominal
            despues = redondear_centena(antes * 1.17)
            envio.monto_nominal = despues
            return antes, despues
    return 0, 0


# -----------------------------r4-------------------------------
def calculo_impositivo(v, matriz):
    impuesto = 0
    monto_final = 0
    m_2 = []

    for i in range(len(matriz)):
        mont_ba = matriz[i][1]

        i = v[i]
        if i.algoritmo_impositivo == 1:
            if mont_ba <= 300000:
                impuesto = 0
            else:
                excedente = mont_ba - 300000
                impuesto = excedente * 25 / 100

            monto_final = mont_ba - impuesto

        elif i.algoritmo_impositivo == 2:
            if mont_ba < 50000:
                impuesto = 50
            else:
                impuesto = 100
            monto_final = mont_ba - impuesto

        elif i.algoritmo_impositivo == 3:
            impuesto = mont_ba * 3 / 100
            monto_final = mont_ba - impuesto

        m_2.append([impuesto, monto_final])

    return m_2


def generar_matriz_maximos(v, m_montos_finales):
    n = len(v)
    filas = 6
    columnas = 6
    matriz_max = [[None] * columnas for i in range(filas)]

    matriz_montos = [[-1.0] * columnas for _ in range(filas)]

    for i in range(n):
        envio = v[i]

        mon_origen = envio.obtener_codigo_moneda_origen()
        mon_pago = envio.obtener_codigo_moneda_destino()

        monto_final = m_montos_finales[i][1]

        if monto_final > matriz_montos[mon_origen][mon_pago]:
            matriz_montos[mon_origen][mon_pago] = monto_final

            matriz_max[mon_origen][mon_pago] = envio

    return matriz_max


# r41
def mostrar_codigo_op4(matriz):
    for mo in range(1, 6):
        for mp in range(1, 6):
            envio_max = matriz[mo][mp]
            if envio_max is not None:
                print(f'{mo}|{mp}|{envio_max.obtener_identificador_pago()}')

