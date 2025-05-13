espectadores = int(input("ingrese la cantidad de participantes: "))


con_descuento = 50
sin_descuento = 75
entrada = 0
funciones_con_descuentos = 0

while espectadores != 0:
    cantidad = int(input("cantidad de espectadores: "))
    descuento = str(input("ingrese si tiene descuento o no(SI/NO): "))
    if descuento == "SI":
        entrada += 50
        funciones_con_descuentos += 1
    if descuento == "NO":
        entrada += 75


total_ventas = entrada
procentaje = total_ventas 

print("se vendieron ",funciones_con_descuentos,"funciones con descuento")
print("un", ,"porciento")


