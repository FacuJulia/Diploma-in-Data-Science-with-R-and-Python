# ciclos anidados

t1 = (1,2,3,4)
t2 = ("a","b","c","d")

for x in t1:
	for y in t2:
		print(x,y)
		if y == "c":
			break

