def mitad_palabra(cant_letras_en_palabra):
    return cant_letras_en_palabra // 2


def principal():
    m = open("silaba de.txt")
    texto = m.read()
    m.close()

    cant_palabras_con_digitos = 0
    cant_letras_en_palabra = 0
    cant_palabras = 0
    bandera_hay_digito = False
    bandera_de = False
    cant_palabras_men_3 = 0
    cant_palabras_4_6 = 0
    cant_palabras_mas_6 = 0
    longitud = 0
    letra_anterior = ""
    cant_palabras_con_de = 0
    posicion = 0


    for letra in texto:

        if letra == " " or letra == ".":
            cant_palabras += 1
            mitad = mitad_palabra(cant_letras_en_palabra)

            if bandera_de and posicion <= mitad:
                cant_palabras_con_de += 1

            if bandera_hay_digito:
                cant_palabras_con_digitos += 1

            if cant_letras_en_palabra <= 3:
                cant_palabras_men_3 += 1

            elif cant_letras_en_palabra >= 4 and cant_letras_en_palabra <= 6:
                cant_palabras_4_6 += 1

            elif cant_letras_en_palabra > 6:
                cant_palabras_mas_6 += 1

            if cant_letras_en_palabra > longitud:
                longitud = cant_letras_en_palabra


            cant_letras_en_palabra = 0
            bandera_hay_digito = False
            bandera_de = False
            posicion = 0

        else:
            cant_letras_en_palabra += 1

            if letra in "0123456789":
                bandera_hay_digito = True

            if (letra_anterior == "d" and letra == "e") and bandera_de == False:
                bandera_de = True
                posicion = cant_letras_en_palabra

        letra_anterior = letra


    print("a: ",cant_palabras_con_digitos)
    print("b: ",cant_palabras_men_3, cant_palabras_4_6, cant_palabras_mas_6)
    print("c: ",longitud)
    print("d: ",cant_palabras_con_de)

if __name__ == "__main__":
    principal()