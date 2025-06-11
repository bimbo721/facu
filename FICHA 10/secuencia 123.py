primer_valor = int(input("ingrese los numeros: "))

cant_numeros_div_4 = 0

mayor_impares = 0

cant_ingreso_primer = 0

cant_secuencias = 0

ultimo_fue_1 = False
ultimo_fue_1_y_2 = False

while primer_valor > 0:
    numero = int(input("ingrese los numeros: "))
        
    if numero % 4 == 0:
        cant_numeros_div_4 += 1

    if numero % 3 == 0:
        if numero > mayor_impares:
            mayor_impares = numero
    
    if numero == primer_valor:
        cant_ingreso_primer += 1
######

    if numero == 1:
        ultimo_fue_1 = True
        bandera_1_y_2 = False
    else:
        if numero == 2 and ultimo_fue_1 == True:
            bandera_1_y_2 = True
            ultimo_fue_1 = False
        else:
            if numero == 3 and bandera_1_y_2 == True:
                cant_secuencias += 1
                bandera_1_y_2 = False
            

    numero_anterior = numero    
    if numero == 0:
        break

print("primer valor:", primer_valor)
print("mayor: ", mayor_impares)
print("cantidad de veces de primero: ",cant_ingreso_primer)
print("cantidad de secuencias: ",cant_secuencias)

