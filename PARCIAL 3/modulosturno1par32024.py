
def validar(tipo):
    while tipo < 1 or tipo > 30:
        tipo = int(input("error,cargue entre el rango correspondiente: "))
    return tipo

def acomodar_vector(v):
    n = len(v)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if v[i].calorias > v[j].calorias:
                v[i] , v[j] = v[j] , v[i]

def conteo(v):
    v_acu = [0] * 30

    for i in v:
        t = i.tipo
        if 0 < t <= 30:
            v_acu[t-1] += 1
    return v_acu


def busqueda(v):
    cod = input("ingrese el codigo del producto a buscar: ")
    n = len(v)
    for i in range(n):
        if v[i].codigo == cod:
            return i
    return -1



def generar_arreglo():
    cod_pro = input("ingrese el codigo del producto: ")
    desc = input("ingrese la descripcion del producto: ")
    cant = int(input("ingrese la cantidad de calorias: "))
    tipo = int(input("ingrese el tipo de producto que es: "))
    tipo = validar(tipo)
    precio = input("ingrese el precio: ")

    producto = Producto(cod_pro,desc,cant,tipo,precio)
    return producto


class Producto:
    def __init__(self,cod_pro,desc,cant,tipo,precio):
        self.codigo = cod_pro
        self.descripcion = desc
        self.calorias = cant
        self.tipo = tipo
        self.precio = precio

    def __str__(self):
        cadena = "codigo:"+ str(self.codigo) + "| descripcion:" + str(self.descripcion) + "| calorias:" + str(self.calorias) + "| tipo:" + str(self.tipo) + "| precio:" + str(self.precio)
        return cadena