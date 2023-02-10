DROP TABLE Jugadores

--EJERCICIO 2.1
--NOMBRE TABLA: "Jugadores"
--NOMBRE CAMPOS: "Nombre", "Apellido", "Edad", "Puesto", "DNI"
CREATE TABLE Jugadores(Id int, Nombre nvarchar(25), Apellido nvarchar(25), Edad int, Puesto nvarchar(25), DNI int)

--EJERCICIO 2.2
INSERT INTO Jugadores(Id, Nombre, Apellido, Edad, Puesto, DNI)
VALUES(1, 'Alberto', 'Perez', 21, 'Delantero', 31222333)
INSERT INTO Jugadores(Id, Nombre, Apellido, Edad, Puesto, DNI)
VALUES(2, 'Juan', 'Rodriguez', 23, 'Defensor', 30222444)
INSERT INTO Jugadores(Id, Nombre, Apellido, Edad, Puesto, DNI)
VALUES(3, 'Jose', 'Sanchez', 25, 'Arquero', 29444333)

--EJERCICIO 2.3
SELECT DNI, Nombre FROM Jugadores

--EJERCICIO 2.4
DELETE FROM Jugadores WHERE Edad<=21
SELECT * FROM Jugadores

--EJERCICIO 2.5
UPDATE Jugadores SET Edad = 38 WHERE Apellido='Rodriguez'
SELECT * FROM Jugadores