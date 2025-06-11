
def cantidad_empiezan_vocal(letra,vocales):
    if letra in vocales:
        cant_empiezan_vocal += 1

def principal():
    texto = str("ingrese el texto: ")
    
    for letra in texto:
        vocales = "aeiouAEIOU"
        if letra == " " or ".":
            cant_palabras += 1
            bandera_palabra = True
        else:
            vocales_principio = cantidad_empiezan_vocal(letra,vocales)
            bandera_palabra = False

principal()


