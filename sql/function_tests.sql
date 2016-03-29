---! just playing around with sql functions, testing out stuff like CROSS APPLY




USE BLAH

CREATE TABLE EMPLOYEE
(

	EMPID   INT NOT NULL
   ,MGRID   INT NOT NULL
   ,EMPNAME VARCHAR(10) NOT NULL
   ,SALARY  INT NOT NULL
   
)



INSERT INTO EMPLOYEE
SELECT 1111, 2222, 'RAFAEL', 100 UNION ALL
SELECT 2222, 2222, 'PABLO',  30000232  UNION ALL
SELECT 3333, 2222, 'RICK',   10



select * from EMPLOYEE

GO
alter FUNCTION fn_employeename
(
 @empid  int
)
RETURNS  TABLE
AS
RETURN
(

 SELECT EE.EMPNAME FROM EMPLOYEE EE where ee.EMPID = @empid
)GO




ALTER FUNCTION fn_employeename2
(
 @empid  int
)
RETURNS @somdata TABLE
(
	val varchaR(50)
)
AS
BEGIN

DECLARE @TT  TABLE (VAL VARCHAR(50))


 EXEC getone
 
RETURN
END

SELECT * FROM  fn_employeename2(1)



---!!!TESTING OUT THE CROSS APPLY !!!!
SELECT * FROM EMPLOYEE E1
CROSS APPLY fn_employeename(E1.EMPID)



create function raf()
returns table
as 
return(
select 1 dd
)
