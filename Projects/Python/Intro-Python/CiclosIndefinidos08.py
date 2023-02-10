# Ciclos indefinidos

from math import floor

a = 100

while a>10:
	print(a)
	a = a/2

	if a!=floor(a):
		break

print("Fin")


