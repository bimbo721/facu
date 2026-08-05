#from blablabla import *

def asignar_caracteristicas(i):
    print(f"los siguientes datos son para el libro {i+1}...")
    nombre = input("ingrese el nombre: ")
    #autor = input("ingrese el autor: ") # para hacer mas corto el procedimiento
    id = int(input("ingrese el ID: "))
    
    objeto = Libro(nombre,id)
    
    return objeto


def modificar_datos(libro):
    #aca habria que hacer un menu para que elija que cosa modificar
    libro.nombre = input("ingrese el nuevo nombre: ")
    return f"--> modificado con exito!\n"
    


def principal():
    opc = 0
    vector = [] #seria la base de datos(por asi decirlo) de todos los libros registrados
    while opc != 4:
        print("opcion 1) registrar nuevos libros")
        print("opcion 2) mostrar informacion de un libro")
        print("opcion 3) modificar datos de un libro")
        print("opcion 4) salir")

        
        opc = int(input("elija la opcion: "))
        
        if opc == 1:
            n = int(input("ingrese la cantidad de libros a registrar: "))
            for i in range(n):
                libro = asignar_caracteristicas(i)
                vector.append(libro)
                
            
        if opc == 2:
            if not vector:
                print("esta vacio")
            else:
                print("--informacion--")
                for i in vector:
                    print(f"{i}\n------------------")
        
        if opc == 3:
            id_mod = int(input("ingrese el ID del libro a modificar: "))
            flag = False
            for libro in vector:
                if libro.id == id_mod:
                    modificar_datos(libro)
                    flag = True
                    
            if flag == False:
                print("no se encontró")
                    
                    
        if opc == 4:
            print("adios")
            break
    

class Libro():
    def __init__(self,nombre,id):
        self.nombre = nombre
        self.id = id

    #print(f"lo que quiera y para llamar variables es con {} bla bla")
    def __str__(self):
        return f"El nombre del libro es:{self.nombre}\nEl ID es:{self.id}" 

# El autor es:{self.autor}\nEsta en la estanteria:{self.estanteria}
principal()