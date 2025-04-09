ingreso_mensual = 81000
gasto_mensual = 80000

#if anillados y else if(elif)

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("estas en negativo")
    elif ingreso_mensual - gasto_mensual > 1000:
        print("bien pa, estas bien")
    else:
        print("y pa, estas gastando una banda")
    
elif ingreso_mensual > 1000:
    print("estas bien en latam")

elif ingreso_mensual > 500:
    print("estas bien")

elif ingreso_mensual:
    print("estas mal")
    
