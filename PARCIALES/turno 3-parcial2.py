def es_mayuscula(letra):
    return letra in "QWERTYUIOPASDFGHJKLÑZXCVBNM"

def digito(letra):
    return letra in "0123456789"

def vocal(letra):
    return letra in "aeiouAEIOU"

def calculo_promedio(cant_palabras_que_cumplen, cant_letras_palabra_que_cumplen):
    return cant_letras_palabra_que_cumplen // cant_palabras_que_cumplen
 
            
def principal():
    #m = open("entrada.txt")
    #texto = m.read()
    #m.close()
    
    texto = input("ingrese el texto: ")
    
    cant_palabras = 0
    cant_letras_palabra = 0
    bandera_empieza_mayusc = False
    cant_palabras_apartado_1 = 0
    bandera_digito_4_posi = False
    bandera_hay_p_o_n = False
    palabra = ""
    bandera_tiene_vocal = False
    bandera_tiene_un_digito = False
    cant_palabras_que_cumplen = 0
    longitud = 0
    bandera_empieza_con_vocal = False
    letra_anterior = ""
    bandera_silaba_fa = False
    cant_apartado_4 = 0
    bandera_tiene_dos_digitos = False
    cant_letras_palabra_que_cumplen = 0
    promedio = 0
    
    for letra in texto:
        if letra == " " or letra == ".":
            cant_palabras += 1
        
            if bandera_digito_4_posi and bandera_empieza_mayusc:
                cant_palabras_apartado_1 += 1
            
            if bandera_tiene_vocal and bandera_tiene_dos_digitos:
                cant_palabras_que_cumplen += 1
                cant_letras_palabra_que_cumplen += cant_letras_palabra
            
            if bandera_hay_p_o_n:
                if cant_letras_palabra > longitud:
                    longitud = cant_letras_palabra
            
            if bandera_silaba_fa and bandera_empieza_con_vocal:
                cant_apartado_4 += 1
                
            
            bandera_empieza_mayusc = False
            bandera_digito_4_posi = False
            palabra = ""
            bandera_tiene_vocal = False
            cant_letras_palabra = 0
            bandera_tiene_un_digito = False
            bandera_hay_p_o_n = False
            bandera_empieza_con_vocal = False
            bandera_silaba_fa = False
            bandera_tiene_dos_digitos = False
         
        else:
            cant_letras_palabra += 1
            
            if cant_letras_palabra == 1 and es_mayuscula(letra):
                bandera_empieza_mayusc = True

            if (cant_letras_palabra == 4 and digito(letra)) and bandera_empieza_mayusc:
                bandera_digito_4_posi = True
            
            if letra == "p" or letra == "n":
                bandera_hay_p_o_n = True
                

            if vocal(letra):
                bandera_tiene_vocal = True
            
            if digito(letra) and bandera_tiene_un_digito == False:
                bandera_tiene_un_digito = True
            else:
                if digito(letra) and bandera_tiene_un_digito == True:
                    bandera_tiene_dos_digitos = True
                
            if cant_letras_palabra == 1 and vocal(letra):
                bandera_empieza_con_vocal = True
            
            if (letra == "a" or letra == "A") and (letra_anterior == "F" or letra_anterior == "f") and bandera_silaba_fa == False:
                bandera_silaba_fa = True
            
            letra_anterior = letra
            palabra += letra
            
    if cant_palabras_que_cumplen != 0 and cant_letras_palabra_que_cumplen != 0:
        promedio = calculo_promedio(cant_palabras_que_cumplen, cant_letras_palabra_que_cumplen)        
    
    print("1: ", cant_palabras_apartado_1)
    print("2: ", longitud)
    print("3: ", promedio)
    print("4: ", cant_apartado_4)
    
if __name__ == "__main__":
    principal()