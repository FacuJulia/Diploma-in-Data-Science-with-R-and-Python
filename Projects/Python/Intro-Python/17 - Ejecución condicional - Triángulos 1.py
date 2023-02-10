# Distinguir si tres números pueden ser las longitudes de los lados de un triángulo

a = 7
b = 6
c = 5

if a<b+c and b<a+c and c<b+a:
	print("Pueden ser los lados de un triángulo")
else:
	print("No pueden ser los lados de un triángulo")

print("Terminé")
