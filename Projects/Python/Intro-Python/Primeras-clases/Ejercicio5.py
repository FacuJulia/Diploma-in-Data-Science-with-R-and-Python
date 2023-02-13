# Definicion de clase con encapsulamiento, metodo y constructor

class Coche():
	def __init__(self, marca1):
		self.__marca = marca1
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

	def apagarMotor(self):
		self.__motor = "Apagado"
		self.__luces = "Apagadas"
	
	def encenderLuces(self):
		if self.__motor == "Encendido":
			self.__luces = "Encendidas"
		else:
			print("No se puede pelotudo")

	def apagarLuces(self):
		self.__luces = "Apagadas"

	def __str__(self):
		return "Coche marca "+self.__marca

class Camioneta(Coche):
	def __init__(self, marca1, modelo1):
		super().__init__(marca1)
		#Coche.__init__(self,marca1)
		self.__modelo = modelo1
		self.__carga = 0
	
	def verModelo(self):
		return self.__modelo
	
	def verCarga(self):
		return self.__carga
	
	def modificarCarga(self, carga1):
		self.__carga = carga1
		
# Programa

Auto1 = Coche("Ford")
Auto2 = Coche("Toyota")
Camioneta1 = Camioneta("Chevrolet", "S10")

print("Datos Auto1")
print("Marca: ", Auto1.verMarca())
print("Motor: ", Auto1.verMotor())
print("Luces: ", Auto1.verLuces())
print("\nDatos Auto2")
print("Marca: ", Auto2.verMarca())
print("Motor: ", Auto2.verMotor())
print("Luces: ", Auto2.verLuces())
print("\nDatos Camioneta1")
print("Marca: ", Camioneta1.verMarca())
print("Luces: ", Camioneta1.verModelo())
print("Luces: ", Camioneta1.verCarga())
print("Motor: ", Camioneta1.verMotor())
print("Luces: ", Camioneta1.verLuces())
Auto1.encenderMotor()
Auto2.encenderLuces()
Camioneta1.modificarCarga(1500)
print("\nDatos Auto1")
print("Marca: ", Auto1.verMarca())
print("Motor: ", Auto1.verMotor())
print("Luces: ", Auto1.verLuces())
print("\nDatos Auto2")
print("Marca: ", Auto2.verMarca())
print("Motor: ", Auto2.verMotor())
print("Luces: ", Auto2.verLuces())
print("\nDatos Camioneta1")
print("Marca: ", Camioneta1.verMarca())
print("Luces: ", Camioneta1.verModelo())
print("Luces: ", Camioneta1.verCarga())
print("Motor: ", Camioneta1.verMotor())
print("Luces: ", Camioneta1.verLuces())

Auto1.apagarMotor()
Auto1.apagarLuces()

print("\n")
print(Auto1)
print(Auto2)