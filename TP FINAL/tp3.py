from modulostp3 import *

def principal():
    op = -1
    vector = []
    while op != 0:
        print("Opciones:")
        print("1)cargar envios")
        print("2)mostrar resultados")
        print("3)buscar")
        print("4)mayores")
        print("0)salir")
        op = validar(input("Ingrese opción: "))
        op = int(op)


        if op == 1:
            distintos = procesar_archivo_csv(vector)
            r11 = len(vector)
            r12 = distintos
#############
            i = int(input("ingrese un valor i: "))
            buscar_valor(vector,i)


        if op == 2:
            if not vector:
                print("error,primero declare el vector")
            else:
                m_comisiones = comisiones(vector)
                r21 = porcentaje_comision(m_comisiones)
                round(r21,2)

                #r22
                matriz_2 = calculo_impositivo(vector,m_comisiones)
                r22 = identificador(matriz_2,vector,m_comisiones)


                #r23
                impuesto_22 = matriz_2[0][0]
                monto_base_22 = m_comisiones[0][1]

                monto_final_orden_22 = monto_base_22 - impuesto_22

                tasa = vector[0].tasa_conv
                r23_final = monto_final_orden_22 * tasa

                print("r2.1:", r21)
                print("r2.2:", r22)
                print("r2.3:", r23_final)

                ## extra

                resultado = sumatoria_impuestos_por_par_monedas(vector, matriz_2)
                n = len(resultado)
                i = 0
                while i < n - 1:
                    j = i + 1
                    while j < n:
                        if (resultado[i][0] > resultado[j][0]) or (resultado[i][0] == resultado[j][0] and resultado[i][1] > resultado[j][1]):
                            aux = resultado[i]
                            resultado[i] = resultado[j]
                            resultado[j] = aux
                        j = j + 1
                    i = i + 1


                generar_nuevo_archivo(vector)


                print("r2.4:")
                k = 0
                while k < len(resultado):
                    mo = resultado[k][0]
                    mp = resultado[k][1]
                    total = resultado[k][2]
                    print("moneda_origen=" + str(mo) + ", moneda_pago=" + str(mp) + ":", round(total, 2))
                    k = k + 1


        if op == 0:
            print("el programa terminó")

if __name__ == "__main__":
    principal()
