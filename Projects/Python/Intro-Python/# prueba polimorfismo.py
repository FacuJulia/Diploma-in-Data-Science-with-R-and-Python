# prueba herencia

class Padre():

	def __init__(self,estado):
		self.__Estado = estado

	def LeerEstado(self):
		return self.__Estado

	def EscribirEstado(self,Estado):
		self.__Estado = Estado

class Hijo(Padre):
	def Nombre(self):
		return "Julio"

	def LeerEstado(self):
		return "Ni en broma"


Padre1 = Padre("Estado 1")
Hijo1 = Hijo("Estado 3")

lista = [Padre1,Hijo1]

for x in lista:
	print(x.LeerEstado())
