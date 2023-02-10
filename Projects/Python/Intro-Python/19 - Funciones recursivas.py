# Funciones recursivas

def facto(n):
	if n==1:
		f = 1
	else:
		f = n * facto(n-1)
	return f

def facto2(n):
	p = 1
	f = 1
	while p<=n:
		f = f * p
		p=p+1
	return f


print(facto(5))
print(facto2(5))
