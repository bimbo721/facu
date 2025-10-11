import pickle

def validar_tipo(tipo):
    if tipo > 9 or tipo < 0:
        return False
    else:
        return True



def arreglo_alquileres(lista):
    dni = str(lista[0].replace("-",""))
    monto = float(lista[1])
    tipo = int(lista[2])
    tipo = validar_tipo(tipo)

    if tipo:
        inquilino = Alquiler(dni,monto,tipo)
        return inquilino
    else:
        return None


class Alquiler():
    def __init__(self,dni,monto,tipo):
        self.dni = dni
        self.monto = monto
        self.tipo = tipo

    def __str__(self):
        cadena = "dni: " + str(self.dni) + " |monto:" +str(self.monto) + " |tipo:" +str(self.tipo)
        return cadena


def principal():
    v = []
    op = 0
    while op != 4:
        print("opcion 1)...")
        print("opcion 2)...")
        print("opcion 3)...")
        op = int(input("elija la opcion: "))

        if op == 1:
            m = open("alquileres.csv", "rt")

            primer_linea = False
            for linea in m:
                if not primer_linea:
                    primer_linea = True
                    continue

                linea = linea.rstrip("\n")
                lista = linea.split(",")

                inquilino = arreglo_alquileres(lista)
                if inquilino is None:
                    continue
                else:
                    v.append(inquilino)
            m.close()

        if op == 2:
            n = len(v)
            x = int(input("ingrese un monto a definir: "))
            p = open("nuevos_alquileres", "wb")

            for i in range(n):
                if v[i].monto > x:
                    pickle.dump(v[i], p)
            p.close()

            p = open("nuevos_alquileres", "rb")

            for i in range(n):
                obj = pickle.load(p)
                print(obj)
            p.close()

        if op == 3:
            m = open("nuevos_alquileres", "rt")
            v_monto = [0] * 10

            primer_linea = False
            for linea in m:
                if not primer_linea:
                    primer_linea = True
                    continue

                linea = linea.rstrip("\n")
                lista = linea.split(",")

                for i in range(10):
                    if int(lista[2]) == i:
                        v_monto[i] += float(lista[1])

            for i in range(10):
                print("en el tipo de cabañas", i, ",se reacaudo:", v_monto[i])

            m.close()

        if op == 4:
            print("chau")

principal()