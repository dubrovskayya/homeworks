--1

SELECT YEAR(soh.OrderDate) AS Year, AVG(soh.TotalDue) AS AverageSum, COUNT(1) AS OrderCount
, CASE
WHEN COUNT(1)>500
THEN 'High'
WHEN COUNT(1) BETWEEN 300 AND 500
THEN 'Medium'
ELSE 'Low'
END AS Demand
FROM Sales.SalesOrderHeader soh
GROUP BY YEAR(soh.OrderDate)
HAVING AVG(soh.TotalDue)>2000
ORDER BY Year

--2

SELECT pc.Name, SUM(sod.LineTotal) AS FullSalesSum, AVG(sod.UnitPriceDiscount) AS AverageDiscount 
, CASE
WHEN SUM(sod.LineTotal)>200000
THEN 'Top Category'
WHEN SUM(sod.LineTotal) BETWEEN 100000 AND 200000
THEN 'Mid Category'
ELSE 'Low Category'
END AS Category
FROM Production.Product pp
JOIN Sales.SalesOrderDetail sod ON pp.ProductID=sod.ProductID
JOIN Production.ProductSubcategory ps ON ps.ProductSubcategoryID=pp.ProductSubcategoryID
JOIN Production.ProductCategory pc ON ps.ProductCategoryID=pc.ProductCategoryID
GROUP BY pc.Name
HAVING SUM(sod.LineTotal)>50000

--3

SELECT sp.Name AS RegionName, AVG(soh.TotalDue) AS AverageSum, COUNT(1) AS OrderNumber,
CASE
WHEN  AVG(soh.TotalDue)>3000
THEN 'Expensive'
WHEN  AVG(soh.TotalDue) BETWEEN 2000 AND 3000
THEN 'Moderate'
ELSE 'Affordable'
END AS Category
FROM Person.StateProvince sp
JOIN Person.Address pa ON  pa.StateProvinceID=sp.StateProvinceID
JOIN Sales.SalesOrderHeader soh ON soh.ShipToAddressID=pa.AddressID
GROUP BY sp.Name
HAVING AVG(soh.TotalDue)>1500

--4

SELECT DATENAME(WEEKDAY, soh.OrderDate) AS WeekDay,COUNT(1) AS OrderNumber, AVG(sod.UnitPriceDiscount) AS AverageDiscount,
CASE
WHEN  COUNT(1)>300
THEN 'Peak Day'
WHEN  COUNT(1) BETWEEN 200 AND 300
THEN 'High Traffic'
ELSE 'Regular'
END AS Traffic
FROM Sales.SalesOrderHeader soh
JOIN Sales.SalesOrderDetail sod ON soh.SalesOrderID=sod.SalesOrderID
GROUP BY DATENAME(WEEKDAY, soh.OrderDate)
HAVING COUNT(1)>100