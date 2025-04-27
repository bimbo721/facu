dividendo = int(input("Ingrese un numero entero de no mas de tres digitos:"))


if dividendo > 0 and dividendo <1000:
    cociente1 = dividendo // 9
    resto1 = dividendo % 9

    cociente2 = cociente1 // 9
    resto2 = cociente1 % 9
    if cociente2 < 9:
        restos_str = str(cociente2) + str(resto2) + str(resto1)
        print("numero convertido en base 9:",restos_str)
        print("cocientes:",cociente1,",",cociente2)
    else:
        cociente3 = cociente2 // 9
        resto3 = cociente2 % 9
    
        restos_str = str(cociente3) + str(resto3) + str(resto2) + str(resto1)
        print("numero convertido en base 9:",restos_str)
        print("cocientes:",cociente1,",",cociente2,",",cociente3)
    
elif dividendo > -1000 and dividendo <0:
        dividendo = abs(dividendo)
        cociente1 = dividendo // 9
        resto1 = dividendo % 9

        cociente2 = cociente1 // 9
        resto2 = cociente1 % 9
        if cociente2 < 9:
            if cociente2 == 0:
                restos_str = str("-") + str(resto2) + str(resto1)
            else:
                restos_str = str("-") + str(cociente2) + str(resto2) + str(resto1)
            print("numero convertido en base 9:",restos_str)
            print("cocientes:",cociente1,",",cociente2)
        else:
            cociente3 = cociente2 // 9
            resto3 = cociente2 % 9
            restos_str = str("-") + str(cociente2) + str(resto3) + str(resto2) + str(resto1)
            print("numero convertido en base 9:",restos_str)
            print("cocientes:",cociente1,",",cociente2,",",cociente3)
else:
    print("Valor no admitido")



    













