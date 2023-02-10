# Clasificación de triángulos

a = 4
b = 6
c = 5

if a==b and b==c:
	print("Equilátero")
else:
	if a==b or b==c or c==a:
		print("Isóceles")
	else:
		print("Escaleno")


