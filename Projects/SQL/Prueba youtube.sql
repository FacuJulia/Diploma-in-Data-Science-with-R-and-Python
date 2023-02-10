--BORRO LA TABLE
DROP TABLE Clients

--CREO LA TABLA
CREATE TABLE Clients(Id int, Nombre nvarchar(50), Apellido nvarchar(50), FechaNacimiento date);
--MUESTRO TODAS LAS COLUMNAS DE LA TABLA CON *
--SELECT * FROM Clients

--AGREGO UNA COLUMNA FALTANTE A LA TABLA YA CREADA
ALTER TABLE Clients ADD Address nvarchar(250)
--SELECT * FROM Clients

--CARGO LAS FILAS DE LA TABLA
INSERT INTO Clients(Id, Nombre, Apellido, FechaNacimiento, Address)
VALUES(1, 'Facu', 'Julia', '15-07-94', 'Santotome')
INSERT INTO Clients(Id, Nombre, Apellido, FechaNacimiento, Address)
VALUES(2, 'Flor', 'Dalotto', '16-07-94', 'Mendoza')
INSERT INTO Clients(Id, Nombre, Apellido, FechaNacimiento, Address)
VALUES(3, 'Daniel', 'Dalotto', '18-02-70', 'Llerena')
INSERT INTO Clients(Id, Nombre, Apellido, FechaNacimiento, Address)
VALUES(4, 'Cristina', NULL, '12-12-65', 'Llerena')
SELECT * FROM Clients

--AGREGO UN REGISTRO ESPECIFICO 
--UPDATE Clients SET Apellido = 'Padro' WHERE Id=4
--SELECT * FROM Clients

--MUESTRO SOLO LAS COLUMNAS REQUERIDAS
--SELECT Nombre,Apellido FROM Clients

--MUESTRO SOLO LAS FILAS REQUERIDAS
--SELECT * FROM Clients
--WHERE Id>1

--BORRO DESDE LA FILA 2 EN ADELANTE
--DELETE FROM Clients WHERE Id>2
--SELECT * FROM Clients

