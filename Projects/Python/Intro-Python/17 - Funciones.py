# Funciones recursivas

def facto(n):
	if n==1:
		f = 1
	else:
		f = n * facto(n-1)
	return f

print(facto(5))


