# listas

lis = [1,3,"Hola",True]

print(lis)
print(type(lis))

print(lis[1])
lis[1]=17
print(lis[1])

lis.append("a")
print(lis)
print(len(lis))

lis2 = ["a","b","a"]
lis.extend(lis2)
print(lis)

lis.remove("a")
print(lis)

print('z' in lis)
