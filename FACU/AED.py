#beneficiario = input("ingrese el nombre y apellido del beneficiario:")
codigo = input("ingrese el codigo de identificacion de la transferencia:")
#monto_nominal = int(input("ingrese el valor a transferir:"))



if "ARS" in codigo:
    print("es valido")
elif "USD" in codigo:
    print("es valido")
elif "EUR" in codigo:
    print("es valido")
elif "JPY" in codigo:
    print("es valido")

else: 
    print("no es valido")

    






