# Manejo de excepciones

a = 5
b = 0

try:
	c = a/b
except ZeroDivisionError:
	print("No se puede dividir por cero")
	c = ""

print(c)