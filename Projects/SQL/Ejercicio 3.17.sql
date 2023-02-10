--CREATE FUNCTION Funcion

--AS
--BEGIN
	--RETURN
--END


DECLARE @V1 INT
DECLARE @V2 INT
DECLARE @RES INT

SET @RES = @V1 + @V2
SELECT @RES


-- AÑO BISIESTO
--Divisible entre 4.
--No divisible entre 100.
--Divisible entre 400. (2000 y 2400 son bisiestos pues aún siendo divisibles entre 100 lo son también entre 400. Pero los años 1900, 2100, 2200 y 2300 no lo son porque sólo son divisibles entre 100).

DECLARE @Y INT
DECLARE @D INT
SET @Y=2024

IF FLOOR(@Y/4)*4 = @Y
	BEGIN
	IF FLOOR(@Y/100)*100 = @Y
	BEGIN
		IF FLOOR(@Y/400)*400 = @Y
		BEGIN
			SET @D = 29
		END
		ELSE
		BEGIN
			SET @D = 28
		END
	END
	ELSE
	BEGIN
	SET @D = 29
	END
END
ELSE
	BEGIN
	SET @D = 28
END

SELECT @D