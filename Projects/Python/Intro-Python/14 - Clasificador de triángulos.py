# Clasificador de triángulos

a = 4
b = 4 
c = 4

if a==b and b==c:
	print("Equilátero")
else:
	if a==b or b==c or c==a:
		print("Isóceles")
	else:
		print("Escaleno")


print("Terminé")