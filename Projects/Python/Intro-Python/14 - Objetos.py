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

	def encenderLuces(self):
		if self.__motor == "Encendido":
			self.__luces = "Encendidas"
		else:
			print("Ni loco")

	def apagarLuces(self):
		self.__luces = "Apagadas"

	def verLuces(self):
		return self.__luces


class Camioneta(Coche):
	
	def __init__(self,m,c):
		super().__init__(m)
		self.__carga = c

	def verCarga(self):
		return self.__carga

	def cargar(self,c):
		self.__carga = c 


c1 = Coche("Ford")
c2 = Coche("BMW")
c3 = Camioneta("Renault", 0)

print(c1.verMarca(),c1.verMotor(), c1.verLuces())
print(c2.verMarca(),c2.verMotor(), c2.verLuces())
print(c3.verMarca(),c3.verMotor(), c3.verLuces())

c1.encenderMotor()
c2.encenderMotor()
c2.encenderLuces()
c2.apagarMotor()
c3.cargar(100)

print(c1.verMarca(),c1.verMotor(), c1.verLuces())
print(c2.verMarca(),c2.verMotor(), c2.verLuces())
print(c3.verMarca(),c3.verMotor(), c3.verLuces(), c3.verCarga())

lis = [c1,c2,c3]

for x in lis:
	print(x.verMarca())

	