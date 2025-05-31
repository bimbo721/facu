palabra = input("ingrese la palabra: ")

cant_palabras_cuatro = 0

cant_palabras_con_x_y = 0

cant_de_palabras = 0

cant_silabas_mo = 0

cant_letras = 0

cant_letras_totales = 0


cant_silabas_mo_en_una_palabra = 0

letra_anterior = ""

"el mono momoxy toca el xilofon."
for letra in palabra:

    
    if letra == " " or letra == ".":
        cant_de_palabras += 1
        if bandera_x_y == True:
            cant_palabras_con_x_y += 1
            bandera_x_y = False
            
        if cant_letras > 4:
            cant_palabras_cuatro += 1
            cant_letras = 0
            
        if cant_silabas_mo_en_una_palabra == 1:
            cant_silabas_mo += 1
            cant_silabas_mo_en_una_palabra = 0
        else: cant_silabas_mo_en_una_palabra = 0

            
    else:
        cant_letras_totales += 1
        if letra == "x" or letra == "y":
            bandera_x_y = True
            
        if letra_anterior == "m" and letra == "o":
            cant_silabas_mo_en_una_palabra += 1
    
    letra_anterior = letra
    
    
        
promedio = round(cant_letras_totales / cant_de_palabras, 2)
        
print("cantidad de palabras: ",cant_de_palabras)
print("cantidad letras totales: ",cant_letras_totales)

print("...")
print("palabras con mas de 4 letras: ",cant_palabras_cuatro)
print("x e y: ",cant_palabras_con_x_y)
print("promedio: ",promedio)        
print("cantidad de silabas mo: ",cant_silabas_mo)        
        
        