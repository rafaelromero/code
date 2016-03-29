--just a template for sql cursors (since I always forget the syntax!)

DECLARE @EmployeeID INT
DECLARE @EmployeeNumber VARCHAR(250)
DECLARE @ActiveSecurityUserId INT
DECLARE @StartDate DATETIME

SET @ActiveSecurityUserId   = 1
SET @StartDate	            = '2013-01-01 00:00:00.000'


DECLARE db_cursor CURSOR FOR  
SELECT '000111somenumber' EmployeeNumber 

OPEN db_cursor   
FETCH NEXT FROM db_cursor INTO @EmployeeNumber 

WHILE @@FETCH_STATUS = 0   
BEGIN
  



		--cursor logic here!!! :)



     
FETCH NEXT FROM db_cursor INTO @EmployeeNumber   
END   

CLOSE db_cursor   
DEALLOCATE db_cursor


