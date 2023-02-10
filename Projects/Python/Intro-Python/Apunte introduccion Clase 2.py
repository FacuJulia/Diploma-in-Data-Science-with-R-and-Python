# # GENERADORES

# #cantidad variable en el argumento de la funcion "*"
# def devuelve_ciudades(*ciudades):
# 	for elemento in ciudades:
# 		# opcion 1
# 		yield  elemento	

# 		# opcion 2
# 		#for letra in elemento:
# 		#	yield letra
		
# 		# opcion 3
# 		#yield from elemento


# ciudades_devueltas = devuelve_ciudades("buenos aires", "salta", "tucuman", "mar del plata")

# print(next(ciudades_devueltas))
# print(next(ciudades_devueltas))
# print(next(ciudades_devueltas))



# # EXCEPCIONES
# while 1==1:
# 	try:
# 		a = int(input("Dividendo: "))
# 		b= int(input("Divisor: "))
# 		c = int(a/b)
# 		break
# 	except ValueError:
# 		print("Los valores introducidos son incorrectos, intentalo de nuevo")
# 	except ZeroDivisionError:
# 		print("No se puede dividir por cero, intentalo de nuevo")
# 	finally:
# 		print("Bye Bye!")

# print("Cociente: ", c, "Resto: ", a-b*c)
# print("FIN")




# EXCEPCIONES
# import math

# def raiz(a):
# 	if a<0:
# 		raise TypeError("Con negativos no puedo")
# 	else:
# 		b=math.sqrt(a)
# 	return b

# c = float(input("Ingresar numero: "))

# try:
# 	d=raiz(c)
# 	print("La raiz de ",c,"es ",d)
# except TypeError as MsjError:
# 	print(MsjError)

# print("Fin")




# VARIABLE LOCAL Y GLOBAL
# a=1
# print("Antes",a)

# def suma(b,c):
# 	a=3
# 	print("Funcion",a)
# 	return b+c

# print("Despues",a)
# print("Suma", suma(a,a))



# MANEJO DE ARCHIVO
# import os
# import shutil

# print(os.getcwd())

# for l in os.listdir():
# 	print(l)
 
# g = os.walk("f:/")

# for i in range(1):
# 	print(next(g))

# print(os.getcwd())
# os.chdir("..")
# print(os.getcwd())

#print(os.getcwd())
#os.makedirs("abc")

#shutil.copy2("Programación Python.pdf", "Ejercicios")

#os.remove("Programación Python - copia.pdf")

#os.makedirs("abc")
#shutil.rmtree("abc")



# FS - PyFilesystem
from fs.osfs import OSFS

# CARPETA PERSONAL VISUALIZACION LISTA
#home_fs = OSFS("~/")
#print(home_fs.listdir("/"))

# CARPETA ACTUAL VISUALIZACION GRAFICA
#home_fs = OSFS(".")
#home_fs.tree()


# CARPETA ACTUAL CREO UN ARCHIVO Y ESCRIBO
#home_fs = OSFS(".")
#home_fs.writetext("Prueba.txt", "Probando 1 2 3...")
#home_fs.close()

# INFORMACION DEL DIRECTORIO LOCAL MEJOR QUE LISTDIR
#home_fs = OSFS(".")
#for entrada in home_fs.scandir(path = "."):
#	print(entrada.name)
#print(home_fs.listdir("."))


# CLASIFICAR ARCHIVOS O DIRECTORIOS
# home_fs = OSFS(".")
# for entrada in home_fs.scandir(path = "."):
# 	if entrada.is_dir:
# 		print("Directorio: ", entrada.name)
# 	elif entrada.is_file:
# 		print("Archivo: ", entrada.name)
# 	else:
# 		print("Ni archivo ni directorio: ", entrada.name)


# TAMAÑO DE ARCHIVOS
# home_fs = OSFS(".")
# for entrada in home_fs.scandir(path = "."):
# 	print(entrada.name, home_fs.getsize(entrada.name))


# RECORRER UN DIRECTORIO PARTICULAR
# import os
# k=0
# for l in os.walk("C:/Users/Facu/Dropbox/Ciencia datos/0- Nivelacion/Python"):
# 	print(k,l)
# 	k=k+1

#Cada uno de los elementos que devuelve walk es un tupla con tres elementos:
#La raíz de la entrada que estoy recorriendo
#Una tupla con los nombres de los archivos que cuelgan de esa entrada
#Una tupla con los nombres de los directorios que cuelgan de esa entrada
#Cuando agota la recorrida de la entrada salta recursivamente por sus directorios.


# RECORRER UN DIRECTORIO PARTICULAR Y CLASIFICAR ARCHIVOS O DIRECTORIOS SIMILAR A "GLOBING"
# import os
# k=0
# for root, dirs, files in os.walk("C:/Users/Facu/Dropbox/Ciencia datos/0- Nivelacion/Python", topdown=True):
# 	k=k+1
# 	print("Vamos x ", k, " root ", root)
# 	for name in files:
# 		print(os.path.join(root, name))
# 	for name in dirs:
# 		print(os.path.join(root, name))


# MOVER Y COPIAR ARCHIVOS 
# import shutil
# shutil.copy("Prueba.txt", "Prueba2.txt")

# Otros comandos move(), copy(), movedir(), copydir()

# MANEJO DE ARCHIVOS
# archivo = open("Prueba.txt")
# texto = archivo.read()
# print(texto)
# archivo.close()

# Escribir
#archivo = open("Prueba.txt","w")
#for i in range(10):
#	archivo.write("Paso "+str(i)+"\n")
#archivo.close()

# Leer
#archivo = open("Prueba.txt","r")
#texto = archivo.read()
#print(texto)
#archivo.close()


# BUSQUEDA DE PATRONES DE TEXTO
import re
# patron = re.compile("a")
# print(patron.match("amigo"))
# print(patron.match("pepa"))
# print(patron.match("pepe"))
# print("\n")

# print(patron.search("amigo"))
# print(patron.search("pepa"))
# print(patron.search("pepe"))
# print("\n")

# patron = re.compile("[abg]")
# print(patron.findall("amigo"))
# print(patron.findall("pepa"))
# print(patron.findall("papa"))
# print("\n")
#patron = re.compile("[^a]")
#print(patron.findall("amigo"))
#print(patron.findall("pepa"))
#print(patron.findall("papa"))
# print("\n")

#print(patron.finditer("amigo"))
#print(patron.finditer("pepa"))
#print(patron.finditer("pepe"))

# match(): El cual determinada si la regex tiene coincidencias en el comienzo del texto.
# search():El cual escanea todo el texto buscando cualquier ubicación donde haya una coincidencia.
# findall(): El cual encuentra todos los subtextos donde haya una coincidencia y nos devuelve estas coincidencias como una lista.
# finditer(): El cual es similar al anterior pero en lugar de devolvernos una lista nos devuelve un generador.

# SECUENCIAS DE ESCAPE
# \n 		Nueva línea (new line). El cursor pasa a la primera posición de la línea siguiente.
# \t 		Tabulador. El cursor pasa a la siguiente posición de tabulación.
# \\ 		Barra diagonal inversa
# \v 		Tabulación vertical.
# \ooo 		Carácter ASCII en notación octal.
# \xhh 		Carácter ASCII en notación hexadecimal.
# \xhhhh 	Carácter Unicode en notación hexadecimal.

# METACARACTERES
# ^ 		inicio de línea.
# $ 		fin de línea.
# \A 		inicio de texto.
# \Z 		fin de texto.
# . 		cualquier caracter en la línea.
# \b 		encuentra límite de palabra.
# \B 		encuentra distinto a límite de palabra.

# METACARACTERES PREDEFINIDOS
# \w 		un caracter alfanumérico (incluye "_").
# \W 		un caracter no alfanumérico.
# \d 		un caracter numérico.
# \D 		un caracter no numérico.
# \s 		cualquier espacio (lo mismo que [ \t\n\r\f]).
# \S 		un no espacio.

# METACARACTERES ITERADORES
# * 		cero o más, similar a {0,}.
# + 		una o más, similar a {1,}.
# ? 		cero o una, similar a {0,1}.
# {n} 		exactamente n veces.
# {n,} 		por lo menos n veces.
# {n,m} 	por lo menos n pero no más de m veces.
# *? 		cero o más, similar a {0,}?.
# +? 		una o más, similar a {1,}?.
# ?? 		cero o una, similar a {0,1}?.
# {n}? 		exactamente n veces.
# {n,}? 	por lo menos n veces.
# {n,m}? 	por lo menos n pero no más de m veces.

# # PAGINA 105!!!!!!!!!!!
# # PAGINA 122!!!!!!!!!!!


