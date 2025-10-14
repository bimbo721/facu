import random
import os
import pickle


def generar_matriz(v):
    #filas: tipo
    #columnas:calificacion
    #subindice/celda: reporducciones
    n = 15
    m = 13
    matriz = [0] * n
    for c in range(n):
        matriz[c] = [0] * m


    for i in range(len(v)):
        f = v[i].tipo -1
        c = v[i].calificacion
        matriz[f][c] += v[i].cantidad



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