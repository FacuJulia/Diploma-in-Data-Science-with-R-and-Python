DECLARE @N INT
	SET @N = 0

WHILE @N<=100
	BEGIN
	IF FLOOR(@N/2)*2 = @N
		BEGIN
		SELECT @N
		SELECT 'Es par'
		END
	SET @N = @N+1
END