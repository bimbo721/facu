def validar_marca(marca):
    while marca < 1 or marca > 20:
        marca = int(input("error,ingrese un valor entre el 1 y 20"))
    return marca


def ordenar_arreglo(v):
    n1 = int(input("ingrese el valor 1: "))
    n2 = int(input("ingrese el valor 2: "))
    v_km = []

    for i in range(len(v)):
        if n1 <= v[i].tarifa <= n2:
            v_km.append(v[i])

    m = len(v_km)
    for i in range(0,m-1):
        for j in range(i+1,m):
            if v_km[i].codigo > v_km[j].codigo:
                v_km[i] , v_km[j] = v_km[j] , v_km[i]

    return v_km

def conteo(v):
    v_acu = [0] * 21 #ya que no admite el cero
    n = len(v_acu)

    for i in range(len(v)):
        t = v[i].marca
        for j in range(len(v_acu)):
            if t == j:
                v_acu[i+1] += 1
    del v_acu[0]
    return v_acu


def buscar_dni(v):
    d = int(input("ingrese el dni a buscar: "))

    for i in range(len(v)):
        if v[i].dni == d:
            return i
    return -1


def generar_arreglo():
    cod_ident = int(input("ingrese el numero que lo identifica: "))
    dni = int(input("ingrese el dni: "))
    marca = int(input("ingrese la marca del 1 al 20: "))
    marca = validar_marca(marca)
    tarifa = int(input("ingrese la tarifa por km: "))

    taxi = Taxi(cod_ident,dni,marca,tarifa)
    return taxi


class Taxi():
    def __init__(self,cod_ident,dni,marca,tarifa):
        self.codigo = cod_ident
        self.dni = dni
        self.marca = marca
        self.tarifa = tarifa


    def __str__(self):
        cadena = "|codigo:" + str(self.codigo) + "| dni:" + str(self.dni) + "| marca:" + str(self.marca) + "| tarifa:" + str(self.tarifa)
        return cadena


