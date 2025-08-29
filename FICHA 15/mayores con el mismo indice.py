def principal():

    primer_vector = []
    segundo_vector = []
    tercer_vector = []

    tamaño = int(input("ingrese el tamaño de los vectores:"))

    for i in range(tamaño):
        a = int(input("ingrese los numeros del primer vector:"))
        primer_vector.append(a)


    for i in range(tamaño):
        b = int(input("ingrese los numeros del segundo vector:"))
        segundo_vector.append(b)


    for i in range(len(primer_vector)):
        if primer_vector[i] > segundo_vector[i]:
            tercer_vector.append(primer_vector[i])
        else:
            tercer_vector.append(segundo_vector[i])


    print("tercer vector: ", tercer_vector)

principal()