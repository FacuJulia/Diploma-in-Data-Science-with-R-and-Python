# objetos

class Coche():

	def __init__(self, m):
		self.__marca = m
		self.__motor = "Apagado"
		self.__luces = "Apagadas"

	def verMarca(self):
		return self.__marca

	def verMotor(self):
		return self.__motor

	def encenderMotor(self):
		self.__motor = "Encendido"

	def apagarMotor(self):
		self.__motor = "Apagado"
		self.__luces = "Apagadas"

	def verLuces(self):
		return self.__luces

	def encenderLuces(self):
		if self.__motor == "Encendido":
			self.__luces = "Encendidas"
		else:
			print("No se pueden prender las luces con el motor apagado")

	def apagarLuces(self):
		self.__luces = "Apagadas"

	def verEstado(self):
		s = "Marca: "+self.__marca+ "Motor: "+self.__motor+ "Luces: "+self.__luces
		return s

class Camioneta(Coche):

	def __init__(self,m,c):
		super().__init__(m)
		self.__carga = c

	def verCarga(self):
		return self.__carga

	def cargar(self,c):
		self.__carga = c

	def verEstado(self):
		s = super().verEstado()
		s = s + "Carga: " +  str(self.__carga)
		return s

miCoche = Coche("Fiat")

miCamioneta = Camioneta("Ford",50)

print(miCamioneta.verEstado())
miCamioneta.cargar(100)
print(miCamioneta.verCarga())
print(miCamioneta.verEstado())

lis = [miCoche,miCamioneta]

for x in lis:
	print(x.verEstado())
	