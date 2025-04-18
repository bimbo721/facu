cont1 = 0
cont2 = 0
cont3 = 0
ventas_en_cero = 0
total_autos = 0
total = 0

ventas = int(input("Ingrese la cantidad de autos vendidos (-1 para terminar): "))

while ventas != -1:
    if ventas > 0 and ventas < 10000:
        cont1 += 1
    if ventas == 0: ventas_en_cero = "si hubo"
    
    if ventas >= 10000 and  ventas < 15000:
        cont2 += 1
    if ventas > 15000:
        cont3 += 1    
     
    total = total + ventas
    
    ventas = int(input("Ingrese la cantidad de autos vendidos (-1 para terminar): "))


print("Resultados:")
print("Ventas entre 0 y 9999:", cont1)
print("Ventas entre 10000 y 14999:", cont2)
print("Ventas de 15000 o más:", cont3)
print("Total de autos vendidos:", total)
print("meses en cero:", ventas_en_cero)
    
#TERMINADO LA PUTA MADRE
            
        

        
    
    
    
    












