valor1 = int(input("ingrese el primer valor:"))
valor2 = int(input("ingrese el segundo valor:"))
valor3 = int(input("ingrese el tercer valor:"))

resto1 = valor1 % 5
resto2 = valor2 % 5
resto3 = valor3 % 5

par1 = valor1 % 2
par2 = valor2 % 2
par3 = valor3 % 2

impares = 0
bandera = False

###
if resto1 == 0:
    bandera = True

elif resto2 == 0:
    bandera = True

elif resto3 == 0:
    bandera = True

### 
if par1 == 1:
    impares += 1    
if par2 == 1:
    impares += 1
if par3 == 1:
    impares += 1
    

###
if bandera == True:
    print("uno de los valores es multiplo de 5")
else:
    print("ningun numero es multiplo de 5")

print("numeros impares:", impares)



##
if valor1 > valor2 and valor1 > valor3:
    mayor = valor1
    suma = valor2 + valor3
    if mayor > suma:
        print("el valor ",valor1," es mayor a la suma")
    else:
        print("no,la suma es mayor a", valor1)
elif valor2 > valor3:
    mayor = valor2
    suma = valor1 + valor3
    if mayor > suma:
        print("el valor ",valor2," es mayor a la suma")
    else:
        print("no,la suma es mayor a", valor2)
else:
    mayor = valor3
    suma = valor1 + valor2
    if mayor > suma:
        print("el valor ",valor3," es mayor a la suma")
    else:
        print("no,la suma es mayor a", valor3)     


