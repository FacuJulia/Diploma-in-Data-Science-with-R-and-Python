#Definicion de clase

class Coche():
	marca = ""

#Programa

Auto1 = Coche()
Auto2 = Coche()

Auto1.marca = "Chevrolet"
Auto2.marca = "Toyota"

print("La marca del auto 1 es: ", Auto1.marca)

Auto1.marca = "Perro"
print("La marca del auto 1 es: ", Auto1.marca)