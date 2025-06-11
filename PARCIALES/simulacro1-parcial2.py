def promedioentero(suma,cant_palabras_mas_consonantes_que_vocales):
    return suma // cant_palabras_mas_consonantes_que_vocales

def es_consonante(letra):
    return letra in "qwrtypsdfghjklñzxcvbnmQWRTYPSDFGHJKLÑZXCVBNM"

def es_vocal(letra):
    return letra in "aeiouAEIOU"


def principal():
    m = open("textosimulacro1.txt")
    texto = m.read()
    m.close()
    print(texto)

    #cantidades:
    cant_letras_en_palabra = 0
    cant_palabras = 0
    longitud = 0
    cant_palabras_mas_consonantes_que_vocales = 0
    cant_vocales = 0
    cant_consonantes = 0
    suma = 0
    cant_palabras_primer_apartado = 0
    cant_palabras_2_da = 0
    cant_de_dyvocal = 0

    #banderas:
    bandera_empieza_digito = False
    bandera_mayuscula = False
    bandera_tiene_b = False
    empieza_con_vocal = False
    bandera_m_a = False
    letra_anterior = ""

    for letra in texto:
        if letra == " " or letra == ".":
            cant_palabras += 1

            if bandera_empieza_digito == True and bandera_mayuscula == False:
                cant_palabras_primer_apartado += 1

            if bandera_tiene_b and empieza_con_vocal:
                if cant_letras_en_palabra > longitud:
                    longitud = cant_letras_en_palabra

            if (cant_consonantes > cant_vocales) and bandera_m_a == False:
                suma += cant_letras_en_palabra
                cant_palabras_mas_consonantes_que_vocales += 1

#mucho ojo aca,hay que pasarle a la funcion la letra anterior especificamente
            if es_vocal(letra_anterior) and cant_de_dyvocal >= 2:
                cant_palabras_2_da += 1


            cant_letras_en_palabra = 0
            cant_vocales = 0
            cant_consonantes = 0
            bandera_mayuscula = False
            bandera_tiene_b = False
            empieza_con_vocal = False
            bandera_empieza_digito = False
            bandera_m_a = False
            cant_de_dyvocal = 0


        else:
            cant_letras_en_palabra += 1

            if cant_letras_en_palabra == 1 and letra in "013579":
                bandera_empieza_digito = True

            if letra in "QWERTYUIOPASDFGHJKLÑZXCVBNM":
                bandera_mayuscula = True

            if cant_letras_en_palabra == 1 and es_vocal(letra):
                empieza_con_vocal = True

            if letra == "b" or letra == "B":
                bandera_tiene_b = True

            if letra == "m" or letra == "a":
                bandera_m_a = True

            if es_vocal(letra):
                cant_vocales += 1

            if es_consonante(letra):
                cant_consonantes += 1

            if letra_anterior == "d" and es_vocal(letra):
                cant_de_dyvocal += 1

        letra_anterior = letra

    promedio = promedioentero(suma, cant_palabras_mas_consonantes_que_vocales)
    print("Primer resultado:", cant_palabras_primer_apartado)
    print("Segundo resultado:", longitud)
    print("Tercer resultado:", promedio)
    print("Cuarto resultado:", cant_palabras_2_da)

if __name__ == "__main__":
    principal()