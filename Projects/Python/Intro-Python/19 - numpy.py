import numpy as np

lista = [1,3,5,7,9]

vector = np.array(lista)

print(lista)
print(vector)

vector = vector + 1

print(vector)
print(vector*2)
print(vector+vector)
print(vector*vector)

print("Promedio: ",np.mean(vector))
print("Desvío:   ",np.std(vector))
print("Slice [3:5]: ",vector[3:5])

v = np.zeros((3,2,4))

print("Cubo de 3 x 2 x 4:")
print(v)

print("Elemento [0,0,0]:")
print(v[0,0,0])

print("Números aleatorios en Numpy:")
v[0,0,:] = np.random.rand(4)

print(v)

print("Agregación:")
print(v.sum())