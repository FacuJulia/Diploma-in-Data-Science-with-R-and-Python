# Excepciones

a = 3
b = "4"

try:
	c = a/b
except ZeroDivisionError:
	print("No se puede dividir por cero")
	c = ""
except TypeError:
	print("Debe dividir números")
	c = ""

print(c)
print("Terminé")