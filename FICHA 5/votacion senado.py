votos_favor = int(input("ingrese los votos a favor: "))
votos_contra = int(input("ingrese los votos en contra: "))
abstenciones = int(input("ingrese los votos de abstencion: "))

absoluta = votos_contra + abstenciones
cantidad_votos = votos_favor + votos_contra + abstenciones

if votos_favor > absoluta:
    print("la ley fue aprobada por mayoria absoluta")
elif votos_favor > votos_contra:
    print("la ley fue aprobada por mayoria simple")
else:
    print("la ley fue rechazada")
    
senadores = 72
ausentes = senadores - cantidad_votos

if ausentes == 0:
    print("todos estaban presentes")
else:
    print("los senadores ausentes fueron", ausentes)
