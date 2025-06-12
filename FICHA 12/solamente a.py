def tiene_vocal_no_a(letra):
    return letra in "eiouEIOU"

def calculo_procentaje(cant_palabras_con_1_a, cant_palabras):
    return cant_palabras_con_1_a * 100 / cant_palabras

#el agua clara salta por las piedras.
def principal():
    
    texto = input("ingrese el texto: ")

    cant_palabras = 0
    cant_letras_palabra = 0
    longitud = 0
    bandera_hay_a = False
    cant_palabras_con_1_a = 0
    bandera_tiene_otras_vocales = False
    
    for letra in texto:
        if letra == " " or letra == ".":
            cant_palabras += 1
            
            
            if cant_letras_palabra > longitud:
                longitud = cant_letras_palabra
                
            if bandera_hay_a and bandera_tiene_otras_vocales == False:
                cant_palabras_con_1_a += 1
                
        
            cant_letras_palabra = 0
            bandera_hay_a = False
            bandera_tiene_otras_vocales = False

        else:
            cant_letras_palabra += 1
            if tiene_vocal_no_a(letra):
                bandera_tiene_otras_vocales = True
                
            if letra == "a" or letra == "A":
                bandera_hay_a = True
            
    porcentaje = calculo_procentaje(cant_palabras_con_1_a, cant_palabras)
    print("a: ",longitud)
    print("b: ", cant_palabras_con_1_a)
    print("c: ",porcentaje)

if __name__ == "__main__":
    principal()