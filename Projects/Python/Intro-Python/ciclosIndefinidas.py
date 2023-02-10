# ciclos indefinidos

import math

n = 100

while n>10:
	n=n/2
	print(n)
	if n != math.floor(n):
		break
		

