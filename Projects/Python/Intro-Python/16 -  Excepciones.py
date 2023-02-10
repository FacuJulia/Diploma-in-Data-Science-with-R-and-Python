# Excepciones

a = 1
b = 0

try:
	c = a/b
except ZeroDivisionError:
	print("No se puede dividir por cero")
	c = ""


print(c)

