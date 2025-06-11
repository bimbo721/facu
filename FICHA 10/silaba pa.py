



def principal():
    #m = open("entrada.txt")
    #texto = m.read()
    #m.close()
    texto = input("ingrese el texto: ")
    cant_palabras_pa = 0
    cant_palabras = 0
    cant_letras = 0
    cant_palabras_n = 0
    letra_anterior = ""
    palabra_procesada = ""
    
    
    for letra in texto:
        if letra == " " or letra == ".":
            palabra_procesada = ""
            cant_palabras += 1
            
            
        else:
            cant_letras += 1
            palabra_procesada += letra 
            

            
            
    letra_anterior = letra
        
        
    print(palabra_procesada)





principal()


