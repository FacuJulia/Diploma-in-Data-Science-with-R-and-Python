# división por cero

a = 5

while a>-3:
	a=a-1
	try:
		b = 5/a
	except ZeroDivisionError:
		b = "NA"
		
	print(a,b)

print("Terminé")

