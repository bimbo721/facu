v = []
import bisect

#ordenamiento sort (metodo profesional) Por defecto ordena ascendente sino usar (v.sort(key=lambda x: x.atributo)
v.sort(key=lambda x: x.atributo)

#añadir ordenadamente(usa busqueda binaria,hay que acomodarlo antes o usar __lt__ en la clase)

def añadir_al_vector(vector,obj):
    bisect.insort(vector,obj)


    def __lt__(self, other):
        return self.loquequiera < other.loquequiera #ascendente


################################# ordenar matrices
def insercion_directa(v):
    n = len(v)

    for j in range(1,n):
        y = v[j]
        k = j-1
        while k >= 0 and y < v[k]:
            v[k+1] = v[k]
            k -= 1
        v[k+1] = y


def shell_sort(v):
    n = len(v)
    h = 1
    while h <= n // 9:
        h = 3 * h + 1
    while h > 0:
        for j in range(h, n):
            y = v[j]
            k = j - h
            while k >= 0 and y < v[k]:
                v[k+h] = v[k]
                k -= h
            v[k+h] = y
        h //= 3