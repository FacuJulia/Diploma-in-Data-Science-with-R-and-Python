# Ciclos definidos

a = 3

for i in range(5):
	for j in range(3):
		print(i,j)
		if j >= i:
			break

print("Terminamos")