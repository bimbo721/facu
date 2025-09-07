def validacion(tipo):
    while tipo < 0 or tipo > 39:
        tipo = int(input("error,ingrese el tipo de empleo correctamente: "))
    return tipo


def cargar_arreglo(n):
    numero = input("ingrese el numero de identificacion: ")
    desc = input("descripcion: ")
    tipo = int(input("tipo de empleo: "))
    tipo = validacion(tipo)
    monto = float(input("ingrese el monto:"))

    empl = Empleo(numero,desc,tipo,monto)
    return empl

def acomodar_vector(v):
    n = len(v)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if v[i].desc > v[j].desc:
                v[i] , v[j] = v[j] , v[i]



def conteo(v):
    v_conteo = [0] * 40
    n = len(v)
    for i in range(n):
        if 0 < v[i].tipo <= 39:
            v_conteo[i] += 1
    return v_conteo

def buscar_empleado(v,x):
    n = len(v)
    for i in range(n):
        if x == int(v[i].num_ident):
            return i
    return -1


class Empleo():
    def __init__(self,num_ident,desc,tipo,monto):
        self.num_ident = num_ident
        self.desc = desc
        self.tipo = tipo
        self.monto = monto

    def __str__(self):
        cadena = "numero de identificacion: " + str(self.num_ident) + "descripcion: " + str(self.desc) + "tipo de empleo: " + str(self.tipo) + "monto: " + str(self.monto)

        #cadena = "numero de identificacion: " + str(self.num_ident) + "\n"
        #cadena += "descripcion: " + str(self.desc) + "\n"
        #cadena += "tipo de empleo: " + str(self.tipo) + "\n"
        #cadena += "monto: " + str(self.monto) + "\n"

        return cadena