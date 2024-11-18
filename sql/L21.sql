
CREATE PROCEDURE dbo.GoodsAnalysis 
AS
BEGIN
	CREATE TABLE ProductInventorySummary(ProductID INT, TotalQuantity INT)

	DECLARE @Counter INT
	SELECT @Counter = MIN(ProductID)
	FROM Production.ProductInventory 

	WHILE @Counter<=(SELECT MAX(ProductID) FROM Production.ProductInventory )
		BEGIN
		INSERT INTO ProductInventorySummary
		SELECT ppI.ProductID, SUM(ppi.Quantity)
		FROM Production.ProductInventory ppi
		GROUP BY ppi.ProductID
		HAVING ppi.ProductID=@Counter
		SET @Counter+=1
		END
END

EXEC dbo.GoodsAnalysis 
SELECT * FROM ProductInventorySummary



