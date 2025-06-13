def es_vocal(letra):
    return letra in "aeiouAEIOUáéíóúÁÉÍÓÚ"

def calculo_promedio(cant_palabras, cant_letras_totales):
    return cant_letras_totales / cant_palabras

def principal():
    texto = input("ingrese el texto: ")
    valor_usuario = int(input("ingrese un valor: "))
    #m = open("entrada.txt")
    #texto = m.read()
    #m.close()
    cant_palabras = 0
    cant_letras_en_palabra = 0
    cant_apartado_1 = 0
    bandera_hay_vocales_distintas = False
    primer_vocal = ""
    bandera_habia_vocal = False
    cant_apartado_2 = 0
    palabra_anterior = ""
    cant_apartado_3 = 0
    cant_letras_totales = 0
    palabra = ""
    promedio_letras = 0
    cant_palabra_anterior = 0
    #El águila vuela alto sobre las montañas nevadas al amanecer.
    
    for letra in texto:
        if letra == " " or letra == ".":
            cant_palabras += 1

            if bandera_hay_vocales_distintas:
                cant_apartado_1 += 1
                
            cant_palabra_anterior = len(palabra_anterior)
            
            if cant_palabra_anterior % cant_letras_en_palabra == 0:
                cant_apartado_2 += 1
            
            if cant_letras_en_palabra > valor_usuario:
                cant_apartado_3 += 1
            
            cant_letras_en_palabra = 0
            bandera_hay_vocales_distintas = False
            primer_vocal = ""
            bandera_habia_vocal = False
            palabra_anterior = palabra
            palabra = ""

        else:
            cant_letras_en_palabra += 1
            cant_letras_totales += 1
            palabra += letra
            
            if es_vocal(letra) and bandera_habia_vocal == False:
                primer_vocal = letra
                bandera_habia_vocal = True
                
            if es_vocal(letra) and letra != primer_vocal and bandera_habia_vocal:
                bandera_hay_vocales_distintas = True
                   
    promedio_letras = calculo_promedio(cant_palabras, cant_letras_totales)
    palabra = ""
    cant_apartado_4 = 0
    cant_letras_en_palabra = 0

    
    for letra in texto:
        if letra == " " or letra == ".":
            
            if cant_letras_en_palabra > promedio_letras:
                cant_apartado_4 += 1 
            
            palabra = ""
            cant_letras_en_palabra = 0
        
        else:
            palabra += letra
            cant_letras_en_palabra += 1
    
    
    print("a: ", cant_apartado_1)
    print("b: ", cant_apartado_2)
    print("c: ", cant_apartado_3)
    print("d: ", cant_apartado_4)

if __name__ == "__main__":
    principal()