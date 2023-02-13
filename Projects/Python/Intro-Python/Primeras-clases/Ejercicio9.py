#Paquete numpy - error, estadistica y matriz

lista1=[1,2,3,4]
lista2=[5,6,7]

v1=numpy.array(lista1)
v2=numpy.array(lista2)

v1+v2 #distinto largo error

prom1 = numpy.mean(v1)
prom2 = numpy.mean(v2)

v3 = v1[2:4]
v4 = numpy.zeros(3)
v5 = numpy.ones(4)

type(v5[1])

dims = (3,4) #tupla

matriz = numpy.zeros(dims)
matriz.shape
