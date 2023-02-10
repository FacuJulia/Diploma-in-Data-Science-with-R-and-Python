import math

def multiplo(a,b):
	if a==b*math.floor(a/b):
		w = True
	else:
		w = False
	return w

k=1
v=1
p=1

print(k,p,v)

while k!=100:
	if multiplo(k,7):
		v=-v
	if multiplo(k,11):
		p=p+2*v
	else:
		p=p+v

	k=k+1

	# mantengo la persona entre 1 y 10 pues forman un círculo
	if p>10:
		p=p-10
	if p<1:
		p=p+10

	print(k,p,v)



