nombre = str(input("ingrese el nombre:"))
apellido = str(input("ingrese el apellido:"))
dominio = str(input("ingrese el legajo:"))

nombre = nombre.lower()
apellido = apellido.lower()
dominio = dominio.lower()

primera_letra_nombre = nombre[0]
primera_letra_apellido = apellido[0]

if primera_letra_nombre != primera_letra_apellido:
    mail = (primera_letra_nombre + apellido + "@" + dominio)
else:
    mail = (nombre + "." + apellido + "@" + dominio)


print(mail)

