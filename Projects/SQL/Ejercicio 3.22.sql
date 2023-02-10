DROP TABLE Personal
CREATE TABLE Personal(Nombre VARCHAR(25), FechaIngreso DATE)
INSERT Personal(Nombre, FechaIngreso)
VALUES('Facu', '2010-06-10')
INSERT Personal(Nombre, FechaIngreso)
VALUES('Flor', '2003-06-10')
INSERT Personal(Nombre, FechaIngreso)
VALUES('Beto', '2012-06-10')
INSERT Personal(Nombre, FechaIngreso)
VALUES('Tere', '2001-06-10')

ALTER TABLE Personal ADD Legajo INT

DECLARE @NombrePersonal VARCHAR(25), @FechaIngresoPersonal DATE, @LegajoPersonal INT, @K INT

--DECLARE AgregarLegajo CURSOR FOR SELECT Nombre,FechaIngreso FROM Personal
--DECLARE AgregarLegajo CURSOR FOR SELECT * FROM Personal

DECLARE AgregarLegajo CURSOR FOR SELECT * FROM Personal ORDER BY FechaIngreso

OPEN AgregarLegajo

FETCH NEXT FROM Agregarlegajo
--FETCH NEXT FROM Agregarlegajo INTO @NombrePersonal, @FechaIngresoPersonal, @LegajoPersonal

SET @K = 1
--UPDATE Personal SET Legajo = @K WHERE CURRENT OF AgregarLegajo

WHILE @@FETCH_STATUS = 0
BEGIN
	UPDATE Personal SET Legajo = @K WHERE CURRENT OF AgregarLegajo
	FETCH NEXT FROM Agregarlegajo
	--FETCH NEXT FROM Agregarlegajo INTO @NombrePersonal, @FechaIngresoPersonal, @LegajoPersonal
	
	--SET @K = @K+1
	--UPDATE Personal SET Legajo = @K WHERE CURRENT OF AgregarLegajo
END
CLOSE AgregarLegajo
DEALLOCATE AgregarLegajo
