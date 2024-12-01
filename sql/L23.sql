CREATE INDEX idx_products_category_id ON [dbo].[Products](category_id)
CREATE INDEX idx_order_items_product_id ON [dbo].[OrderItems](product_id)
CREATE INDEX idx_order_items_order_id ON [dbo].[OrderItems](order_id)

SELECT cat.name AS Category, SUM(oi.quantity*prod.price) AS TotalSum, SUM(oi.quantity) AS SoldCount, SUM(oi.quantity*prod.price)/SUM(oi.quantity) AS AvgPrice FROM [dbo].[Categories] cat
INNER JOIN [dbo].[Products] prod ON cat.id=prod.id
INNER JOIN [dbo].[OrderItems] oi ON oi.product_id=prod.id
GROUP BY  cat.name
ORDER BY TotalSum DESC