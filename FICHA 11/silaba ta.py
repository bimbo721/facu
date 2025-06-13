def calculo_porcentaje(cant_letras_totales, cant_vocales):
    return cant_vocales * 100 / cant_letras_totales

def es_vocal(letra):
    return letra in "aeiouAEIOU"
    
def longitud_palabra(cant_letras_totales, cant_palabras):
    return cant_letras_totales / cant_palabras

def principal():
    texto = input("ingrese el texto: ")

    cant_palabras = 0
    cant_letras_palabra = 0
    cant_vocales = 0
    cant_letras_totales = 0
    longitud_promedio = 0
    longitud = 0
    bandera_t = False
    bandera_ta = True
    cant_palabras_con_ta = 0
    
    for letra in texto:
        if letra == "." or letra == " ":
            cant_palabras += 1
            
            if cant_letras_palabra > longitud:
                longitud = cant_letras_palabra
                
            if bandera_t and bandera_ta:
                cant_palabras_con_ta += 1
                
            cant_letras_palabra = 0
            bandera_ta = False
            bandera_t = False

        else:
            cant_letras_palabra += 1
            cant_letras_totales += 1
            
            if es_vocal(letra):
                cant_vocales += 1
                
            if cant_letras_palabra == 1 and letra == "t":
                bandera_t = True
            
            if cant_letras_palabra == 2 and letra == "a":
                bandera_ta = True    
            
    longitud_promedio = longitud_palabra(cant_letras_totales, cant_palabras)
    procentaje = calculo_porcentaje(cant_letras_totales, cant_vocales)
    print("a: ", procentaje)
    print("b: ", longitud_promedio)
    print("c: ", longitud)
    print("d: ", cant_palabras_con_ta)
    
    
if __name__ == "__main__":
    principal()