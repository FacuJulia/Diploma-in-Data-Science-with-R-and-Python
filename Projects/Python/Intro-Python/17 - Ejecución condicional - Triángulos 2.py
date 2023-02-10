# Distinguir si tres números pueden ser las longitudes de los lados de un triángulo y clasificarlo

a = 7
b = 7
c = 27

if a<b+c and b<a+c and c<b+a:
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
