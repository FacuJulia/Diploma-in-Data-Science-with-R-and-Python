# Reconocer y clasificar triángulos

a = 5
b = 15
c = 5

if a<b+c and b<a+c and c<a+b:
	print("Triángulo")
	if a==b and b==c:
		print("Equilátero")
	else:
		if a==b or b==c or c==a:
			print("Isóceles")
		else:
			print("Escaleno")
else:
	print("No triángulo")

