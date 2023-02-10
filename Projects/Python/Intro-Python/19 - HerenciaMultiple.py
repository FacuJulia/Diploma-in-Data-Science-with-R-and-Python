# Objetos

class Coche():

	def __init__(self,marca):
		self._marca = marca

	def verMarca(self):
		return self._marca

	def __str__(self):
		return "Marca: "+self._marca+"\n"

class Barco():

	def __init__(self,calado):
		self._calado = calado
		print("Cargar calado: ",calado)

	def verCalado(self):
		return self._calado

	def __str__(self):
		return "Calado: "+str(self._calado)+"\n"

class Anfibio(Coche,Barco):

	def __init__(self,marca,calado):
		super().__init__(marca)
		Barco.__init__(self,calado)

	def __str__(self):
		r = super().__str__()
		r = r + Barco.__str__(self)
		return r

coche1 = Coche("Toyota")
anfibio1 = Anfibio("DWK",3)

print(coche1.verMarca())
print(anfibio1.verMarca())
print(anfibio1.verCalado())

lis = [coche1,anfibio1]

for x in lis:
	print(x)
	

