def principal():
    
    n = int(input("cuantos elementos va a tener su vector?: "))
    vector = [0] * n
    cant_repite_ultimo_digito = 0

    rango = len(vector)
    for i in range(rango):
        elemento = int(input("ingrese los elementos del vector: "))
        
        vector[i] = elemento
    
    primer_digito = [0]
    ultimo_digito = vector[-1]
    
    for i in vector:
        if ultimo_digito == i:
            cant_repite_ultimo_digito += 1
    
    
    nuevo_vector = []
    for i in vector:
        if i < primer_digito:
            nuevo_vector.append(vector[i])
    
    
    print("1: ", cant_repite_ultimo_digito, "veces")
    if nuevo_vector == []:
        print("no hay elementos menores al primer valor ingresado")
    else:
        print("2: ",nuevo_vector)
    
principal()
    
     







