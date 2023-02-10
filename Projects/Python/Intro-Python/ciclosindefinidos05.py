# Ciclos indefinidos

lis = [1,1,1,2,3,3,5,7,True,1]

eliminar = 1
c = 0

while eliminar in lis:
	lis.remove(eliminar)
	c = c + 1
	

print(lis)
print("Eliminé: ",c,"ocurrencias de ",eliminar)



