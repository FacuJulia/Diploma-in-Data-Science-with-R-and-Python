# listas

lis = [1,3,"Hola",True]

print(lis)
print(type(lis))
print(lis[3])
lis.append("Hola")
print(lis)
lis.insert(1,False)
print(lis)
lis.remove(lis[3])
print(lis)
lis2 = ["a","b"]
lis.extend(lis2)
print(lis)
print(1 in lis)
print(1 in lis2)
