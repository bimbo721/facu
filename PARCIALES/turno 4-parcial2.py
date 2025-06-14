def vocales(letra):
    return letra in "aeiouAEIOUÁÉÍÓÚáéíóú"

def digitos(letra):
    return letra in "0123456789"

def consonante(letra):
    return letra in "qrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM"

def calculo_procentaje(cant_palabras_no_digitos, cant_palabras):
    return  cant_palabras_no_digitos * 100 // cant_palabras


def principal():
    m = open("entrada.txt")
    texto = m.read()
    m.close()
    
    
    cant_palabras = 0
    cant_letras_en_palabra = 0
    cant_consonantes_en_palabra = 0
    cant_digito_en_palabra = 0
    cant_vocales_en_palabra = 0
    cant_apartado_1 = 0
    bandera_tiene_soc = False
    longitud = 99999999999
    bandera_tiene_digito = False
    cant_palabras_no_digitos = 0
    bandera_tiene_n = False
    bandera_empieza_v = False
    bandera_empieza_vi = False
    cant_apartado_4 = 0

    
    for letra in texto:
        print(letra)
        if letra == " " or letra == ".":
            cant_palabras += 1
            
            if (cant_digito_en_palabra > cant_vocales_en_palabra) and (cant_consonantes_en_palabra == 1):
                cant_apartado_1 += 1
            
            if bandera_tiene_digito == False:
                cant_palabras_no_digitos += 1
            
            if cant_letras_en_palabra < longitud and bandera_tiene_soc:
                longitud = cant_letras_en_palabra
            
            if bandera_empieza_vi and bandera_tiene_n:
                cant_apartado_4 += 1
            
            cant_letras_en_palabra = 0
            cant_consonantes_en_palabra = 0
            cant_digito_en_palabra = 0
            cant_vocales_en_palabra = 0
            bandera_tiene_soc = False
            bandera_tiene_digito = False
            bandera_tiene_n = False
            bandera_empieza_v = False
            bandera_empieza_vi = False
            
            
        else:
            cant_letras_en_palabra += 1
            
            if digitos(letra):
                cant_digito_en_palabra += 1
                bandera_tiene_digito = True
            
            if vocales(letra):
                cant_vocales_en_palabra += 1
            
            if consonante(letra):
                cant_consonantes_en_palabra += 1
                
            if letra in "sS" or letra in "cC":
                bandera_tiene_soc = True    
            
            if cant_letras_en_palabra == 1 and letra in "vV":
                bandera_empieza_v = True
            
            if (cant_letras_en_palabra == 2 and letra in "iI") and bandera_empieza_v:
                bandera_empieza_vi = True
                
            if letra in "nN":
                bandera_tiene_n = True
            
            
    porcentaje = calculo_procentaje(cant_palabras_no_digitos, cant_palabras)        

    print("1: ", cant_apartado_1)
    print("2: ", longitud)
    print("3: ", porcentaje)
    print("4: ", cant_apartado_4)

if __name__ == "__main__":
    principal()