# objetos

class Coche():

	def __init__(self,m,p):
		self.__marca = m
		self.__motor = "Apagado"
		self.__luces = "Apagadas"
		self.peso = p

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
			print("No se pueden encender las luces con el motor apagado")

	def apagarLuces(self):
		self.__luces = "Apagadas"		

class Camioneta(Coche):

	def __init__(self,m,p,c):
		super().__init__(m,p)
		self.__carga = c

	def verCarga(self):
		return self.__carga

miCoche = Coche("BMW",500)
miCamioneta = Camioneta("Kangoo",2500,50)

print(miCoche.verMarca())
print(miCoche.verMotor())
miCoche.encenderLuces()
print(miCoche.verLuces())
miCoche.peso = 1500
print(miCoche.peso)

print(miCamioneta.verMarca())
print(miCamioneta.verCarga())

lis = [miCoche,miCamioneta]

for x in lis:
	print(type(x))

