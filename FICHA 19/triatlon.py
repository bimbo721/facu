def mostrar(vector):
    for i in range(len(vector)):
        print(vector[i])


def principal():
    vector = [0] * 3

    for i in range(3):
        nom = input("ingrese el nombre: ")
        t_natacion = input("ingrese el tiempo en natacion: ")
        t_ciclismo = input("ingrese el tiempo en ciclismo: ")
        t_corrido = input("ingrese el tiempo corrido: ")
        vector[i] = atletas(nom,t_natacion,t_ciclismo,t_corrido)

    mostrar(vector)


class atletas:
    def __init__(self ,nom ,tiempo_natacion ,tiempo_ciclismo ,tiempo_corrido):
        self.nombre = nom
        self.natacion = tiempo_natacion
        self.ciclismo = tiempo_ciclismo
        self.corrido = tiempo_corrido

    def __str__(self):
        cadena = "nombre: "+ self.nombre + "-tiempo natacion: " + str(self.natacion) + "-tiempo ciclismo: " + str(self.ciclismo) + "-tiempo corrido: " + str(self.corrido)
        return cadena


principal()