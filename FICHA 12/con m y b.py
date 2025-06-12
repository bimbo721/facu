def es_vocal(letra):
    return letra in "aeiouAEIOU"



# Mi amiga Ambar siempre piensa y cambia pronto.
def principal():
    #m = open("entrada.txt")
    #texto = m.read()
    #m.close()
    texto = input("ingrese el texto: ")
    
    cant_palabras = 0
    cant_apartado_1 = 0
    cant_letras_palabra = 0
    bandera_empieza_p = False
    bandera_hay_m = False
    bandera_hay_b = False
    cant_apartado_2 = 0
    bandera_sigue_vocal = False
    cant_apartado_3 = 0
    letra_final = ""
    letra_principio = ""


    for letra in texto:
        if letra == " " or letra == ".":
            cant_palabras += 1
            
            if bandera_hay_m and bandera_hay_b:
                cant_apartado_1 += 1
            
            if bandera_empieza_p and bandera_sigue_vocal:
                cant_apartado_2 += 1
            
            if letra_final == letra_principio:
                cant_apartado_3 += 1
            
            cant_letras_palabra = 0
            bandera_hay_b = False
            bandera_hay_m = False
            bandera_empieza_p = False
            bandera_sigue_vocal = False
        
        else:
            cant_letras_palabra += 1

            if letra == "m":
                bandera_hay_m = True
                      
            if cant_letras_palabra > 3:
                if letra == "m":
                    bandera_hay_m = True
                elif letra == "b":
                    bandera_hay_b = True
                    
            if letra == "p" and cant_letras_palabra == 1:
                bandera_empieza_p = True
                
            if (es_vocal(letra) and bandera_empieza_p and cant_letras_palabra == 2):
                bandera_sigue_vocal = True
                
            if cant_letras_palabra == 1:
                letra_principio = letra
                print("letra principio: ",letra_principio)
            letra_final = letra
    
            
                
                
    print("a: ", cant_apartado_1)
    print("b: ", cant_apartado_2)
    print("c: ", cant_apartado_3)


if __name__ == "__main__":
    principal()
