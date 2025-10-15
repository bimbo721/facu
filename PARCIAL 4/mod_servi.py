import random
import os.path
import pickle

def generar_archivo(v):
    n = len(v)
    x = int(input("ingrese el valor mayor a calificacion: "))
    tipos_prohibidos = [4,8,12]
    m = open("archivoespecial.dat", "wb")
    for i in range(n):
        if v[i].tipo not in tipos_prohibidos and v[i].calificacion > x:
            pickle.dump(v[i],m)

    m.close()

    return True

def mostrar_archivo():
    m = open("archivoespecial.dat","rb")
    n = os.path.getsize("archivoespecial.dat")
    total_cant = 0
    if n == 0:
        print("archivo vacio")
        return

    while m.tell() < n:
        obj = pickle.load(m)
        print("rta 5:"+" codigo:"+str(obj.codigo)+"- nombre:"+str(obj.nombre)+" ...etc")
        total_cant += obj.cantidad

    print("cant:",total_cant)
    print("")
    m.close()


def generar_matriz(v):
    #filas: tipo
    #columnas:calificacion
    #subindice/celda: reproducciones
    n = 15
    m = 13
    matriz = [0] * n
    for c in range(n):
        matriz[c] = [0] * m

    for i in range(len(v)):
        f = v[i].tipo -1
        c = v[i].calificacion
        matriz[f][c] += v[i].cantidad

    return matriz

def mostrar_matriz(matriz):
    n = len(matriz)

    for f in range(n):
        for c in range(len(matriz[f])):
            if matriz[f][c] > 0:
                print("fila",f," columa",c," valor:",matriz[f][c])


def cargar_arreglo():
    v = []
    n = int(input("ingrese la cantidad de contenidos a agregar:"))
    nombres = ["Alpha", "Beta", "Gamma", "Delta", "Omega", "Nova", "Pixel", "Astra", "Orion", "Echo"]

    for i in range(n):
        cod = random.randint(1, 100000)
        nom = random.choice(nombres)
        tipo = random.randint(1, 15)
        cali = random.randint(0, 12)
        cant = random.randint(0, 1000000)

        pelicula = Contenido(cod,nom,tipo,cali,cant)

        acomodar_arreglo(v,pelicula)

    return v


def acomodar_arreglo(v,pelicula):
    n = len(v)
    izq = 0
    der = n-1
    pos = 0
    #pelicula.nombre es el objeto que se esta metiendo al vector
    while izq <= der:
        centro = (izq + der) // 2

        if v[centro].nombre == pelicula.nombre:
            pos = centro
            break

        if v[centro].nombre < pelicula.nombre:
            izq = centro + 1

        elif v[centro].nombre > pelicula.nombre:
            der = centro - 1

    if izq > der:
        pos = izq

    v[pos:pos] = [pelicula]


class Contenido:
    def __init__(self,cod,nom,tipo,cali,cant):
        self.codigo = cod
        self.nombre = nom
        self.tipo = tipo
        self.calificacion = cali
        self.cantidad = cant


    def __str__(self):
        cadena = "|codigo:"+str(self.codigo) + " |nombre:"+str(self.nombre)+" |tipo:"+str(self.tipo)+ " |calificacion:"+str(self.calificacion)+ " |cantidad:" +str(self.cantidad)
        return cadena