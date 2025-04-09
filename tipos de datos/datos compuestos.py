#lista(se puede modificar)
lista = ["bimbo","1,73","19 años"]

lista [1] = "bimbazo"

print(lista)

#tupla(no se puede modificar)
tupla = ("joaco","pan")

print(tupla)


#conjuntos(no se accede a elementos por indice, no almacena datos duplicados)
conjunto = {"bimbo","1,73","19 años"}

#print(conjunto[3]) -> no puede acceder al elemento


#diccionario, va con comas y :
diccionario = {
    'nombre' : 'lucas dalto',
    'apodo' : 'soy dalto',
    'altura' : 1.84
    
}

print(diccionario["apodo"] + " 2")