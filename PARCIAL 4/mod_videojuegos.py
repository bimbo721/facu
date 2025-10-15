import pickle
import random
import os

def crear_archivo(v):
    m = open("archivojuegos.dat","wb")

    for i in range(len(v)):
        if v[i].stock != 0 and (v[i].pais != 1 and v[i].pais != 0):
            pickle.dump(v[i],m)

    m.close()


def mostrar_archivo():
    m = open("archivojuegos.dat","rb")
    tamaño = os.path.getsize("archivojuegos.dat")
    suma = 0
    cant_registros = 0

    if tamaño == 0:
        print("archivo vacio")
        m.close()
        return

    while m.tell() < tamaño:
        obj = pickle.load(m)
        print("juego---",obj)
        suma += obj.precio
        cant_registros += 1


    promedio = suma // cant_registros
    print("precio promedio:",promedio)

    m.close()


def generar_matriz(v):
    #filas: pais
    #columa: tipo
    #casilla: cantidad de juegos
    n = 30
    m = 15
    matriz = [0] * n
    for f in range(n):
        matriz[f] = [0] * m

    for i in range(len(v)):
        f = v[i].pais
        c = v[i].tipo
        matriz[f][c] += 1

    x = int(input("ingrese el valor maximo para mostrar los contadores: "))

    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            if 0 < matriz[f][c] < x:
                print("cantidad de juegos del pais",f," del tipo",c,":",matriz[f][c])


def cargar_arreglo():
    n = int(input("ingrese la cantidad de juegos a cargar: "))
    nombres = ["creep","bld","cas","r6","cs","cod","moh","lol"]
    v = []

    for i in range(n):
        ident = random.randint(1,10000)
        nomb = random.choice(nombres)
        stock = random.randint(0,10)
        precio = random.randint(1,100)
        pais = random.randint(0,29)
        tipo = random.randint(0,14)

        juego = Juego(ident,nomb,stock,precio,pais,tipo)

        acomodar_arreglo(v,juego)

    return v


def acomodar_arreglo(v,juego):
    n = len(v)
    izq = 0
    der = n-1
    pos = 0

    while izq <= der:
        centro = (izq + der) //2

        if v[centro].nombre == juego.nombre:
            pos = centro
            break

        if v[centro].nombre > juego.nombre:
            der = centro - 1

        elif v[centro].nombre < juego.nombre:
            izq = centro + 1

    if izq > der:
        pos = izq

    v[pos:pos] = [juego]


class Juego:
    def __init__(self,ident,nomb,stock,precio,pais,tipo):
        self.identificacion = ident
        self.nombre = nomb
        self.stock = stock
        self.precio = precio
        self.pais = pais
        self.tipo = tipo

    def __str__(self):
        cadena = "identificacion:"+str(self.identificacion)+" |nombre:"+str(self.nombre)+" |stock:"+str(self.stock)+" |precio:"+str(self.precio)+" |pais:"+str(self.pais)+" |tipo:"+str(self.tipo)
        return cadena