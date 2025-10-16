import os.path
import pickle
import random
from pokemons import *


def acomodar_arreglo(v,pokemon):
    n = len(v)
    izq = 0
    der = n-1
    pos = 0

    while izq <= der:
        centro = (izq+der) // 2
        if v[centro].numero == pokemon.numero:
            pos = centro
            break

        if v[centro].numero > pokemon.numero:
            der = centro - 1

        if v[centro].numero < pokemon.numero:
            izq = centro + 1

    if izq > der:
        pos = izq

    v[pos:pos] = [pokemon]


def cargar_arreglo():
    n = int(input("ingrese la cantidad de pokemons a cargar: "))
    nombres = ["pika","pacu","leon","qdq","vorte","gummy","fansta"]
    v = []

    for i in range(n):
        nombre = random.choice(nombres)
        numero = random.randint(1,1025)
        tipo = random.randint(1,18)
        pc = random.randint(1,5000)
        nivel = random.randint(1,6)

        bicho = Pokemon(nombre,numero,tipo,pc,nivel)

        acomodar_arreglo(v,bicho)

    return v


def mostrar_vector(v):
    contador = [0]
    t1 = int(input("ingrese el tipo: "))
    t2 = int(input("ingrese el tipo: "))
    t3 = int(input("ingrese el tipo: "))

    for i in range(len(v)):
        print("pokemon= ",v[i])

        if v[i].tipo == t1 or v[i].tipo == t2 or v[i].tipo == t3:
            contador += 1

    print("Cantidad con tipo t1/t2/t3:", contador)


def generar_matriz(v):
    #fila: tipo
    #columna: nivel
    #casilla: cantidad de pokemons
    n = 18
    m = 6
    matriz = [0] * n
    for c in range(n):
        matriz[c] = [0] * m

    for i in range(len(v)):
        f = v[i].tipo
        c = v[i].nivel
        matriz[f][c] += 1

    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            if matriz[f][c] > 0:
                print("fila",f," columna:",c," cantidad:",matriz[f][c])

def generar_archivo(fd,v):
    m = open(fd,"wb")

    for i in range(len(v)):
        if v[i].pc < 1500:
            pickle.dump(v[i],m)

    m.close()

def mostrar_archivo(fd):
    m = open(fd,"rb")
    tamaño = os.path.getsize(fd)
    suma = 0
    t = int(input("ingrese el tipo: "))
    cant_objetos = 0

    while m.tell() < tamaño:
        obj = pickle.load(m)
        print("pokemon---",obj)
        if obj.tipo == t:
            suma += obj.pc
            cant_objetos += 1

    promedio = suma / cant_objetos
    print("promedio:",promedio)
    m.close()

class Pokemon:
    def __init__(self, nombre, numero, tipo, pc, nivel):
        self.nombre = nombre
        self.numero = numero
        self.tipo = tipo
        self.pc = pc
        self.nivel = nivel

    def __str__(self):
        return f"{self.nombre:<15} - N° {self.numero:>4} - Tipo {self.tipo:>2} - PC: {self.pc:>6} - Nivel Evolución: {self.nivel:>2}"
