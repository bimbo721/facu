numero1 = int(input("ingrese el primer numero:"))
numero2 = int(input("ingrese el segundo numero:"))
numero3 = int(input("ingrese el tercer numero:"))



numero_mayor = max(numero1, numero2, numero3)
numero_menor = min(numero1, numero2, numero3)

if numero2 == numero_mayor and numero3 == numero_menor:
    numero_medio = numero1
elif numero2 == numero_menor and numero3 == numero_mayor:
    numero_medio = numero1
elif numero1 == numero_mayor and numero3 == numero_menor:
    numero_medio = numero2
elif numero1 == numero_menor and numero3 == numero_mayor:
    numero_medio = numero2
elif numero1 == numero_mayor and numero2 == numero_menor:
    numero_medio = numero3
elif numero1 == numero_menor and numero2 == numero_mayor:
    numero_medio = numero3

numeros_ordenados = numero_mayor, numero_medio , numero_menor

print("nuemeros ordenados de mayor a menor:",numeros_ordenados)

resto = numero_mayor % numero_medio

if resto == numero_mayor or resto == numero_menor:
    print("el tercero es el resto de la division de los dos primeros")










