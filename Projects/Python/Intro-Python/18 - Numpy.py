import numpy as np

lista = [1,3,5,7,9]

vector = np.array(lista)

# impresión
print(lista)
print(vector)

# operaciones
vector = vector + 1
print(vector)
print(vector*2)
print(vector+vector)
print(vector*vector)

# funciones estadísticas básicas
print(np.mean(vector))
print(np.std(vector))

# sacar tajada de un vector
print(vector[3:5])


v = np.zeros((3,2,4))

print(v)

v[0,1,2] = 17
print(v[0,1,2])
# visualizo la ubicación
print(" visualizo la ubicación")
print(v)

m = np.zeros((3,3))
print(m)

print("2x2x2")
c = np.zeros((2,2,2))
print(c)

r = np.random.rand(10)
print(np.mean(r))
print(np.std(r))

r = np.concatenate([r,r])
print(np.mean(r))
print(np.std(r))
print(len(r))