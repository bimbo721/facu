import pickle
import random
import os

#1
def acomodar_arreglo(v,equipo):
    n = len(v)
    izq = 0
    der = n-1
    pos = 0

    while izq <= der:
        centro = (izq+der) // 2

        if v[centro].nombre == equipo.nombre:
            pos = centro
            break

        if v[centro].nombre < equipo.nombre:
            izq = centro + 1

        if v[centro].nombre > equipo.nombre:
            der = centro - 1

    if izq > der:
        pos = izq

    v[pos:pos] = [equipo]

#111
def generar_arreglo():
    n = int(input("ingrese la cantidad de equipos a competir: "))
    v = []
    nombres = ["pepe","julio","julian","a","miami","queso","etc"]

    for i in range(n):
        numero = random.randint(1,100)
        nom = random.choice(nombres)
        edad = random.randint(12,17)
        nivel = random.randint(0,2)
        monto = random.randint(1000,10000)

        equipo = Equipo(numero,nom,edad,nivel,monto)

        acomodar_arreglo(v,equipo)

    return v


#2222222
def agregar_a_la_copia(obj_orig):
    numero = obj_orig.numero
    nom = obj_orig.nombre
    edad = obj_orig.edad
    nivel = obj_orig.nivel
    monto = obj_orig.monto

    obj_copia = Equipo(numero,nom,edad,nivel,monto)

    return obj_copia


#2222
def mostrar_vector(vector_original):
    v = []

    for i in range(len(vector_original)):
        v.append(agregar_a_la_copia(vector_original[i]))


    for i in range(len(v)):
        if v[i].nivel == 0:
            v[i].nivel = "bajo"
            print("equipo--",v[i])

        elif v[i].nivel == 1:
            v[i].nivel = "intermedio"
            print("equipo--", v[i])

        elif v[i].nivel == 2:
            v[i].nivel = "avanzado"
            print("equipo--", v[i])


#3333333
def generar_matriz(v):
    e = int(input("ingrese la edad: "))
    n = 6
    m = 3
    monto_total = 0

    matriz = [0] * n
    for c in range(n):
        matriz[c] = [0] * m

    for i in range(len(v)):
        f = v[i].edad - 12
        c = v[i].nivel
        matriz[f][c] += v[i].monto

    e -= 12
    for f in range(n):
        if f == e:
            for c in range(len(matriz[f])):
                monto_total += matriz[f][c]

    for f in range(n):
        for c in range(len(matriz[f])):
            print("monto total para la edad",f+1," de nivel",c,":",matriz[f][c])


    print("monto total de la edad",e+12,":",monto_total)


#44444
def generar_archivo(v):
    m = open("archivoturno1.dat","wb")
    i1 = int(input("valor 1: "))
    i2 = int(input("valor 2: "))

    for i in range(len(v)):
        if i1 < v[i].numero < i2:
            pickle.dump(v[i],m)

    m.close()


#5555
def mostrar_archivo():
    m = open("archivoturno1.dat","rb")
    tamaño = os.path.getsize("archivoturno1.dat")
    suma = 0
    cant_vueltas = 0

    while m.tell() < tamaño:
        obj = pickle.load(m)
        print("equipo--",obj)
        suma += obj.edad
        cant_vueltas += 1

    promedio = suma // cant_vueltas
    print("suma",suma)
    print("promedio: ",promedio)
    m.close()


class Equipo:
    def __init__(self,numero,nom,edad,nivel,monto):
        self.numero = numero
        self.nombre = nom
        self.edad = edad
        self.nivel = nivel
        self.monto = monto

    def __str__(self):
        cadena = "numero:"+str(self.numero)+" |nombre:"+str(self.nombre)+" |edad:"+str(self.edad)+" |nivel:"+str(self.nivel)+" |monto:"+str(self.monto)
        return cadena