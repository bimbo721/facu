import pickle


def validar(op):
    permitidos = ['0', '1', '2']
    while True:
        op = op.strip()
        if len(op) == 1 and op in permitidos:
            return op
        op = input('Error: se pidio que cargue un numero entre 0 y 2: ')


def cargar_envio(linea):
    linea = linea.strip()
    if linea == "":
        return None

    indice = linea.split(',')

    if len(indice) < 7:
        indice = linea.split(';')
        if len(indice) < 7:
            return None


    codigo = indice[0].strip()


    cod_ord_pago = codigo.split('|')
    if len(cod_ord_pago) != 3:
        return None

    cod_mon_origen = int(cod_ord_pago[0])
    cod_mon_pago = int(cod_ord_pago[1])
    id_pago = cod_ord_pago[2].strip()

    id_dest = indice[1].strip()
    nom_dest = indice[2].strip()
    tasa_conv = float(indice[3])
    monto_nominal = float(indice[4])
    alg_com = int(indice[5])
    alg_imp = int(indice[6])

    objeto = Envio(cod_mon_origen, cod_mon_pago, id_pago, id_dest, nom_dest, tasa_conv, monto_nominal, alg_com, alg_imp)

    return objeto


def procesar_archivo_csv(v):
    m = open("envios.csv", "rt")
    distintos = 0

    for linea in m:
        obj = cargar_envio(linea)

        if obj is not None:
            acomodar_vector(v,obj)
            if obj.cod_mon_origen != obj.cod_mon_pago:
                distintos = distintos + 1

    m.close()
    return distintos

##################
def acomodar_vector(v,obj):
    izq = 0
    der = len(v)

    while izq < der:
        centro = (izq + der) // 2
        if v[centro].id_dest >= obj.id_dest:
            izq = centro + 1
        else:
            der = centro

    pos = izq
    v[pos:pos] = [obj]

##################
def buscar_valor(v,i):
    n = len(v)
    nuevo_indice = 0

    if i >= n or i < 0:
        print("indice fuera de rango")
        return


    for f in range(n):
        if i == f:
            print("r1.1: ",v[f].id_pago)

            if i % 2 == 0:
                nuevo_indice = i // 2

            elif i % 2 != 0:
                nuevo_indice = 3 * i + 1

            if nuevo_indice >= n: #mostrar ultimo
                nuevo_indice = n - 1

            print("r1.2: ",v[nuevo_indice].id_pago)
            break


def generar_nuevo_archivo(v,m_comisiones):
    n = len(v)

    matriz_acumulador = []
    #filas son las 5 monedas
    #columna 0 indica de que moneda es de origen
    #columa 1 suma_comisiones
    #columa 2 cantidad_objetos


    for i in range(n):
        objeto = v[i]
        comision = m_comisiones[i][0] #columna de las comisiones
        moneda_origen = objeto.obtener_codigo_moneda_origen()


        #esto verifica que existe la moneda en la matriz acu,si no,la agrega
        pos = -1
        for fila in range(len(matriz_acumulador)):
            if matriz_acumulador[fila][0] == moneda_origen:
                pos = fila
                break

        if pos == -1:
            matriz_acumulador.append([moneda_origen,comision,1])
        else:
            matriz_acumulador[pos][1] += comision
            matriz_acumulador[pos][2] += 1


    promedio = [0.0] * 6
    for k in range(len(matriz_acumulador)):
        moneda = matriz_acumulador[k][0]
        suma_comision = matriz_acumulador[k][1]
        cant_objetos = matriz_acumulador[k][2]

        if cant_objetos != 0: #poner promedio[moneda] hace que nunca entre al casillero
            #0 del promedio ya que "moneda = matriz_acumulador[k][0]" se guardo la moneda
            # en la matriz como (1,2,3,4 o 5)
            promedio[moneda] = suma_comision / cant_objetos


    #en la m_comisiones es asi:
    # las filas es un envio,o sea un objeto del vector
    # las columa 0 es comision
    # las columna 1 es el monto base


    #dato importante para entender,nunca se usan las filas de la matriz_acumulador,ya que
    #el valor/tipo de las monedas estan en la columna 0
    m = open("archivocomision", "wb")
    for i in range(n):
        comision = m_comisiones[i][0]
        moneda = v[i].obtener_codigo_moneda_origen()

        if comision > promedio[moneda]:
            pickle.dump(v[i],m)

    m.close()



#r22
def identificador(m_2,v,matriz):
    v_acu = []
    for fila in range(len(matriz)):
        comision = matriz[fila][0]
        monto_base = matriz[fila][1]
        impuesto = m_2[fila][0]

        nominal = comision + monto_base
        if nominal != 0:
            porc_desc = (impuesto + comision) * 100 / nominal
        else:
            porc_desc = 0
        v_acu.append(porc_desc)

    n = len(v_acu)
    for i in range(n-1):
        for j in range(i+1,n):
            if v_acu[i] < v_acu[j]:
                v[i] , v[j] = v[j] , v[i]
                v_acu[i], v_acu[j] = v_acu[j], v_acu[i]
                m_2[i] , m_2[j] = m_2[j], m_2[i]
                matriz[i] , matriz[j] = matriz[j] , matriz[i]


    iden_mayor_porc_desc = v[0].id_pago

    return iden_mayor_porc_desc


#r22
def calculo_impositivo(v,matriz):
    impuesto = 0
    monto_final = 0
    m_2 = []

    for i in range(len(matriz)):
        mont_ba = matriz[i][1]

        i = v[i]
        if i.alg_imp == 1:
            if mont_ba <= 300000:
                impuesto = 0
            else:
                excedente = mont_ba - 300000
                impuesto = excedente * 25 / 100

            monto_final = mont_ba - impuesto

        elif i.alg_imp == 2:
            if mont_ba < 50000:
                impuesto = 50
            else:
                impuesto = 100
            monto_final = mont_ba - impuesto

        elif i.alg_imp == 3:
            impuesto = mont_ba * 3 / 100
            monto_final = mont_ba - impuesto

        m_2.append([impuesto,monto_final])

    return m_2

#r21
def comisiones(vector):
    matriz_comi = []

    #las filas es un envio,o sea un objeto del vector
    #las columa 0 es comision
    #las columna 1 es el monto base


    for i in vector:
        monto_n = i.monto_nominal
        comision = 0

        if i.alg_com == 1:
            comision = 9 * monto_n / 100
            monto_base = monto_n - comision

        elif i.alg_com == 2:
            if monto_n < 50000:
                comision = 0
            elif monto_n < 80000:
                comision = 5 * monto_n / 100
            else:
                comision = 7.8 * monto_n / 100
            monto_base = monto_n - comision

        elif i.alg_com == 3:
            if monto_n > 25000:
                comision = 6 * monto_n / 100
            comision += 100
            monto_base = monto_n - comision

        elif i.alg_com == 4:
            if monto_n <= 100000:
                comision = 500
            else:
                comision = 1000
            monto_base = monto_n - comision

        elif i.alg_com == 5:
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

#r21
def porcentaje_comision(matriz):
    suma_nominal = 0
    suma_comisiones = 0

    for fila in matriz:
        comi = fila[0]
        base = fila[1]

        nominal = comi + base

        suma_nominal += nominal
        suma_comisiones += comi

    if suma_nominal != 0:
        porc_comi = suma_comisiones * 100 / suma_nominal
    else:
        return 0

    return porc_comi

def sumatoria_impuestos_por_par_monedas(v, m_2):
    resultado = []

    i = 0
    while i < len(v):
        envio = v[i]
        impuesto = m_2[i][0]
        mo = envio.cod_mon_origen
        mp = envio.cod_mon_pago

        pos = -1
        j = 0
        while j < len(resultado):
            if resultado[j][0] == mo and resultado[j][1] == mp:
                pos = j
                break
            j = j + 1

        if pos == -1:
            resultado.append([mo, mp, float(impuesto)])
        else:
            resultado[pos][2] = resultado[pos][2] + float(impuesto)

        i = i + 1

    return resultado


class Envio:
    def __init__(self, codigo, identificacion_destinatario,
                 nombre_destinatario, tasa, monto_nominal,
                 algoritmo_comision, algoritmo_impositivo):
        self.codigo = codigo
        self.identificacion_destinatario = identificacion_destinatario
        self.nombre_destinatario = nombre_destinatario
        self.tasa = tasa
        self.monto_nominal = monto_nominal
        self.algoritmo_comision = algoritmo_comision
        self.algoritmo_impositivo = algoritmo_impositivo

    def obtener_identificador_pago(self):
        identificador_pago = self.codigo.split("|")
        return identificador_pago[2]

    def obtener_codigo_moneda_origen(self):
        moneda_origen = self.codigo.split("|")
        return int(moneda_origen[0])

    def obtener_codigo_moneda_destino(self):
        moneda_destino = self.codigo.split("|")
        return int(moneda_destino[1])

    def __str__(self):
        return (
            f"Identificador de pago: {self.obtener_identificador_pago()} - Identificación: {self.identificacion_destinatario} -"
            f" Nombre: {self.nombre_destinatario} - Tasa: {self.tasa} - Monto nominal: {self.monto_nominal}")


def generar_envio(token):
    datos_base = token[:-1]
    datos_base = datos_base.split(",")
    codigo = datos_base[0]
    identificacion_destinatario = datos_base[1]
    nombre_destinatario = datos_base[2]
    tasa = float(datos_base[3])
    monto_nominal = int(datos_base[4])
    algoritmo_comision = int(datos_base[5])
    algoritmo_impositivo = int(datos_base[6])
    return Envio(codigo, identificacion_destinatario, nombre_destinatario, tasa, monto_nominal, algoritmo_comision,
                 algoritmo_impositivo)


if __name__ == "__main__":
    envio_base = "05|04|4616A0743D75FC8C,AF188371E36A,Shansa B. Alexis,1,11374056,4,2\n"
    envio = generar_envio(envio_base)
    print(envio)
    print(envio.obtener_identificador_pago())
    print(envio.obtener_codigo_moneda_origen())
    print(envio.obtener_codigo_moneda_destino())
