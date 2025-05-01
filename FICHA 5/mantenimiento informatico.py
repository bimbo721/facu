identificacion1 = input("ingrese el numero de identifacion: ")
tiempo1 = int(input("ingrese el tiempo que tardo la reparacion: "))
causa1 = int(input("ingrese el problema,1 Problema de Hardware, 2 Problema de Software: "))

if causa1 == 1:
    causa1 = "problema de hardware"
else:
    causa1 = "problema de software/n"


identificacion2 = input("ingrese el numero de identifacion: ")
tiempo2 = int(input("ingrese el tiempo que tardo la reparacion: "))
causa2 = int(input("ingrese el problema,1 Problema de Hardware, 2 Problema de Software: "))

if causa2 == 1:
    causa2 = "problema de hardware"
else:
    causa2 = "problema de software/n"
    
    
identificacion3 = input("ingrese el numero de identifacion: ")
tiempo3 = int(input("ingrese el tiempo que tardo la reparacion: "))
causa3 = int(input("ingrese el problema,1 Problema de Hardware, 2 Problema de Software: "))

if causa3 == 1:
    causa3 = "problema de hardware"
else:
    causa3 = "problema de software/n/n/n"



#a
tiempo_total = tiempo1 + tiempo2 + tiempo3
print("el timepo total de tareas de mantenimiento es:", tiempo_total,"minutos")

#b
if tiempo1 > tiempo2 and tiempo1 > tiempo3:
    print("la pc que mayor tiempo tuvo de mantenimiento fue la numero", identificacion1)
elif tiempo2 > tiempo3:
    print("la pc que mayor tiempo tuvo de mantenimiento fue la numero:", identificacion2)
else:
    print("la pc que mayor tiempo tuvo de mantenimiento fue la numero:", identificacion3)
    

#c
tiempo_promedio = tiempo_total // 3
print("tiempo promedio:", tiempo_promedio,"minutos")

#d
if causa1 == causa2 and causa1 == causa3:
    print("todas las computadoras tuvieron problemas de hardaware")
else:
    print("los problemas fueron variados")




