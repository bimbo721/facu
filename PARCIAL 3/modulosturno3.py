
def generar_vector2(v,n1,n2):
    vector_2 =[]
    for i in v:
        if n1 <= v[i].importe <= n2:
            vector_2.append(v[i])

    return vector_2

#apartado c
def conteo(v):
    v_acu = [0] * 10
    for i in v:
        t = v[i]
        if 1 <= v[i].tipo_servicio <= 10:
            v_acu[i - 1] += 1

    return v_acu

#apartado d
def buscar_servicio(v):
    nom = input("ingrese el nombre a buscar: ")

    for i in v:
        if v[i].nombre == nom:
            v[i].importe += 2000
            return i
    return -1


def acomodar_vector(v):
    n = len(v)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if v[i].cod_ident > v[j].cod_ident:
                v[i] , v[j] = v[j] , v[i]


def generar_arreglo():
    cod_ident = int(input("ingrese el codigo de identificatorio: "))
    nom = input("ingrese el nombre del cliente: ")
    tipo_serv = int(input("ingrese el tipo de servicio: "))
    importe = int(input("ingrese el importe a pagar: "))

    cliente = Servicio(cod_ident,nom,tipo_serv,importe)
    return cliente


class Servicio():
    def __init__(self,cod_ident,nom,tipo_serv,importe):
        self.cod_ident = cod_ident
        self.nombre = nom
        self.tipo_servicio = tipo_serv
        self.importe = importe

    def __str__(self):
        cadena = "codigo indentificatorio: " + str(self.cod_ident) + "| nombre: " + str(self.nombre) + "| tipo de servicio: " + str(self.tipo_servicio) + "| monto: " + str(self.importe)
        return cadena