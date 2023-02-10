# objetos

class Coche():

	def __init__(self,m):
		self.__marca = m
		self.__motor = "Apagado"
		self.__luces = "Apagadas"

	def verMarca(self):
		return self.__marca

	def verMotor(self):
		return self.__motor

	def verLuces(self):
		return self.__luces

	def encenderMotor(self):
		self.__motor = "Encendido"

	def encenderLuces(self):
		if self.__motor == "Encendido":
			self.__luces = "Encendidas"
		else:
			print("No se puede encender las luces cuando el motor está apagado")

	def apagarMotor(self):
		self.__motor = "Apagado"
		self.__luces = "Apagadas"

	def apagarLuces(self):
		self.__luces = "Apagadas"

	def imprimirEstado(self):
		print(self.__marca, self.__motor, self.__luces)

class Camioneta(Coche):

	def __init__(self,m,c):
		super().__init__(m)
		self.__carga = c

	def verCarga(self):
		return self.__carga

	def cargar(self,c):
		self.__carga = c

	def imprimirEstado(self):
		print(self.verMarca(), self.verMotor(), self.verLuces(), self.__carga)


miCoche = Coche("BMW")
miCoche2 = Coche("Mercedes Benz")
miCamioneta = Camioneta("Renault",0)
miCamioneta.cargar(100)

lista = [miCoche, miCoche2, miCamioneta]

for x in lista:
	x.imprimirEstado()

miCoche.encenderMotor()
miCoche2.encenderMotor()
miCoche2.encenderLuces()
miCoche2.apagarMotor()

for x in lista:
	x.imprimirEstado()




