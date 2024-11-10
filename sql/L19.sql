
--1
DECLARE @factor INT
SET @factor=1

DECLARE @number INT
SET @number=6

WHILE @factor<11
BEGIN
SELECT CONCAT(@number,'*',@factor,'=',@factor*@number)
SET @factor=@factor+1
END


--2
DECLARE @workAge INT
SET @workAge=12
SELECT pp.FirstName,pp.LastName, DATEDIFF(YEAR,e.HireDate,GETDATE()) AS WorkingYears
FROM [Person].[Person] pp
JOIN HumanResources.Employee e ON pp.BusinessEntityID=e.BusinessEntityID
WHERE DATEDIFF(YEAR,e.HireDate,GETDATE())>@workAge


--3
DECLARE @maxExpences INT
SET @maxExpences=2000

SELECT sc.CustomerID, 
(SELECT SUM(soh.TotalDue)
FROM Sales.SalesOrderHeader soh
WHERE sc.CustomerID=soh.CustomerID) AS TotalExpences
FROM Sales.Customer sc
WHERE (SELECT SUM(soh.TotalDue)
FROM Sales.SalesOrderHeader soh
WHERE sc.CustomerID=soh.CustomerID) > @maxExpEnces


--4
WITH tempo AS(
SELECT YEAR(soh.OrderDate) AS Year,SUM(sod.OrderQty) AS TotalQuantity, sod.ProductID
FROM Sales.SalesOrderDetail sod
JOIN Sales.SalesOrderHeader soh ON soh.SalesOrderID=sod.SalesOrderID
GROUP BY sod.ProductID, YEAR(soh.OrderDate)
)

SELECT t.Year, t.TotalQuantity AS MaxQuantity,pp.Name AS ProductName FROM tempo t
JOIN Production.Product pp ON pp.ProductID=t.ProductID
WHERE t.TotalQuantity=(SELECT MAX(tt.TotalQuantity) 
FROM tempo tt
WHERE tt.Year=t.Year)







