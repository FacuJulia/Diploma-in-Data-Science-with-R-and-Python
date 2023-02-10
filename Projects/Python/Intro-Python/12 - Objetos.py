# Objetos

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

	def verEstado(self):
		print("Marca: ",self.__marca, "Motor: ", self.__motor, "Luces: ", self.__luces)

	def encenderMotor(self):
		self.__motor = "Encendido"

	def encenderLuces(self):
		if self.__motor == "Apagado":
			print("Debe encender primero el motor, ojo la batería!")
		else:
			self.__luces = "Encendidas"

	def apagarMotor(self):
		self.__motor = "Apagado"
		self.__luces = "Apagadas"

	def apagarLuces(self):
		self.__luces = "Apagadas"

class Camioneta(Coche):

	def __init__(self,m,c):
		super().__init__(m)
		self.__carga = c

	def cargar(self,c):
		self.__carga = c

	def verCarga(self):
		return self.__carga

	def verEstado(self):
		print("Marca: ",self.verMarca(), "Motor: ", self.verMotor(), "Luces: ", self.verLuces(), "Carga: ", self.__carga)

coche1 = Coche("Toyota")
coche2 = Coche("Audi")
camioneta1 = Camioneta("Ford",100)

# camioneta1.cargar(100)
coche2.encenderMotor()
coche2.encenderLuces()
coche2.apagarMotor()


lis = [coche1,coche2,camioneta1]

for x in lis:
	x.verEstado()



