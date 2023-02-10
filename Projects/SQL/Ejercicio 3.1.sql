--EJERCICIO 2.12

--DROP TABLE dbo.Pesonas
CREATE TABLE Personas(DNI INT NOT NULL, Nombre VARCHAR(25) NOT NULL, Apellido VARCHAR(25) NOT NULL, Edad INT NOT NULL, Estudios VARCHAR(25) NULL)
-- DNI Clave primaria es unico para cada persona en principio

--DROP TABLE dbo.Automovil
CREATE TABLE Automovil(NumeroChasis INT NOT NULL, Marca VARCHAR(25), Modelo VARCHAR(25))
-- Numero de chasis clave primaria es unico para cada automovil

--DROP TABLE dbo.Casa
CREATE TABLE Casa(Direccion VARCHAR(25) NOT NULL, NumeroCatastro INT NOT NULL, Provincia VARCHAR(25), Ciudad VARCHAR(25))
--Numero catastro clave primaria es unico para cada casa

-- INDICES 
--CREATE CLUSTERED INDEX i ON Personas(DNI ASC)
CREATE NONCLUSTERED INDEX H ON Personas(Nombre ASC)

--CREATE CLUSTERED INDEX j ON Automovil(NumeroChasis ASC)
CREATE NONCLUSTERED INDEX O ON Automovil(Marca ASC)

--CREATE CLUSTERED INDEX k ON Casa(NumeroCatastro ASC)
CREATE NONCLUSTERED INDEX P ON Casa(Provincia ASC)


--CREATE VIEW ClientesDePepe
--AS
--SELECT * FROM dbo.clientes WHERE Vendedor = "PEPE"
