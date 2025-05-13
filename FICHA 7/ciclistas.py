competidores = int(input("ingrese la cantidad de ciclistas(0 para terminar): "))
tiempo_record = int(input("ingrese el tiempo record previsto: "))
print()
total_competidores = 0
tiempo_viejo = 0
ganador_nombre = ""
tiempo_total = 0


while total_competidores < competidores:
    nombre = input("ingrese el nombre del ciclista: ")
    tiempo_ciclista = int(input("ingrese el tiempo de carrera: "))
    tiempo_total = tiempo_ciclista + tiempo_total
    total_competidores += 1
    
    if tiempo_viejo > tiempo_ciclista:
        tiempo_viejo = tiempo_ciclista
        ganador_nombre = nombre

    print()


if tiempo_record > tiempo_viejo:
    print("el ganador ",nombre,"rompio el record")
else:
    print("el tiempo del ganador es menor al tiempo record")

tiempo_promedio = tiempo_total // competidores

print("El tiempo promedio fue:", tiempo_promedio)
print("termino")



