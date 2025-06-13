def calculo_procentaje(cant_palabras_3, cant_palabras):
    return cant_palabras_3 / cant_palabras


def principal():
    texto = input("ingrese el texto: ")
    
    cant_palabras = 0
    cant_letras_palabra = 0
    cant_palabras_3 = 0
    cant_letras_totales = 0
    cant_palabras_terminan_s = 0
    letra_anterior = ""
    bandera_d = False
    bandera_r = False
    bandera_dre = False
    cant_palabras_con_dre = 0
    
    for letra in texto:
        if letra == " " or letra == ".":
            cant_palabras += 1

            if cant_letras_palabra == 3:
                cant_palabras_3 += 1

            if letra_anterior == "s":
                cant_palabras_terminan_s += 1

            if bandera_dre:
                cant_palabras_con_dre += 1
            
            cant_letras_palabra = 0
            letra_anterior = ""
            bandera_d = False
            bandera_r = False
            bandera_dre = False

        else:
            cant_letras_palabra += 1
            cant_letras_totales += 1
            
            if letra == "d" and bandera_d == False:
                bandera_d = True
            
            if letra == "r" and bandera_d:
                bandera_r = True
                bandera_d = False
                
            if letra == "e" and bandera_r:
                bandera_dre = True
                
                
            letra_anterior = letra
         
    porcentaje = calculo_procentaje(cant_palabras_3, cant_palabras)
    print("a: ", cant_palabras_3)
    print("b: ", porcentaje)  
    print("c: ", cant_palabras_terminan_s)  
    print("d: ", cant_palabras_con_dre)          
                    
if __name__ == "__main__":
    principal()