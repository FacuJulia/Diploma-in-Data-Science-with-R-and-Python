# listas

lis = [1,3,"Hola",False]

print(lis)
print(type(lis))

print(lis[1])
lis[1] = 'si'

print(lis)
print(len(lis))
lis.append("xyz")
print(lis)

lis2 = ["si","no"]

lis.extend(lis2)
print(lis)

print(5 in lis)

lis.remove("si")

print(lis)