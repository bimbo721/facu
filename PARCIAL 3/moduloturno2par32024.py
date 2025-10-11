def validar_tipo(tipo):
    while tipo < 1 or tipo > 20:
        tipo = int(input("error,ingrese un valor entre el 1 y el 20: "))
    return tipo

def cant_gramos(v):
    n = len(v)
    suma = 0

    for i in v:
        suma += i.cantidad

    return suma / n

def conteo(v):
    v_acu = [0] * 20

    for i in v:
        t = i.tipo
        v_acu[t-1] += 1
    return v_acu


def acomodar_arreglo(v):
    v_ig = []
    
    for i in range(len(v)):
        if v[i].ignifugo == 1:
            v_ig.append(v[i])

    n = len(v_ig)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if v_ig[i].diametro < v_ig[j].diametro:
                v_ig[i] , v_ig[j] = v_ig[j] , v_ig[i]

    return v_ig

def busqueda(v):
    prod = int(input("ingrese el codigo a buscar: "))

    for i in range(len(v)):
        if v[i].codigo == prod:
            return i
    return -1


def generar_arreglo():
    cod_producto = int(input("ingrese el codigo: "))
    diametro = float(input("ingrese las pulgadas: "))
    tipo = int(input("ingrese el tipo delo 1 al 20: "))
    tipo = validar_tipo(tipo)
    cantidad = float(input("ingrese la cantidad de pv_igc: "))
    ignifugo = int(input("es ignifugo? 1:si , 2:no: "))


    tubo = Tubo(cod_producto,diametro,tipo,cantidad,ignifugo)
    return tubo

class Tubo:
    def __init__(self,cod_producto,diametro,tipo,cantidad,ignifugo):
        self.codigo = cod_producto
        self.diametro = diametro
        self.tipo = tipo
        self.cantidad_pv_igc = cantidad
        self.ignifugo = ignifugo

    def __str__(self):
        cadena = "codigo: " + str(self.codigo) + "| diametro: " + str(self.diametro) + "| tipo: " + str(self.tipo) + "| cantidad pv_igc: " + str(self.cantidad_pv_igc) + "| ingifugo: " + str(self.ignifugo)
        return cadena