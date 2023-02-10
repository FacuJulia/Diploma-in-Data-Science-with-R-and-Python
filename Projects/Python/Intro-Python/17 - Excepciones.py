# Manejo de excepciones

a = 10
b = 2

try:
	c = a/b
except ZeroDivisionError:
	print("No se puede dividir por cero")
	c = ""

print(c)