from modulostp3 import *


def principal():
    op = -1
    vector = []
    m_comisiones = []
    archivo = 'archivocomision.dat'
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
            procesar_archivo_csv(vector)

            i = int(input("ingrese un valor i: "))
            buscar_valor(vector,i)

        if op == 2:
            if not vector:
                print("error,primero declare el vector")
            else:
                if not m_comisiones:
                    m_comisiones = comisiones(vector)

                generar_nuevo_archivo(vector,m_comisiones,archivo)

                #r2.1
                print('r2.1:')
                mostrar_archivo(archivo)
                print()
                #r2.2
                print("r2.2:")
                mostrar_envios_mayorcomision(archivo)

        if op == 3:
            if not vector:
                print("error,primero declare el vector")
            else:
                id_dest = input("Ingrese la identificación del destinatario a buscar: ")
                r31, r32 = buscar_modificar_por_id(vector, id_dest)
                print("r3.1:", r31)
                print("r3.2:", r32)

        if op == 4:
            if not vector and not os.path.exists(archivo):
                print("error,primero declare el vector")
            else:
                if not m_comisiones:
                    m_comisiones = comisiones(vector)

                m_impuestos_mfinal = calculo_impositivo(vector, m_comisiones)
                m_max_mfinal = generar_matriz_maximos(vector,m_impuestos_mfinal)

                print('r4.1:')
                mostrar_codigo_op4(m_max_mfinal)

        if op == 0:
            print("el programa terminó")

if __name__ == "__main__":
    principal()