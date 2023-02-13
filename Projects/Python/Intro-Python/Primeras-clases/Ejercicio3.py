# Definicion de clase con encapsulamiento, metodo y constructor

class Coche():
	def __init__(self, marca1):
		self.__marca = marca1

	def verMarca(self):
		return self.__marca

# Programa

Auto1 = Coche("Ford")
Auto2 = Coche("Audi")

print("La marca del auto 1 es: ", Auto1.verMarca())
print("La marca del auto 2 es: ", Auto2.verMarca())

Auto1 = Coche("Toyoya")
print("La marca del auto 1 es: ", Auto1.verMarca())