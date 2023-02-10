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
			print("Debe encender el motor")

	def apagarLuces(self):
		self.__luces = "Apagadas"

	def __str__(self):
		ret = "Marca: "+self.__marca+"\n"+"Motor: "+self.__motor+"\n"+"Luces: "+self.__luces
		return ret

class Camioneta(Coche):

	def __init__(self,m):
		super().__init__(m)
		self.__carga = 0

	def __str__(self):
		ret = super().__str__()
		ret = ret + "\n" + "Carga: "+str(self.__carga)
		return ret

	def cargar(self,c):
		self.__carga = c

miCoche1 = Coche("Toyota")
miCoche2 = Coche("Fiat")
miCamioneta1 = Camioneta("Rastrojero")
miCamioneta1.cargar(10)

lis = [miCoche1,miCoche2,miCamioneta1]

for x in lis:
	print(x)