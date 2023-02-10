
#	FUNCIONES ; CONDICIONALES
# def sumar(a,b):
# 	c = a + b
# 	return c

# a1 = int(input("Ingrese el numero 1: "))
# b1 = int(input("Ingrese el numero 2: "))

# if a1<b1:
# 	a1 = a1 * 2
# 	print(sumar(a1,b1))
# else:
# 	print(sumar(a1,b1))


#	LISTAS
# colores = ["Rojo", "Amarillo", "Azul"]
# numeros = [1,2,3,4]
# lista = [colores,numeros]
# print(lista[-1][-1])
# colores.append("Negro")
# colores.insert(0,"Blanco")
# colores.extend(colores)
# print(colores.index("Rojo"))
# print("Rojo" in colores)
# colores.remove("Amarillo")
# print("Amarillo" in colores)
# colores.pop()
# print(colores)


#	TUPLAS
# lista_colores = ["Rojo", "Amarillo", "Azul"]
# tupla_colores = ("Rojo", "Amarillo", "Azul")
# tuplaAlista = list(tupla_colores)
# listaAtupla = tuple(lista_colores)
# print(len(lista_colores))
# print(len(tuplaAlista))
# print(lista_colores,tuplaAlista)
# print(tupla_colores, listaAtupla)
# a,b,c = lista_colores
# print(a)
# print(b)
# print(c)


#	DICCIONARIOS
# diccionario_capitales = {"Argentina":"Buenos aires", "Paraguay":"Asuncion", "Peru":"Lima"}
# # print(diccionario_capitales)
# # print(diccionario_capitales["Argentina"])
# # diccionario_capitales["Uruguay"] = "Montevideo"
# # print(diccionario_capitales)
# # del diccionario_capitales["Argentina"]
# # print(diccionario_capitales)
# print(diccionario_capitales.keys())
# print(diccionario_capitales.values())
# print(len(diccionario_capitales))



#	CONDICIONAL 
# a = float(input("Nota: "))

# def evaluar(n):
# 	if n==10:
# 		r = "Sobresaliente"
# 		return r
# 	elif 8.5<n<10:
# 		r = "Excelente"
# 		return r
# 	elif 7.5<n<8.5:
# 		r = "Muy bueno"
# 		return r
# 	elif 6.5<n<7.5:
# 		r = "Bueno"
# 		return r
# 	elif 5.5<n<6.5:
# 		r = "Aprobo"
# 		return r
# 	elif 0<n<5.5:
# 		r = "Participo"
# 		return r
# 	else:
# 		return "Error"

# print(evaluar(a))


#	CICLOS DEFINIDOS
# for i in range(10):
# 	print(i)
# print("\n")

# for i in "range(10)":
# 	print(i)
# print("\n")

# for i in [1,2,3,4,5,6,7]:
# 	print(i)
# print("\n")



# #	CICLOS INDEFINIDOS
# a = int(input("Ingrese cantidad de repeticiones: "))
# while a>0:
# 	print("A: ", a)
# 	a -= 1
# 	if a==5:
# 		continue
# 	print("B: ", a*a)
# 	if a==3:
# 		print("Llego a 3 papi")
# 		break



#	VALIDACION DE DATOS
# a = input("Direccion de mail: ")
# arroba = False
# espacio = False

# for letra in a:
# 	if letra == "@":
# 		arroba = True
# 	if letra == " ":
# 		espacio = True
# 		arroba = False
# 		break

# if arroba == True:
# 	print("Email correcto")
# elif espacio == True:
# 	print("Error, tiene un espacio en blanco")
# else:
# 	print("Error, falta la @")


