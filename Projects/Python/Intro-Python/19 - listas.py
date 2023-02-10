# listas

lis = [1,3,"hola",True]

print(lis)
print(type(lis))
print(lis[0])
lis.append("ja ja ja")
print(lis)
print(len(lis))
lis.insert(3,3)
print(lis)
lis[3]= 9
lis.remove(9)
print(lis)
print(3 in lis)
lis2 = ["si","no"]
lis.extend(lis2)
lis.append(lis2)
print(lis)
