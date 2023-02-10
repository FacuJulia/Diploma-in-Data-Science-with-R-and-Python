# Ejecución condicional

a = 6
b = 6
c = 6

if a<b+c and b<a+c and c<a+b:
	print("Pueden ser los lados de un triángulo")

	if a==b and b==c:
		print("Equilátero")
	else:
		if a==b or b==c or c==a: 
			print("Isóceles")
		else:
			print("Escaleno")

else:
	print("No pueden ser los lados de un triángulo")

print("Terminé")