# Definicion de clases con encapsulamiento y metodo

class Coche():
	__marca = "Toyota"

	def verMarca(self):
		return self.__marca

#Programa

Auto = Coche()

print("La marca del auto 1 es: ", Auto.verMarca())

