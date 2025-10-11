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
    distintos = 0

    m = open("envios.csv", "rt")
    for linea in m:
        obj = cargar_envio(linea)

        if obj is not None:
            v.append(obj)
            if obj.cod_mon_origen != obj.cod_mon_pago:
                distintos = distintos + 1
    m.close()

    return distintos

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

class Envio():
    def __init__(self, cod_mon_origen, cod_mon_pago, id_pago, id_dest, nom_dest, tasa_conv, monto_nominal, alg_com, alg_imp):

        self.cod_mon_origen = int(cod_mon_origen)
        self.cod_mon_pago = int(cod_mon_pago)
        self.id_pago = id_pago
        self.id_dest = id_dest
        self.nom_dest = nom_dest
        self.tasa_conv = float(tasa_conv)
        self.monto_nominal = float(monto_nominal)
        self.alg_com = int(alg_com)
        self.alg_imp = int(alg_imp)

    def __str__(self):
        cadena = "Envio("
        cadena += "mon_origen=" + str(self.cod_mon_origen)
        cadena += ", mon_pago=" + str(self.cod_mon_pago)
        cadena += ", id_pago=" + self.id_pago
        cadena += ", id_dest=" + self.id_dest
        cadena += ", nom_dest=" + self.nom_dest
        cadena += ", tasa_conv=" + str(self.tasa_conv)
        cadena += ", monto_nominal=" + str(self.monto_nominal)
        cadena += ", alg_com=" + str(self.alg_com)
        cadena += ", alg_imp=" + str(self.alg_imp)
        cadena += ")"
        return cadena