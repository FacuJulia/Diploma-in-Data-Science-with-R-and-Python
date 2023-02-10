import pandas as pd
import numpy as np
import os

os.chdir("C:/Users/ignac/Documents")

h = pd.read_excel('prueba.xlsx')

print(h)

h2 = pd.read_csv('prueba.csv')

print(h2)
print(h2["a"][1])

# guardo un elemento
h2["a"][1]=27

# obtengo un elemento
print(h2["a"][1])

# agrego una columna
v3 = np.zeros(3)
h2["d"] = v3

# imprimo h2
print(h2)

# imprimo las columnas
print(h2.columns)

# imprimo las cantidades
print("Número de columnas: ",len(h2.columns))
print("Número de filas:    ",len(h2["d"]))
print("Filas y columnas:   ",h2.shape)

h3 = h2.drop(["d"], axis = 1)

print(h3)

