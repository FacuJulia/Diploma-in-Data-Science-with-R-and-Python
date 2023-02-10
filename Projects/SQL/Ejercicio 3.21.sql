--DROP TABLE Socios
--DROP TABLE Familiares
--CREATE TABLE Socios(IdSocio INT, NombreSocio VARCHAR(25))
--CREATE TABLE Familiares(IdFamiliar INT, IdSocio INT, NombreFamiliar VARCHAR(25))

--DROP TRIGGER BorraFamiliares
--GO
--CREATE TRIGGER BorraFamiliares
	--ON Socios
	--AFTER delete
--AS
--	BEGIN
--		DELETE FROM Familiares WHERE IdSocio in (SELECT DISTINCT IdSocio FROM DELETED)
--	END
--GO

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

SELECT * FROM Liquidaciones
SELECT * FROM Sueldos


--DROP TRIGGER BorraFamiliares
GO
CREATE TRIGGER BorrarLiquidacion
	ON Sueldos
	AFTER delete
AS
	BEGIN
		DELETE FROM Liquidaciones WHERE Nombre in (SELECT DISTINCT Nombre FROM DELETED)
	END
GO

DELETE FROM Sueldos WHERE Nombre = 'Facu'
SELECT * FROM Liquidaciones
SELECT * FROM Sueldos


GO
CREATE TRIGGER AgregarEmpleado
	ON Sueldos
	AFTER delete
AS
	BEGIN
		--DELETE FROM Liquidaciones WHERE Nombre in (SELECT DISTINCT Nombre FROM DELETED)
	END
GO