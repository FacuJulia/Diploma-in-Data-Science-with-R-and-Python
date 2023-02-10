--AVG: Promedio
--COUNT: Cuenta
--MAX: Nos devuelve el máximo
--MIN: Nos devuelve el mínimo
--SUM: Nos devuelve la suma

DROP TABLE Sueldos
CREATE TABLE Sueldos(Nombre VARCHAR(25), Sueldo INT)
INSERT INTO Sueldos(Nombre,Sueldo)
VALUES('Facu',2000)
INSERT INTO Sueldos(Nombre,Sueldo)
VALUES('Flor',1000)
INSERT INTO Sueldos(Nombre,Sueldo)
VALUES('Tere',4000)
INSERT INTO Sueldos(Nombre,Sueldo)
VALUES('Beto',8000)

SELECT AVG(Sueldo) FROM Sueldos
SELECT MAX(Sueldo) FROM Sueldos
SELECT MIN(Sueldo) FROM Sueldos
SELECT SUM(Sueldo) FROM Sueldos
SELECT COUNT(Sueldo) FROM Sueldos


DROP TABLE Liquidaciones
CREATE TABLE Liquidaciones(Nombre VARCHAR(25), Mes INT, Liquidacion INT)
INSERT INTO Liquidaciones(Nombre,Mes,Liquidacion)
VALUES('Facu',1,500)
INSERT INTO Liquidaciones(Nombre,Mes,Liquidacion)
VALUES('Flor',4,700)
INSERT INTO Liquidaciones(Nombre,Mes,Liquidacion)
VALUES('Tere',8,1000)
INSERT INTO Liquidaciones(Nombre,Mes,Liquidacion)
VALUES('Beto',12,400)

SELECT * FROM Liquidaciones
SELECT * FROM Sueldos