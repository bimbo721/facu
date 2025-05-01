formula1 = input("Ingrese fórmula del partido 1: ")
candidato1 = int(input("ingrese la cantidad de votos obtenida:"))
formula2 = input("Ingrese fórmula del partido 2: ")
candidato2 = int(input("ingrese la cantidad de votos obtenida:"))
formula3 = input("Ingrese fórmula del partido 3: ")
candidato3 = int(input("ingrese la cantidad de votos obtenida:"))


cantidad_votos = candidato1 + candidato2 + candidato3

porcentaje_cand_1 = candidato1 * 100 / cantidad_votos

porcentaje_cand_2 = candidato2 * 100 / cantidad_votos

porcentaje_cand_3 = candidato3 * 100 / cantidad_votos



if porcentaje_cand_1 >= 45:
    electo1 = porcentaje_cand_1
elif porcentaje_cand_2 >= 45:
    electo1 = porcentaje_cand_2
elif porcentaje_cand_3 >= 45:
    electo1 = porcentaje_cand_3
else:
    if porcentaje_cand_1 > 40:
        electo2 = porcentaje_cand_1
    elif porcentaje_cand_2 > 40:
        electo2 = porcentaje_cand_2
    elif porcentaje_cand_3 > 40:
        electo2 = porcentaje_cand_3


#flag = False
#if electo1 >= 45 or electo2 >= 40 and (electo1 - electo2) > 10:
#    flag = True


if electo1 < 45 and electo2 >= 36 :
    candidato1_vuelta = int(input("ingrese la cantidad de votos obtenida:"))
    candidato2_vuelta = int(input("ingrese la cantidad de votos obtenida:"))
    
    cantidad_votos = candidato1_vuelta + candidato2_vuelta
    
    porcentaje_cand_1 = candidato1_vuelta * 100 / cantidad_votos
    porcentaje_cand_2 = candidato2_vuelta * 100 / cantidad_votos
elif porcentaje_cand_1 > porcentaje_cand_2:
    print("el electo 1 es presidente")
else:
    print("el electo 2 gano la segunda vuelta")



print("el presidente es:", formula1)


