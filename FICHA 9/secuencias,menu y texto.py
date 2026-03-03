
def ingresar():
    cant = int(input("ingrese la cantidad de numeros: "))
    cant_cumplen = 0

    while cant == 0 or cant < 0:
        print("error,que sea mayor a 0")
        cant = int(input("ingrese la cantidad de numeros: "))


    for i in range(cant):
        numero = int(input("ingrese el numero: "))

        if (numero % 3 == 0) and (numero % 5 == 0):
            cant_cumplen +=1

    porcentaje = cant_cumplen * 100 / cant

    print("cantidad multiplos: ",cant_cumplen)
    print("porcentaje: ",porcentaje)


def caracteres():
    texto = input("ingrese el texto(que termine en punto): ")
    cant_letras = 0
    cant_mayores = 0

    for letra in texto:
        if letra != " ":
            cant_letras += 1
        if letra == ".":
            if cant_letras > 4:
                cant_mayores += 1
        else:
            if cant_letras > 4:
                cant_mayores += 1
            cant_letras = 0

    print("cantidad palabras: ",cant_mayores)

def alumnos():
    nombres = []
    notas = []

    for i in range(3):
        nombres.append(input("ingrese el nombre: "))
        notas.append(input("ingrese la nota: "))



def principal():
    op = 0
    while op != 4:
        print("op 1")
        print("op 2")
        print("op 3")
        print("op 4 salir")
        op = int(input("opcion: "))

        if op == 1:
            ingresar()

        if op == 2:
            caracteres()

        if op == 3:
            alumnos()

        if op == 4:
            print("adios")


if __name__ == "__main__":
    principal()