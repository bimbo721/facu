def validar_pais(pais):
    while pais < 1 or pais > 20:
        pais = int(input("error,ingrese el valor correspondiente: "))
    return pais

def validar_codigo(codigo):
    while codigo != str:
        codigo = input("error,ingrese una cadena de string: ")
    return codigo


def acomodar_codigo_vuelo(v):
    n = len(v)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if v[i].codigo_vuelo > v[j].codigo_vuelo:
                v[i] , v[j] = v[j] , v[i]


def ticekts_mayores_num(v,x):
    v_mayores = []
    n = len(v)

    for i in range(n):
        if x > v[i].asiento:
            v_mayores.append(v[i].pasajero)
    return v_mayores

def nose(v):
    t = int(input("ingrese la t: "))
    n = len(v)
    v_acu = [0] * 20 #acumular los montos
    suma = 0

    for i in range(n):
        for j in range(i+1,n):
            if v[i+1].pais == j:
                v_acu[i] += v[j].monto

    for i in range(len(v_acu)):
        if t > v_acu[i]:
            suma += v_acu[i]
    return suma

def buscar_num_ident(v,id):
    n = len(v)
    for i in range(n):
        if id == v[i].numero_ident:
            return i
    return -1



def generar_arreglo():
    codigo_vuelo = input("ingrese codigo de vuelo: ")
    codigo_vuelo = validar_codigo(codigo_vuelo)

    codigo_ident = input("ingrese numero de identifacion: ")
    pais = int(input("ingrese pais destino: "))
    pais = validar_pais(pais)
    asiento = input("ingrese asiento designado: ")
    importe = float(input("ingrese el monto pagado: "))

    pasajero = Ticket(codigo_vuelo,codigo_ident,pais,asiento,importe)

    return pasajero

class Ticket():
    def __init__(self,codigo_vuelo,codigo_ident,pais,asiento,importe):
        self.codigo_vuelo = codigo_vuelo
        self.numero_ident = codigo_ident
        self.pais = pais
        self.asiento = asiento
        self.monto = importe

    def __str__(self):
        cadena = "codigo :" + str(self.codigo_vuelo) + "numero identifiacion : " + str(self.numero_ident) + "pais: " + str(self.pais) + "asiento: "+ str(self.asiento) + "importe: " + str(self.monto)
        return cadena