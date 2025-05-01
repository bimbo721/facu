primer_mes = int(input("ingrese el monto del primermes:"))
segundo_mes = int(input("ingrese el monto del segundo mes:"))
tercer_mes = int(input("ingrese el monto del tercer mes:"))


total_monto = primer_mes + segundo_mes + tercer_mes
menor_monto = min(primer_mes, segundo_mes, tercer_mes)

premio = menor_monto * 50 // 100



if total_monto > 1000:
    premio_adicional = menor_monto * 10 //100
    premio_final = premio + premio_adicional
    
    print(premio_final)
else:
    print("el premio es:", premio)


