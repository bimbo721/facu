import os.path

m = open("")

tamaño = os.path.getsize("nombre del archivo")
#retorna el tamaño de bytes del archivo(la cantidad de arreglos)

#eof: final del archivo

# concepto de file pointer: es una variable de tipo ENTERO que
#indica el subindice del byte que esta siendo leido del archivo
#ayuda en la busqueda secuencial

#la funcion tell() devuelve el valor entero del file pointer
m.tell()

#while m.tell() < t:

#la funcion seek(a,b) sirve para cambiar el valor del file pointer
#a = cuantos bytes debe moverse(saltar) el file pointer
#b = indica desde que subindice se hace ese salto(por defecto es 0)


# m.seek(10, io.SEEK_SET) posiciona a "b" al principio
# m.seek(10, io.SEEK_CUR) posiciona a "b" en el file pointer actual

