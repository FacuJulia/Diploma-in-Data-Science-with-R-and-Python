--CREATE TABLE Clientes(CUIT INT, Nombre VARCHAR(25), Direccion VARCHAR(25))
--CREATE TABLE Facturas(CUIT INT, IdFactura INT, Fecha DATE, CondicionPago VARCHAR(25), FechaVencimiento DATE, SubTotal INT, Impuesto INT)
--CREATE TABLE Renglones(IdFactura INT, IdRenglon INT, IdArticulo INT, Cantidad INT, Precio INT)
--CREATE TABLE Articulos(IdArticulo INT, Articulo VARCHAR(25))

--CREATE TABLE clientes(IdCliente INT NOT NULL,FechaAlta DATE NOT NULL,RazonSocial VARCHAR(50) NOT NULL,Vendedor VARCHAR(50) NULL)

--	EJERCICIO 3.8
DROP VIEW ClientesPepe
DROP VIEW Facturas1


--	EJERCICIO PRACTICO 3.4
GO
CREATE VIEW ClientesPepe
AS
SELECT * FROM clientes where vendedor = 'PEPE'
GO


--	EJERCICIO PRACTICO 3.6
SELECT * FROM ClientesPepe


--	EJERCICIO PRACTICO 3.5
GO
CREATE VIEW Facturas1
AS
SELECT CUIT, IdFactura, SubTotal FROM Facturas
GO

SELECT * FROM Facturas1


--	EJERCICIO PRACTICO 3.7
SELECT CUIT FROM Facturas1





--	EJERCICIO PRACTICO 3.9 / 3.10 - 'PEPE' / @VENDEDOR
GO
CREATE PROCEDURE ProcedimientoVerCliente
@VENDEDOR VARCHAR(25)
AS
BEGIN
SELECT * FROM clientes where vendedor = @VENDEDOR
END
GO


--	EJERCICIO PRACTICO 3.11
EXEC ProcedimientoVerCliente 'PEPE'


--	EJERCICIO PRACTICO 3.12
DROP PROCEDURE ProcedimientoVerCliente